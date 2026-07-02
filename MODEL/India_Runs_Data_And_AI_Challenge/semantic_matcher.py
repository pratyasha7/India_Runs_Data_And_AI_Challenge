import re 
from quality_controller import _safe_float

#  KEYWORD DICTIONARIES (Pulled straight from the Job Description) 

# Central Information Retrieval (IR) and search platform concepts 
CORE_IR_KEYWORDS = {
    "ranking", "recommendation", "recommender", "retrieval", "hybrid search", 
    "search engine", "information retrieval", "query parsing", "matching system",
    "matching engine", "item-to-item", "collaborative filtering"
}

# Modern vector databases, search indexes, and embedding tools
VECTOR_DB_KEYWORDS = {
    "milvus", "pinecone", "qdrant", "weaviate", "faiss", "elasticsearch", 
    "opensearch", "lucene", "embeddings", "sentence-transformers", "bge", "e5"
}

# Rigorous search ranking evaluation metrics (The JD emphasizes these heavily)
EVALUATION_METRICS = {
    "ndcg", "mrr", "map", "precision@10", "recall", "offline evaluation", 
    "evaluation framework", "ab test", "a/b testing", "ranking evaluation"
}

# High-value bonus skills (nice-to-haves, but not strict requirements)
DESIRABLE_ML_KEYWORDS = {
    "fine-tuning", "fine tuning", "lora", "qlora", "peft", "llm", "xgboost", 
    "learning-to-rank", "learning to rank", "peft", "distributed systems"
}

# Out-of-scope fields (Computer Vision, Speech, Robotics) that get penalized
RED_FLAG_DOMAINS = {
    "computer vision", "yolo", "opencv", "image segmentation", "object detection", 
    "speech recognition", "tts", "text-to-speech", "robotics", "ros", "gans", "gan"
}

#TEXT CLEANING HELPERS 

def _clean_text(text) -> str:
    """Clean and lowercase text so we don't miss matches due to capitalization."""
    if not text:
        return ""
    return str(text).lower().strip()

# THE SEMANTIC SCORER 

def calculate_relevance_score(candidate) -> float:
    """
    Scans a candidate's text profile and scores their relevance from 0.0 to 1.0 [3].
    Analyzes their headline, summary, skills, and historical job descriptions.
    """
    profile = candidate.get("profile", {}) or {}
    skills = candidate.get("skills", []) or []
    history = candidate.get("career_history", []) or []
    
    # 1. Assemble the candidate's text data into readable blocks
    headline = _clean_text(profile.get("headline", ""))
    summary = _clean_text(profile.get("summary", ""))
    skills_names = [_clean_text(s.get("name", "")) for s in skills]
    skills_corpus = " ".join(skills_names)
    
    # Stitch together their previous job titles and descriptions
    history_corpus = ""
    for job in history:
        desc = _clean_text(job.get("description", ""))
        title = _clean_text(job.get("title", ""))
        history_corpus += f" {title} {desc}"

    # Merge everything into one master string for fast scanning
    full_profile_corpus = f"{headline} {summary} {skills_corpus} {history_corpus}"

    # 2. Evaluate their experience across the 4 key dimensions
    score = 0.0
    
    # Dimension A: Hands-on Search/IR/Recommendation experience (Max +0.40)
    # We prioritize actual work history descriptions over simple keyword-stuffed skills 
    ir_matches = sum(1 for keyword in CORE_IR_KEYWORDS if keyword in history_corpus)
    if ir_matches > 0:
        score += min(0.40, ir_matches * 0.15)
    elif any(keyword in full_profile_corpus for keyword in CORE_IR_KEYWORDS):
        score += 0.15  # They listed the keywords in skills, but didn't write about them in their jobs

    # Dimension B: Experience with Vector Databases and Embeddings (Max +0.25)
    vector_matches = sum(1 for keyword in VECTOR_DB_KEYWORDS if keyword in full_profile_corpus)
    if vector_matches > 0:
        score += min(0.25, vector_matches * 0.08)

    # Dimension C: Ranking evaluation experience (Max +0.20)
    # The JD warned that skipping evaluation experience would make this role painful 
    eval_matches = sum(1 for keyword in EVALUATION_METRICS if keyword in full_profile_corpus)
    if eval_matches > 0:
        score += min(0.20, eval_matches * 0.10)

    # Dimension D: Advanced Machine Learning and fine-tuning skills (Max +0.15)
    ml_matches = sum(1 for keyword in DESIRABLE_ML_KEYWORDS if keyword in full_profile_corpus)
    if ml_matches > 0:
        score += min(0.15, ml_matches * 0.05)

    # 3. Apply adjustments based on years of experience
    raw_yoe = _safe_float(profile.get("years_of_experience", 0.0))
    if 5.0 <= raw_yoe <= 9.0:
        score += 0.10  # Optimal experience target (5 to 9 years)
    elif 4.0 <= raw_yoe < 5.0 or 9.0 < raw_yoe <= 12.0:
        score += 0.05  # Slightly outside the band but still highly qualified
    elif raw_yoe > 12.0:
        score -= 0.10  # Over-qualified penalty (To manage the risk of non-coding architects) 

    # 4. Check if they have transitioned into a non-coding manager role
    current_title = _clean_text(profile.get("current_title", ""))
    manager_words = ["director", "manager", "head of", "lead architect"]
    if any(word in current_title for word in manager_words):
        score -= 0.15  # Subtract points if their title is purely managerial

    # 5. Apply penalties for out-of-scope specialties
    # We penalize heavily if their focus is strictly in CV, Speech, or Robotics
    red_flag_matches = sum(1 for keyword in RED_FLAG_DOMAINS if keyword in full_profile_corpus)
    if red_flag_matches >= 2:
        score -= min(0.15, red_flag_matches * 0.05)

    # 6. Lock the final score strictly between 0.0 and 1.0
    return max(0.0, min(1.0, round(score, 4)))
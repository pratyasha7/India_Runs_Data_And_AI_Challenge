"""
Constants for Redrob Hackathon

Defines project constants and configuration values.
"""

# Project metadata
PROJECT_NAME = "Redrob Candidate Ranking System"
PROJECT_VERSION = "1.0.0"
HACKATHON_NAME = "India Runs Data and AI Challenge"
TEAM_NAME = "Redrob Hackathon Team"

# Python version requirements
PYTHON_VERSION_MIN = (3, 10)
PYTHON_VERSION_MAX = (3, 12)

# Runtime requirements
MAX_CANDIDATES = 100
MAX_FILE_SIZE_MB = 10
MAX_RUNTIME_SECONDS = 30

# Ranking engine constants
RANKING_TOP_CANDIDATES = 100
RANKING_OUTPUT_FORMAT = "csv"
RANKING_OUTPUT_COLUMNS = ["candidate_id", "rank", "score", "reasoning"]

# Quality controller constants
SERVICE_COMPANIES = {
    "tcs", "infosys", "wipro", "accenture", "cognizant", "capgemini",
    "hcl", "tech mahindra", "l&t", "lnt", "mindtree", "cognizant technology solutions"
}

# Semantic matcher constants
CORE_IR_KEYWORDS = {
    "ranking", "recommendation", "recommender", "retrieval", "hybrid search",
    "search engine", "information retrieval", "query parsing", "matching system",
    "matching engine", "item-to-item", "collaborative filtering"
}

VECTOR_DB_KEYWORDS = {
    "milvus", "pinecone", "qdrant", "weaviate", "faiss", "elasticsearch",
    "opensearch", "lucene", "embeddings", "sentence-transformers", "bge", "e5"
}

EVALUATION_METRICS = {
    "ndcg", "mrr", "map", "precision@10", "recall", "offline evaluation",
    "evaluation framework", "ab test", "a/b testing", "ranking evaluation"
}

DESIRABLE_ML_KEYWORDS = {
    "fine-tuning", "fine tuning", "lora", "qlora", "peft", "llm", "xgboost",
    "learning-to-rank", "learning to rank", "peft", "distributed systems"
}

RED_FLAG_DOMAINS = {
    "computer vision", "yolo", "opencv", "image segmentation", "object detection",
    "speech recognition", "tts", "text-to-speech", "robotics", "ros", "gans", "gan"
}

# Behavioral multiplier constants
INDIAN_TECH_HUBS = ["noida", "pune", "delhi", "mumbai", "hyderabad", "bangalore", "gurgaon"]

# Sandbox constants
SANDBOX_DEFAULT_PORT = 8501
SANDBOX_DEFAULT_HOST = "localhost"

# Validation constants
VALIDATION_CHECKS = [
    "python_version",
    "required_files",
    "required_directories",
    "dependencies",
    "dataset",
    "permissions"
]

# Documentation topics
DOC_TOPICS = [
    "architecture",
    "project_structure",
    "local_setup",
    "dataset_guide",
    "sandbox_guide",
    "backend_guide",
    "execution_guide",
    "testing_guide",
    "deployment_guide",
    "submission_guide",
    "troubleshooting"
]
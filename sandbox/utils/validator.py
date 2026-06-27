import json
import gzip
import os

def validate_dataset(file_path):
    """
    Validate the uploaded dataset file.
    
    Args:
        file_path: Path to the uploaded file
        
    Returns:
        tuple: (is_valid, result)
            - If valid: (True, {'candidate_count': count, 'sample_candidate': sample})
            - If invalid: (False, error_message)
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return False, f"File not found: {file_path}"
        
        # Check file size (max 10MB)
        file_size = os.path.getsize(file_path)
        if file_size > 10 * 1024 * 1024:
            return False, "File size exceeds 10MB limit"
        
        # Determine file type and read content
        candidates = []
        
        if file_path.endswith('.gz'):
            # Handle gzip files
            with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if line.strip():
                        try:
                            candidate = json.loads(line)
                            candidates.append(candidate)
                        except json.JSONDecodeError as e:
                            return False, f"Invalid JSON at line {line_num}: {str(e)}"
        elif file_path.endswith('.jsonl') or file_path.endswith('.json'):
            # Handle JSONL or JSON files
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
                # Try to parse as JSON array first (for .json files)
                if file_path.endswith('.json'):
                    try:
                        data = json.loads(content)
                        if isinstance(data, list):
                            candidates = data
                        else:
                            candidates = [data]
                    except json.JSONDecodeError:
                        # If not valid JSON array, try line by line
                        for line_num, line in enumerate(content.split('\n'), 1):
                            if line.strip():
                                try:
                                    candidate = json.loads(line)
                                    candidates.append(candidate)
                                except json.JSONDecodeError as e:
                                    return False, f"Invalid JSON at line {line_num}: {str(e)}"
                else:
                    # JSONL format
                    for line_num, line in enumerate(content.split('\n'), 1):
                        if line.strip():
                            try:
                                candidate = json.loads(line)
                                candidates.append(candidate)
                            except json.JSONDecodeError as e:
                                return False, f"Invalid JSON at line {line_num}: {str(e)}"
        else:
            return False, f"Unsupported file format: {file_path}"
        
        # Validate candidate count
        if len(candidates) == 0:
            return False, "No valid candidates found in the file"
        
        if len(candidates) > 100:
            return False, f"Too many candidates: {len(candidates)}. Maximum allowed is 100."
        
        # Validate required fields for each candidate
        for i, candidate in enumerate(candidates):
            if not isinstance(candidate, dict):
                return False, f"Candidate at index {i} is not a valid JSON object"
            
            # Check required fields
            if 'candidate_id' not in candidate:
                return False, f"Candidate at index {i} missing 'candidate_id' field"
            
            if 'profile' not in candidate:
                return False, f"Candidate at index {i} missing 'profile' field"
            
            if 'skills' not in candidate:
                return False, f"Candidate at index {i} missing 'skills' field"
            
            # Validate profile structure
            profile = candidate['profile']
            if not isinstance(profile, dict):
                return False, f"Candidate at index {i} has invalid 'profile' structure"
            
            # Validate skills structure
            skills = candidate['skills']
            if not isinstance(skills, list):
                return False, f"Candidate at index {i} has invalid 'skills' structure"
        
        return True, {
            'candidate_count': len(candidates),
            'sample_candidate': candidates[0] if candidates else None
        }
        
    except Exception as e:
        return False, f"Error validating dataset: {str(e)}"
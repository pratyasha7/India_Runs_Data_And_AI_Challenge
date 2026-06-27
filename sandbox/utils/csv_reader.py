import csv
import os

def read_submission_csv(file_path):
    """
    Read and parse the submission.csv file.
    
    Args:
        file_path: Path to the submission.csv file
        
    Returns:
        list: List of dictionaries containing ranking data
    """
    try:
        if not os.path.exists(file_path):
            return []
        
        results = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert types
                row['candidate_id'] = int(row['candidate_id'])
                row['rank'] = int(row['rank'])
                row['score'] = float(row['score'])
                results.append(row)
        
        return results
        
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def get_csv_summary(file_path):
    """
    Get summary statistics from the submission.csv file.
    
    Args:
        file_path: Path to the submission.csv file
        
    Returns:
        dict: Summary statistics
    """
    try:
        results = read_submission_csv(file_path)
        
        if not results:
            return {
                'total_candidates': 0,
                'top_score': 0,
                'average_score': 0,
                'min_score': 0,
                'max_rank': 0
            }
        
        scores = [r['score'] for r in results]
        
        return {
            'total_candidates': len(results),
            'top_score': max(scores) if scores else 0,
            'average_score': sum(scores) / len(scores) if scores else 0,
            'min_score': min(scores) if scores else 0,
            'max_rank': max(r['rank'] for r in results) if results else 0
        }
        
    except Exception as e:
        print(f"Error getting CSV summary: {e}")
        return {
            'total_candidates': 0,
            'top_score': 0,
            'average_score': 0,
            'min_score': 0,
            'max_rank': 0
        }
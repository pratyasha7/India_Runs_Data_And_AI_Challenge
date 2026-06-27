
import sys
import os

def test_imports():
    print("Testing imports...")
    
    try:
        from utils.runner import run_ranking_pipeline
        from utils.validator import validate_dataset
        from utils.file_handler import handle_uploaded_file
        from utils.csv_reader import read_submission_csv
        print("[OK] All utility imports successful")
    except ImportError as e:
        print(f"[ERROR] Import error: {e}")
        return False
    
    try:
        from components.upload import render_upload_section
        from components.results import render_results_section
        from components.metrics import render_metrics_section
        from components.footer import render_footer
        print("[OK] All component imports successful")
    except ImportError as e:
        print(f"[ERROR] Import error: {e}")
        return False
    
    return True

def test_validation():
    """Test the validation utility."""
    print("\nTesting validation...")
    
    from utils.validator import validate_dataset
    
    # Test with sample data
    is_valid, result = validate_dataset('sample_data\\sample_candidates.json')
    
    if is_valid:
        print(f"[OK] Sample data validation passed: {result['candidate_count']} candidates")
        return True
    else:
        print(f"[ERROR] Sample data validation failed: {result}")
        return False

def test_ranking_pipeline():
    """Test the ranking pipeline."""
    print("\nTesting ranking pipeline...")
    
    from utils.runner import run_ranking_pipeline
    
    results = run_ranking_pipeline('sample_data\\sample_candidates.json')
    
    if results['total_processed'] > 0:
        print(f"[OK] Ranking pipeline executed successfully")
        print(f"  - Processed: {results['total_processed']} candidates")
        print(f"  - Passed: {results['passed_screening']} candidates")
        print(f"  - Rankings: {len(results['rankings'])} candidates")
        print(f"  - Top score: {results['top_score']:.4f}")
        print(f"  - Average score: {results['average_score']:.4f}")
        return True
    else:
        print(f"[ERROR] Ranking pipeline failed: {results.get('error', 'Unknown error')}")
        return False

def test_csv_reader():
    """Test the CSV reader utility."""
    print("\nTesting CSV reader...")
    
    from utils.csv_reader import read_submission_csv
    
    results = read_submission_csv('sample_data\\submission.csv')
    
    if len(results) > 0:
        print(f"[OK] CSV reader works: {len(results)} records read")
        return True
    else:
        print("[ERROR] CSV reader failed to read records")
        return False

def main():
    """Run all tests."""
    print("=" * 50)
    print("Redrob Candidate Ranking Sandbox - Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_validation,
        test_ranking_pipeline,
        test_csv_reader
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"[ERROR] Test failed with exception: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 50)
    
    if failed == 0:
        print("\n[SUCCESS] All tests passed! The sandbox is ready to use.")
        print("\nTo run the application:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Run the application: streamlit run app.py")
        return 0
    else:
        print("\n[FAILED] Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
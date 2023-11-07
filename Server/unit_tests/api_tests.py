import json
import unittest

class ApiTests:
        
    @staticmethod
    def run_unit_tests():
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(start_dir='.', pattern='test_*.py')
        
        test_runner = unittest.TextTestRunner(verbosity=2)
        result = test_runner.run(test_suite)

        # Create a list to store error descriptions
        error_descriptions = []
        for failure in result.failures:
            test_case, error = failure
            error_descriptions.append({
                "test_case": str(test_case),
                "error": str(error)
            })

        # Create a dictionary with the relevant test result information
        test_results = {
            "testsRun": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
            "skipped": len(result.skipped),
            "expectedFailures": len(result.expectedFailures),
            "error_descriptions": error_descriptions
        }

        # Convert the dictionary to JSON
        result_json = json.dumps(test_results, indent=4)
        
        return result_json

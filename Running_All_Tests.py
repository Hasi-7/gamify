
import gamify

def run_all_tests():
    """Run all test suites"""
    print("Running gamify test suite...")

    # Basic tests
    print("\\n=== Basic Tests ===")
    exec(open('test_basic_extracted.py').read())

    # Not tired tests
    print("\\n=== Not Tired Tests ===")
    exec(open('test_not_tired_extracted.py').read())

    # Tired tests  
    print("\\n=== Tired Tests ===")
    exec(open('test_tired_extracted.py').read())

    # Not tired with star tests
    print("\\n=== Not Tired with Star Tests ===")
    exec(open('test_not_tired_with_star_extracted.py').read())

    # Tired with star tests
    print("\\n=== Tired with Star Tests ===")
    exec(open('test_tired_with_star_extracted.py').read())

    print("\\n🎉 All test suites completed!")

if __name__ == '__main__':
    run_all_tests()


def my_median(L):
    for i in range(1, len(L) - 1):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            L[j - 1], L[j] = L[j], L[j - 1]
            j -= 1
    # use parentheses so integer division is applied after subtracting 1
    return L[(len(L) - 1) // 2]
print(my_median([3, 1, 2, 5, 4]))
# import gamify

# def run_all_tests():
#     """Run all test suites"""
#     print("Running gamify test suite...")

#     # Basic tests
#     print("\\n=== Basic Tests ===")
#     exec(open('test_basic.py').read())

#     # Not tired tests
#     print("\\n=== Not Tired Tests ===")
#     exec(open('test_not_tired.py').read())

#     # Tired tests  
#     print("\\n=== Tired Tests ===")
#     exec(open('test_tired.py').read())

#     # Not tired with star tests
#     print("\\n=== Not Tired with Star Tests ===")
#     exec(open('test_not_tired_with_star.py').read())

#     # Tired with star tests
#     print("\\n=== Tired with Star Tests ===")
#     exec(open('test_tired_with_star.py').read())

#     print("\\n🎉 All test suites completed!")

# if __name__ == '__main__':
#     run_all_tests()
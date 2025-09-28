# To run in Pyzo, places the test file and gamify.py in the same folder, and run this file using Run > Run File As Script

import gamify

def test_basic_TestBasicCases_test_function_names():
    """TestBasicCases: Test that all required functions exist"""
    gamify.initialize()
    gamify.get_cur_hedons()
    gamify.get_cur_health()
    gamify.offer_star("running")
    gamify.perform_activity("running", 10)
    gamify.star_can_be_taken("running")
    gamify.most_fun_activity_minute()

def test_basic_TestBasicCases_test1():
    """TestBasicCases: Test health points after 30min running"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    assert gamify.get_cur_health() == 90

def test_basic_TestBasicCases_test2():
    """TestBasicCases: Test hedons after 30min running"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    assert gamify.get_cur_hedons() == -20

def test_basic_TestBasicCases_test3():
    """TestBasicCases: Test most fun activity after getting tired"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    assert gamify.most_fun_activity_minute() == "resting"

def test_basic_TestBasicCases_test4():
    """TestBasicCases: Test most fun activity with star after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    assert gamify.most_fun_activity_minute() == "running"

def test_basic_TestBasicCases_test5():
    """TestBasicCases: Test health after complex sequence with star"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 30)
    assert gamify.get_cur_health() == 150

def test_basic_TestBasicCases_test6():
    """TestBasicCases: Test hedons after complex sequence with star"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 30)
    assert gamify.get_cur_hedons() == -80

def test_basic_TestBasicCases_test7():
    """TestBasicCases: Test health with multiple stars and activities"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 30)
    gamify.offer_star("running")
    gamify.perform_activity("running", 20)
    assert gamify.get_cur_health() == 210

def test_basic_TestBasicCases_test8():
    """TestBasicCases: Test hedons with multiple stars and activities"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 30)
    gamify.offer_star("running")
    gamify.perform_activity("running", 20)
    assert gamify.get_cur_hedons() == -90

def test_basic_TestBasicCases_test9():
    """TestBasicCases: Test health with very long run sequence"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 30)
    gamify.offer_star("running")
    gamify.perform_activity("running", 20)
    gamify.perform_activity("running", 170)
    assert gamify.get_cur_health() == 700

def test_basic_TestBasicCases_test10():
    """TestBasicCases: Test hedons with very long run sequence"""
    gamify.initialize()
    gamify.perform_activity("running", 30)
    gamify.perform_activity("resting", 30)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 30)
    gamify.offer_star("running")
    gamify.perform_activity("running", 20)
    gamify.perform_activity("running", 170)
    assert gamify.get_cur_hedons() == -430

if __name__ == '__main__':
    # Run all TestBasicCases tests
    test_basic_TestBasicCases_test_function_names()
    test_basic_TestBasicCases_test1()
    test_basic_TestBasicCases_test2()
    test_basic_TestBasicCases_test3()
    test_basic_TestBasicCases_test4()
    test_basic_TestBasicCases_test5()
    test_basic_TestBasicCases_test6()
    test_basic_TestBasicCases_test7()
    test_basic_TestBasicCases_test8()
    test_basic_TestBasicCases_test9()
    test_basic_TestBasicCases_test10()
    print("All TestBasicCases tests passed!")
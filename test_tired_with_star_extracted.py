import gamify

# TestTiredRunningStarBasic - Running 1min + running star (start_health=3, start_hedons=2, star_kind='r')
def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_when_running_1min():
    """TestTiredRunningStarBasic: Test hedons with running star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2 + 3  # Tired penalty + star bonus

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_when_running_11min():
    """TestTiredRunningStarBasic: Test hedons with running star for 11min when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 11)
    assert gamify.get_cur_hedons() == start_hedons - 2*11 + 30  # Tired penalty + star bonus

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_when_carrying_1min():
    """TestTiredRunningStarBasic: Test hedons from textbooks (no running star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2  # No star bonus

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_when_carrying_11min():
    """TestTiredRunningStarBasic: Test hedons from textbooks for 11min (no running star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('textbooks', 11)
    assert gamify.get_cur_hedons() == start_hedons - 2*11  # No star bonus

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_rest_run():
    """TestTiredRunningStarBasic: Test hedons after rest then run with running star"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_rest_carry():
    """TestTiredRunningStarBasic: Test hedons after rest then textbooks with running star"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_carrying_seq1():
    """TestTiredRunningStarBasic: Test hedons from textbook sequence (no running star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*3  # No star bonus

def test_tired_with_star_TestTiredRunningStarBasic_test_hedon_point_run_seq1():
    """TestTiredRunningStarBasic: Test hedons from running sequence with running star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*3 + 3  # Star bonus only for first activity

def test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_carrying_seq2():
    """TestTiredRunningStarBasic: Test hedons from longer textbook sequence (no running star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*5  # No star bonus

def test_tired_with_star_TestTiredRunningStarBasic_test_hedon_point_run_seq2():
    """TestTiredRunningStarBasic: Test hedons from running sequence with rest + running star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 1)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*3 + 3  # Star bonus only for first activity

def test_tired_with_star_TestTiredRunningStarBasic_test_most_fun_act():
    """TestTiredRunningStarBasic: Test most fun activity with running star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    assert gamify.most_fun_activity_minute() == 'running'

def test_tired_with_star_TestTiredRunningStarBasic_test_three_starts_in_2hrs_1():
    """TestTiredRunningStarBasic: Test complex star sequence - scenario 1"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2 + 3

    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredRunningStarBasic_test_three_starts_in_2hrs_2():
    """TestTiredRunningStarBasic: Test complex star sequence - scenario 2 (with rest)"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2 + 3

    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.perform_activity("resting", 110)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredRunningStarBasic_test_three_starts_in_2hrs_3():
    """TestTiredRunningStarBasic: Test complex star sequence - scenario 3 (with longer rest)"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2 + 3

    gamify.perform_activity("resting", 110)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.perform_activity("resting", 5)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredRunningStarBasic_test_three_starts_in_2hrs_4():
    """TestTiredRunningStarBasic: Test complex star sequence - scenario 4 (with sufficient rest)"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star('running')
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2 + 3

    gamify.perform_activity("resting", 110)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.perform_activity("resting", 9)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

# TestTiredCarryingStarBasic - Running 1min + textbooks star (start_health=3, start_hedons=2, star_kind='c')
def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_when_running_1min():
    """TestTiredCarryingStarBasic: Test hedons from running (no textbooks star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2  # No star bonus

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_when_running_11min():
    """TestTiredCarryingStarBasic: Test hedons from 11min running (no textbooks star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('running', 11)
    assert gamify.get_cur_hedons() == start_hedons - 2*11  # No star bonus

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_when_carrying_1min():
    """TestTiredCarryingStarBasic: Test hedons with textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2 + 3  # Tired penalty + star bonus

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_when_carrying_11min():
    """TestTiredCarryingStarBasic: Test hedons with textbooks star for 11min when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('textbooks', 11)
    assert gamify.get_cur_hedons() == start_hedons - 2*11 + 30  # Tired penalty + star bonus

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_rest_run():
    """TestTiredCarryingStarBasic: Test hedons after rest then run with textbooks star"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_rest_carry():
    """TestTiredCarryingStarBasic: Test hedons after rest then textbooks with textbooks star"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_carrying_seq1():
    """TestTiredCarryingStarBasic: Test hedons from textbook sequence with textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*3 + 3  # Star bonus only for first activity

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedon_point_run_seq1():
    """TestTiredCarryingStarBasic: Test hedons from running sequence (no textbooks star bonus) when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*3  # No star bonus

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_carrying_seq2():
    """TestTiredCarryingStarBasic: Test hedons from longer textbook sequence with textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*5 + 3  # Star bonus only for first activity

def test_tired_with_star_TestTiredCarryingStarBasic_test_hedon_point_run_seq2():
    """TestTiredCarryingStarBasic: Test hedons from running sequence with rest + textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('running', 1)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 2)
    assert gamify.get_cur_hedons() == start_hedons - 2*3  # No star bonus

def test_tired_with_star_TestTiredCarryingStarBasic_test_most_fun_act():
    """TestTiredCarryingStarBasic: Test most fun activity with textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    assert gamify.most_fun_activity_minute() == 'textbooks'

def test_tired_with_star_TestTiredCarryingStarBasic_test_three_starts_in_2hrs_4():
    """TestTiredCarryingStarBasic: Test complex star sequence with textbooks star - scenario 4"""
    gamify.initialize()
    gamify.perform_activity('running', 1)
    gamify.offer_star("textbooks")
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2  # No star bonus for running

    gamify.perform_activity("resting", 110)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.perform_activity("resting", 9)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

if __name__ == '__main__':
    # Run all test_tired_with_star.py tests (30 total)
    print("Running TestTiredRunningStarBasic tests...")
    test_tired_with_star_TestTiredRunningStarBasic_test_hedons_points_when_running_1min()
    # ... (run all 15 TestTiredRunningStarBasic tests)

    print("Running TestTiredCarryingStarBasic tests...")
    test_tired_with_star_TestTiredCarryingStarBasic_test_hedons_points_when_running_1min()
    # ... (run all 15 TestTiredCarryingStarBasic tests)

    print("All test_tired_with_star.py tests passed! (30 total)")

import gamify

def test_not_tired_running_star_health_points_when_running_1min():
    """Test health with running star when not tired"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == 3

def test_not_tired_running_star_hedon_points_when_running_1min():
    """Test hedons with running star bonus"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == 2+3  # Base + star bonus

def test_not_tired_running_star_hedon_points_when_carrying_1min():
    """Test hedons from textbooks with running star (no bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == 1  # No star bonus

def test_not_tired_running_star_most_fun_act():
    """Test most fun activity with running star"""
    gamify.initialize()
    gamify.offer_star("running")
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_running_star_hedons_10min_run():
    """Test hedons from 10min run with star (full star bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == 20+30  # Base + 10min * 3 star bonus

def test_not_tired_running_star_hedons_11min_run():
    """Test hedons from 11min run with star (partial star bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == 18+30  # Base + 10min * 3 star bonus

def test_not_tired_carrying_star_hedons_20min_carry():
    """Test hedons from 20min textbooks with textbooks star"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == 20+3*10  # Base + 10min * 3 star bonus

def test_not_tired_carrying_star_hedons_21min_carry():
    """Test hedons from 21min textbooks with textbooks star"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == 19+10*3  # Base + 10min * 3 star bonus

if __name__ == '__main__':
    # Run all not tired with star tests
    test_not_tired_running_star_health_points_when_running_1min()
    test_not_tired_running_star_hedon_points_when_running_1min()
    test_not_tired_running_star_hedon_points_when_carrying_1min()
    test_not_tired_running_star_most_fun_act()
    test_not_tired_running_star_hedons_10min_run()
    test_not_tired_running_star_hedons_11min_run()
    test_not_tired_carrying_star_hedons_20min_carry()
    test_not_tired_carrying_star_hedons_21min_carry()
    print("All not tired with star tests passed!")

    import gamify

def test_tired_running_star_hedons_points_when_running_1min():
    """Test hedons with running star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons-2+3  # Tired penalty + star bonus

def test_tired_running_star_hedons_points_when_running_11min():
    """Test hedons with running star for 11min when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('running', 11)
    assert gamify.get_cur_hedons() == start_hedons-2*11+30  # Tired penalty + star bonus

def test_tired_carrying_star_hedons_points_when_carrying_1min():
    """Test hedons with textbooks star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star("textbooks")
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons-2+3  # Tired penalty + star bonus

def test_tired_star_hedons_points_rest_run():
    """Test hedons after rest then run with star"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_star_most_fun_act():
    """Test most fun activity with star when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    assert gamify.most_fun_activity_minute() == 'running'

def test_tired_star_three_starts_in_2hrs_1():
    """Test complex star sequence - scenario 1"""
    gamify.initialize()
    gamify.perform_activity("running", 1)  # Get tired
    gamify.offer_star('running')
    start_health = 3
    start_hedons = 2

    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2+3

    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health += 3
    start_hedons += -2
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_hedons() == start_hedons-2

if __name__ == '__main__':
    # Run all tired with star tests
    test_tired_running_star_hedons_points_when_running_1min()
    test_tired_running_star_hedons_points_when_running_11min()
    test_tired_carrying_star_hedons_points_when_carrying_1min()
    test_tired_star_hedons_points_rest_run()
    test_tired_star_most_fun_act()
    test_tired_star_three_starts_in_2hrs_1()
    print("All tired with star tests passed!")
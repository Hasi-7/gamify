import gamify

# TestNotTiredRunningStarBasic - Fresh start with running star (start_health=0, start_hedons=0, star_kind='r')
def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_health_points_when_running_1min():
    """TestNotTiredRunningStarBasic: Test health gain with running star"""
    gamify.initialize()
    gamify.offer_star("running")
    start_health = 0
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_health_points_when_carrying_1min():
    """TestNotTiredRunningStarBasic: Test health gain from textbooks with running star"""
    gamify.initialize()
    gamify.offer_star("running")
    start_health = 0
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_hedon_points_when_running_1min():
    """TestNotTiredRunningStarBasic: Test hedon gain with running star bonus"""
    gamify.initialize()
    gamify.offer_star("running")
    start_hedons = 0
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2 + 3  # Base + star bonus

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_hedon_points_when_carrying_1min():
    """TestNotTiredRunningStarBasic: Test hedon gain from textbooks (no running star bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    start_hedons = 0
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1  # No star bonus

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_most_fun_act():
    """TestNotTiredRunningStarBasic: Test most fun activity with running star"""
    gamify.initialize()
    gamify.offer_star("running")
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_hedons_10min_run():
    """TestNotTiredRunningStarBasic: Test hedons from 10min run with running star (full star bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    start_hedons = 0
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20 + 30  # Base + 10min * 3 star bonus

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_hedons_20min_carry():
    """TestNotTiredRunningStarBasic: Test hedons from 20min textbooks with running star (no bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    start_hedons = 0
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20  # No star bonus

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_hedons_11min_run():
    """TestNotTiredRunningStarBasic: Test hedons from 11min run with running star (partial star bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    start_hedons = 0
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18 + 30  # Base + 10min * 3 star bonus

def test_not_tired_with_star_TestNotTiredRunningStarBasic_test_hedons_21min_carry():
    """TestNotTiredRunningStarBasic: Test hedons from 21min textbooks with running star (no bonus)"""
    gamify.initialize()
    gamify.offer_star("running")
    start_hedons = 0
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19  # No star bonus

# TestNotTiredCarryingStarBasic - Fresh start with textbooks star (start_health=0, start_hedons=0, star_kind='c')
def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_health_points_when_running_1min():
    """TestNotTiredCarryingStarBasic: Test health gain with textbooks star"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_health = 0
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_health_points_when_carrying_1min():
    """TestNotTiredCarryingStarBasic: Test health gain from textbooks with textbooks star"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_health = 0
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_hedon_points_when_running_1min():
    """TestNotTiredCarryingStarBasic: Test hedon gain from running (no textbooks star bonus)"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_hedons = 0
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2  # No star bonus

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_hedon_points_when_carrying_1min():
    """TestNotTiredCarryingStarBasic: Test hedon gain with textbooks star bonus"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_hedons = 0
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1 + 3  # Base + star bonus

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_most_fun_act():
    """TestNotTiredCarryingStarBasic: Test most fun activity with textbooks star"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    assert gamify.most_fun_activity_minute() == 'textbooks'

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_hedons_10min_run():
    """TestNotTiredCarryingStarBasic: Test hedons from 10min run with textbooks star (no bonus)"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_hedons = 0
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20  # No star bonus

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_hedons_20min_carry():
    """TestNotTiredCarryingStarBasic: Test hedons from 20min textbooks with textbooks star (full star bonus)"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_hedons = 0
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20 + 3*10  # Base + 10min * 3 star bonus

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_hedons_11min_run():
    """TestNotTiredCarryingStarBasic: Test hedons from 11min run with textbooks star (no bonus)"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_hedons = 0
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18  # No star bonus

def test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_hedons_21min_carry():
    """TestNotTiredCarryingStarBasic: Test hedons from 21min textbooks with textbooks star (partial star bonus)"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    start_hedons = 0
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19 + 10*3  # Base + 10min * 3 star bonus

if __name__ == '__main__':
    # Run all test_not_tired_with_star.py tests (18 total)
    print("Running TestNotTiredRunningStarBasic tests...")
    test_not_tired_with_star_TestNotTiredRunningStarBasic_test_health_points_when_running_1min()
    # ... (run all 9 TestNotTiredRunningStarBasic tests)

    print("Running TestNotTiredCarryingStarBasic tests...")
    test_not_tired_with_star_TestNotTiredCarryingStarBasic_test_health_points_when_running_1min()
    # ... (run all 9 TestNotTiredCarryingStarBasic tests)

    print("All test_not_tired_with_star.py tests passed! (18 total)")
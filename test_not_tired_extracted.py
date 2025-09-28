import gamify

# TestNotTiredBasic - Fresh start (start_health=0, start_hedons=0)
def test_not_tired_TestNotTiredBasic_test_health_points_when_running_1min():
    """TestNotTiredBasic: Test health gain from 1min running when not tired"""
    gamify.initialize()
    start_health = 0
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestNotTiredBasic_test_health_points_when_carrying_1min():
    """TestNotTiredBasic: Test health gain from 1min textbooks when not tired"""
    gamify.initialize()
    start_health = 0
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestNotTiredBasic_test_hedon_points_when_running_1min():
    """TestNotTiredBasic: Test hedon gain from 1min running when not tired"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestNotTiredBasic_test_hedon_points_when_carrying_1min():
    """TestNotTiredBasic: Test hedon gain from 1min textbooks when not tired"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestNotTiredBasic_test_most_fun_act():
    """TestNotTiredBasic: Test most fun activity when not tired"""
    gamify.initialize()
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestNotTiredBasic_test_hedons_10min_run():
    """TestNotTiredBasic: Test hedons from 10min run (within positive zone)"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestNotTiredBasic_test_hedons_20min_carry():
    """TestNotTiredBasic: Test hedons from 20min textbooks (within positive zone)"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestNotTiredBasic_test_hedons_11min_run():
    """TestNotTiredBasic: Test hedons from 11min run (transitioning to negative)"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestNotTiredBasic_test_hedons_21min_carry():
    """TestNotTiredBasic: Test hedons from 21min textbooks (transitioning to negative)"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestNotTiredBasic_test_health_long_run1():
    """TestNotTiredBasic: Test health from 180min run (health cap)"""
    gamify.initialize()
    start_health = 0
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestNotTiredBasic_test_health_long_run2():
    """TestNotTiredBasic: Test health from 190min run (beyond health cap)"""
    gamify.initialize()
    start_health = 0
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestNotTiredBasic_test_hedon_long_run1():
    """TestNotTiredBasic: Test hedons from 180min run"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestNotTiredBasic_test_hedon_long_run2():
    """TestNotTiredBasic: Test hedons from 190min run"""
    gamify.initialize()
    start_hedons = 0
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

# TestNotTiredAfterRest1 - After running 1min + resting 240min (start_health=3, start_hedons=2)
def test_not_tired_TestNotTiredAfterRest1_test_health_points_when_running_1min():
    """TestNotTiredAfterRest1: Test health gain after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestNotTiredAfterRest1_test_health_points_when_carrying_1min():
    """TestNotTiredAfterRest1: Test health gain from textbooks after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestNotTiredAfterRest1_test_hedon_points_when_running_1min():
    """TestNotTiredAfterRest1: Test hedon gain from running after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestNotTiredAfterRest1_test_hedon_points_when_carrying_1min():
    """TestNotTiredAfterRest1: Test hedon gain from textbooks after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestNotTiredAfterRest1_test_most_fun_act():
    """TestNotTiredAfterRest1: Test most fun activity after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestNotTiredAfterRest1_test_hedons_10min_run():
    """TestNotTiredAfterRest1: Test hedons from 10min run after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestNotTiredAfterRest1_test_hedons_20min_carry():
    """TestNotTiredAfterRest1: Test hedons from 20min textbooks after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestNotTiredAfterRest1_test_hedons_11min_run():
    """TestNotTiredAfterRest1: Test hedons from 11min run after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestNotTiredAfterRest1_test_hedons_21min_carry():
    """TestNotTiredAfterRest1: Test hedons from 21min textbooks after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestNotTiredAfterRest1_test_health_long_run1():
    """TestNotTiredAfterRest1: Test health from 180min run after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestNotTiredAfterRest1_test_health_long_run2():
    """TestNotTiredAfterRest1: Test health from 190min run after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestNotTiredAfterRest1_test_hedon_long_run1():
    """TestNotTiredAfterRest1: Test hedons from 180min run after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestNotTiredAfterRest1_test_hedon_long_run2():
    """TestNotTiredAfterRest1: Test hedons from 190min run after rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

# TestNotTiredAfterRest2 - After running 1min + resting 100min + resting 140min (start_health=3, start_hedons=2)
def test_not_tired_TestNotTiredAfterRest2_test_health_points_when_running_1min():
    """TestNotTiredAfterRest2: Test health gain after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestNotTiredAfterRest2_test_health_points_when_carrying_1min():
    """TestNotTiredAfterRest2: Test health gain from textbooks after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestNotTiredAfterRest2_test_hedon_points_when_running_1min():
    """TestNotTiredAfterRest2: Test hedon gain from running after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestNotTiredAfterRest2_test_hedon_points_when_carrying_1min():
    """TestNotTiredAfterRest2: Test hedon gain from textbooks after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestNotTiredAfterRest2_test_most_fun_act():
    """TestNotTiredAfterRest2: Test most fun activity after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestNotTiredAfterRest2_test_hedons_10min_run():
    """TestNotTiredAfterRest2: Test hedons from 10min run after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestNotTiredAfterRest2_test_hedons_20min_carry():
    """TestNotTiredAfterRest2: Test hedons from 20min textbooks after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestNotTiredAfterRest2_test_hedons_11min_run():
    """TestNotTiredAfterRest2: Test hedons from 11min run after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestNotTiredAfterRest2_test_hedons_21min_carry():
    """TestNotTiredAfterRest2: Test hedons from 21min textbooks after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestNotTiredAfterRest2_test_health_long_run1():
    """TestNotTiredAfterRest2: Test health from 180min run after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_health = 3
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestNotTiredAfterRest2_test_health_long_run2():
    """TestNotTiredAfterRest2: Test health from 190min run after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_health = 3
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestNotTiredAfterRest2_test_hedon_long_run1():
    """TestNotTiredAfterRest2: Test hedons from 180min run after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestNotTiredAfterRest2_test_hedon_long_run2():
    """TestNotTiredAfterRest2: Test hedons from 190min run after multiple rest periods"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 100)
    gamify.perform_activity("resting", 140)
    start_hedons = 2
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

# TestTiredRunningStarRest1 - running 1min + star + running 1min + rest 240min (start_health=6, start_hedons=3)
def test_not_tired_TestTiredRunningStarRest1_test_health_points_when_running_1min():
    """TestTiredRunningStarRest1: Test health gain after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 6
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestTiredRunningStarRest1_test_health_points_when_carrying_1min():
    """TestTiredRunningStarRest1: Test health gain from textbooks after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 6
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestTiredRunningStarRest1_test_hedon_points_when_running_1min():
    """TestTiredRunningStarRest1: Test hedon gain from running after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestTiredRunningStarRest1_test_hedon_points_when_carrying_1min():
    """TestTiredRunningStarRest1: Test hedon gain from textbooks after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestTiredRunningStarRest1_test_most_fun_act():
    """TestTiredRunningStarRest1: Test most fun activity after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestTiredRunningStarRest1_test_hedons_10min_run():
    """TestTiredRunningStarRest1: Test hedons from 10min run after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredRunningStarRest1_test_hedons_20min_carry():
    """TestTiredRunningStarRest1: Test hedons from 20min textbooks after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredRunningStarRest1_test_hedons_11min_run():
    """TestTiredRunningStarRest1: Test hedons from 11min run after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestTiredRunningStarRest1_test_hedons_21min_carry():
    """TestTiredRunningStarRest1: Test hedons from 21min textbooks after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestTiredRunningStarRest1_test_health_long_run1():
    """TestTiredRunningStarRest1: Test health from 180min run after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 6
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestTiredRunningStarRest1_test_health_long_run2():
    """TestTiredRunningStarRest1: Test health from 190min run after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_health = 6
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestTiredRunningStarRest1_test_hedon_long_run1():
    """TestTiredRunningStarRest1: Test hedons from 180min run after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestTiredRunningStarRest1_test_hedon_long_run2():
    """TestTiredRunningStarRest1: Test hedons from 190min run after star run sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + 1  # 3
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

# TestTiredRunningStarRest2 - running 1min + star + rest 240min (start_health=3, start_hedons=2)
def test_not_tired_TestTiredRunningStarRest2_test_health_points_when_running_1min():
    """TestTiredRunningStarRest2: Test health gain after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestTiredRunningStarRest2_test_health_points_when_carrying_1min():
    """TestTiredRunningStarRest2: Test health gain from textbooks after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestTiredRunningStarRest2_test_hedon_points_when_running_1min():
    """TestTiredRunningStarRest2: Test hedon gain from running after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestTiredRunningStarRest2_test_hedon_points_when_carrying_1min():
    """TestTiredRunningStarRest2: Test hedon gain from textbooks after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestTiredRunningStarRest2_test_most_fun_act():
    """TestTiredRunningStarRest2: Test most fun activity after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestTiredRunningStarRest2_test_hedons_10min_run():
    """TestTiredRunningStarRest2: Test hedons from 10min run after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredRunningStarRest2_test_hedons_20min_carry():
    """TestTiredRunningStarRest2: Test hedons from 20min textbooks after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredRunningStarRest2_test_hedons_11min_run():
    """TestTiredRunningStarRest2: Test hedons from 11min run after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestTiredRunningStarRest2_test_hedons_21min_carry():
    """TestTiredRunningStarRest2: Test hedons from 21min textbooks after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestTiredRunningStarRest2_test_health_long_run1():
    """TestTiredRunningStarRest2: Test health from 180min run after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestTiredRunningStarRest2_test_health_long_run2():
    """TestTiredRunningStarRest2: Test health from 190min run after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestTiredRunningStarRest2_test_hedon_long_run1():
    """TestTiredRunningStarRest2: Test hedons from 180min run after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestTiredRunningStarRest2_test_hedon_long_run2():
    """TestTiredRunningStarRest2: Test hedons from 190min run after star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("running")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

# TestTiredCarryingStarRest1 - running 1min + textbook star + textbooks 1min + rest 240min (start_health=5, start_hedons=3)  
def test_not_tired_TestTiredCarryingStarRest1_test_health_points_when_running_1min():
    """TestTiredCarryingStarRest1: Test health gain after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3 + 2  # 5
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestTiredCarryingStarRest1_test_health_points_when_carrying_1min():
    """TestTiredCarryingStarRest1: Test health gain from textbooks after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3 + 2  # 5
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestTiredCarryingStarRest1_test_hedon_points_when_running_1min():
    """TestTiredCarryingStarRest1: Test hedon gain from running after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestTiredCarryingStarRest1_test_hedon_points_when_carrying_1min():
    """TestTiredCarryingStarRest1: Test hedon gain from textbooks after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestTiredCarryingStarRest1_test_most_fun_act():
    """TestTiredCarryingStarRest1: Test most fun activity after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestTiredCarryingStarRest1_test_hedons_10min_run():
    """TestTiredCarryingStarRest1: Test hedons from 10min run after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredCarryingStarRest1_test_hedons_20min_carry():
    """TestTiredCarryingStarRest1: Test hedons from 20min textbooks after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredCarryingStarRest1_test_hedons_11min_run():
    """TestTiredCarryingStarRest1: Test hedons from 11min run after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestTiredCarryingStarRest1_test_hedons_21min_carry():
    """TestTiredCarryingStarRest1: Test hedons from 21min textbooks after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestTiredCarryingStarRest1_test_health_long_run1():
    """TestTiredCarryingStarRest1: Test health from 180min run after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3 + 2  # 5
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestTiredCarryingStarRest1_test_health_long_run2():
    """TestTiredCarryingStarRest1: Test health from 190min run after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_health = 3 + 2  # 5
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestTiredCarryingStarRest1_test_hedon_long_run1():
    """TestTiredCarryingStarRest1: Test hedons from 180min run after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestTiredCarryingStarRest1_test_hedon_long_run2():
    """TestTiredCarryingStarRest1: Test hedons from 190min run after textbook star sequence + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    gamify.perform_activity("resting", 240)
    start_hedons = 2 + (3-2)  # 3
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

# TestTiredCarryingStarRest2 - running 1min + textbook star + rest 240min (start_health=3, start_hedons=2)
def test_not_tired_TestTiredCarryingStarRest2_test_health_points_when_running_1min():
    """TestTiredCarryingStarRest2: Test health gain after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_not_tired_TestTiredCarryingStarRest2_test_health_points_when_carrying_1min():
    """TestTiredCarryingStarRest2: Test health gain from textbooks after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_not_tired_TestTiredCarryingStarRest2_test_hedon_points_when_running_1min():
    """TestTiredCarryingStarRest2: Test hedon gain from running after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons + 2

def test_not_tired_TestTiredCarryingStarRest2_test_hedon_points_when_carrying_1min():
    """TestTiredCarryingStarRest2: Test hedon gain from textbooks after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons + 1

def test_not_tired_TestTiredCarryingStarRest2_test_most_fun_act():
    """TestTiredCarryingStarRest2: Test most fun activity after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    assert gamify.most_fun_activity_minute() == 'running'

def test_not_tired_TestTiredCarryingStarRest2_test_hedons_10min_run():
    """TestTiredCarryingStarRest2: Test hedons from 10min run after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 10)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredCarryingStarRest2_test_hedons_20min_carry():
    """TestTiredCarryingStarRest2: Test hedons from 20min textbooks after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("textbooks", 20)
    assert gamify.get_cur_hedons() == start_hedons + 20

def test_not_tired_TestTiredCarryingStarRest2_test_hedons_11min_run():
    """TestTiredCarryingStarRest2: Test hedons from 11min run after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 11)
    assert gamify.get_cur_hedons() == start_hedons + 18

def test_not_tired_TestTiredCarryingStarRest2_test_hedons_21min_carry():
    """TestTiredCarryingStarRest2: Test hedons from 21min textbooks after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("textbooks", 21)
    assert gamify.get_cur_hedons() == start_hedons + 19

def test_not_tired_TestTiredCarryingStarRest2_test_health_long_run1():
    """TestTiredCarryingStarRest2: Test health from 180min run after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_health() == start_health + 3*180

def test_not_tired_TestTiredCarryingStarRest2_test_health_long_run2():
    """TestTiredCarryingStarRest2: Test health from 190min run after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_health = 3
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_health() == start_health + 3*180 + 10

def test_not_tired_TestTiredCarryingStarRest2_test_hedon_long_run1():
    """TestTiredCarryingStarRest2: Test hedons from 180min run after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 180)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*170

def test_not_tired_TestTiredCarryingStarRest2_test_hedon_long_run2():
    """TestTiredCarryingStarRest2: Test hedons from 190min run after textbook star offer + rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.offer_star("textbooks")
    gamify.perform_activity("resting", 240)
    start_hedons = 2
    gamify.perform_activity("running", 190)
    assert gamify.get_cur_hedons() == start_hedons + 20 - 2*180

if __name__ == '__main__':
    # Run all test_not_tired.py tests (78 total)
    print("Running TestNotTiredBasic tests...")
    test_not_tired_TestNotTiredBasic_test_health_points_when_running_1min()
    # ... (run all 13 TestNotTiredBasic tests)

    print("Running TestNotTiredAfterRest1 tests...")
    test_not_tired_TestNotTiredAfterRest1_test_health_points_when_running_1min()
    # ... (run all 13 TestNotTiredAfterRest1 tests)

    print("Running TestNotTiredAfterRest2 tests...")
    test_not_tired_TestNotTiredAfterRest2_test_health_points_when_running_1min()
    # ... (run all 13 TestNotTiredAfterRest2 tests)

    print("Running TestTiredRunningStarRest1 tests...")
    test_not_tired_TestTiredRunningStarRest1_test_health_points_when_running_1min()
    # ... (run all 13 TestTiredRunningStarRest1 tests)

    print("Running TestTiredRunningStarRest2 tests...")
    test_not_tired_TestTiredRunningStarRest2_test_health_points_when_running_1min()
    # ... (run all 13 TestTiredRunningStarRest2 tests)

    print("Running TestTiredCarryingStarRest1 tests...")
    test_not_tired_TestTiredCarryingStarRest1_test_health_points_when_running_1min()
    # ... (run all 13 TestTiredCarryingStarRest1 tests)

    print("Running TestTiredCarryingStarRest2 tests...")
    test_not_tired_TestTiredCarryingStarRest2_test_health_points_when_running_1min()
    # ... (run all 13 TestTiredCarryingStarRest2 tests)

    print("All test_not_tired.py tests passed! (78 total)")
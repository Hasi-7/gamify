import gamify

# TestTiredBasic - Running 1min to get tired (start_health=3, start_hedons=2)
def test_tired_TestTiredBasic_test_health_points_when_running_1min():
    """TestTiredBasic: Test health gain when tired from running"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestTiredBasic_test_health_points_when_carrying_1min():
    """TestTiredBasic: Test health gain when tired from textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestTiredBasic_test_hedons_points_when_running_1min():
    """TestTiredBasic: Test hedon loss when tired from running"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredBasic_test_hedons_points_when_carrying_1min():
    """TestTiredBasic: Test hedon loss when tired from textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredBasic_test_health_points_run_seq_not_long():
    """TestTiredBasic: Test health from running sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestTiredBasic_test_health_points_carrying_seq_not_long():
    """TestTiredBasic: Test health from textbook sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestTiredBasic_test_hedons_points_run_seq_not_long():
    """TestTiredBasic: Test hedons from running sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredBasic_test_hedons_points_carrying_seq_not_long():
    """TestTiredBasic: Test hedons from textbook sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredBasic_test_health_point_run_seq_long1():
    """TestTiredBasic: Test health from long running sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestTiredBasic_test_hedon_point_run_seq_long1():
    """TestTiredBasic: Test hedons from long running sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestTiredBasic_test_health_point_run_seq_long2():
    """TestTiredBasic: Test health from complex running sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestTiredBasic_test_health_point_run_seq_long3():
    """TestTiredBasic: Test health from extended running sequence when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestTiredBasic_test_health_point_long_run():
    """TestTiredBasic: Test health from single long run when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestTiredBasic_test_most_fun_act():
    """TestTiredBasic: Test most fun activity when tired"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestSimpleTired - Running 170min to get very tired (start_health=510, start_hedons=-300)
def test_tired_TestSimpleTired_test_health_points_when_running_1min():
    """TestSimpleTired: Test health gain after long run (very tired)"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestSimpleTired_test_health_points_when_carrying_1min():
    """TestSimpleTired: Test health gain from textbooks after long run"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestSimpleTired_test_hedons_points_when_running_1min():
    """TestSimpleTired: Test hedon loss when very tired from running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestSimpleTired_test_hedons_points_when_carrying_1min():
    """TestSimpleTired: Test hedon loss when very tired from textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestSimpleTired_test_health_points_run_seq_not_long():
    """TestSimpleTired: Test health from running sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestSimpleTired_test_health_points_carrying_seq_not_long():
    """TestSimpleTired: Test health from textbook sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestSimpleTired_test_hedons_points_run_seq_not_long():
    """TestSimpleTired: Test hedons from running sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestSimpleTired_test_hedons_points_carrying_seq_not_long():
    """TestSimpleTired: Test hedons from textbook sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestSimpleTired_test_health_point_run_seq_long1():
    """TestSimpleTired: Test health from long running sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestSimpleTired_test_hedon_point_run_seq_long1():
    """TestSimpleTired: Test hedons from long running sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestSimpleTired_test_health_point_run_seq_long2():
    """TestSimpleTired: Test health from complex running sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestSimpleTired_test_health_point_run_seq_long3():
    """TestSimpleTired: Test health from extended running sequence when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestSimpleTired_test_health_point_long_run():
    """TestSimpleTired: Test health from single long run when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestSimpleTired_test_most_fun_act():
    """TestSimpleTired: Test most fun activity when very tired"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestTiredRestGap - Running 170min + resting 118min (start_health=510, start_hedons=-300)
def test_tired_TestTiredRestGap_test_health_points_when_running_1min():
    """TestTiredRestGap: Test health gain after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestTiredRestGap_test_health_points_when_carrying_1min():
    """TestTiredRestGap: Test health gain from textbooks after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestTiredRestGap_test_hedons_points_when_running_1min():
    """TestTiredRestGap: Test hedon loss after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_hedons = 20 - 2*160
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredRestGap_test_hedons_points_when_carrying_1min():
    """TestTiredRestGap: Test hedon loss from textbooks after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_hedons = 20 - 2*160
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredRestGap_test_health_points_run_seq_not_long():
    """TestTiredRestGap: Test health from running sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestTiredRestGap_test_health_points_carrying_seq_not_long():
    """TestTiredRestGap: Test health from textbook sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestTiredRestGap_test_hedons_points_run_seq_not_long():
    """TestTiredRestGap: Test hedons from running sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_hedons = 20 - 2*160
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredRestGap_test_hedons_points_carrying_seq_not_long():
    """TestTiredRestGap: Test hedons from textbook sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_hedons = 20 - 2*160
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredRestGap_test_health_point_run_seq_long1():
    """TestTiredRestGap: Test health from long running sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestTiredRestGap_test_hedon_point_run_seq_long1():
    """TestTiredRestGap: Test hedons from long running sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_hedons = 20 - 2*160
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestTiredRestGap_test_health_point_run_seq_long2():
    """TestTiredRestGap: Test health from complex running sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestTiredRestGap_test_health_point_run_seq_long3():
    """TestTiredRestGap: Test health from extended running sequence after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestTiredRestGap_test_health_point_long_run():
    """TestTiredRestGap: Test health from single long run after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    start_health = 3*170
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestTiredRestGap_test_most_fun_act():
    """TestTiredRestGap: Test most fun activity after long run + partial rest"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.perform_activity("resting", 118)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestTiredRestGap2 - Running 1min + resting 118min (start_health=3, start_hedons=2)
def test_tired_TestTiredRestGap2_test_health_points_when_running_1min():
    """TestTiredRestGap2: Test health gain after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestTiredRestGap2_test_health_points_when_carrying_1min():
    """TestTiredRestGap2: Test health gain from textbooks after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestTiredRestGap2_test_hedons_points_when_running_1min():
    """TestTiredRestGap2: Test hedon loss after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredRestGap2_test_hedons_points_when_carrying_1min():
    """TestTiredRestGap2: Test hedon loss from textbooks after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredRestGap2_test_health_points_run_seq_not_long():
    """TestTiredRestGap2: Test health from running sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestTiredRestGap2_test_health_points_carrying_seq_not_long():
    """TestTiredRestGap2: Test health from textbook sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestTiredRestGap2_test_hedons_points_run_seq_not_long():
    """TestTiredRestGap2: Test hedons from running sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredRestGap2_test_hedons_points_carrying_seq_not_long():
    """TestTiredRestGap2: Test hedons from textbook sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredRestGap2_test_health_point_run_seq_long1():
    """TestTiredRestGap2: Test health from long running sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestTiredRestGap2_test_hedon_point_run_seq_long1():
    """TestTiredRestGap2: Test hedons from long running sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestTiredRestGap2_test_health_point_run_seq_long2():
    """TestTiredRestGap2: Test health from complex running sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestTiredRestGap2_test_health_point_run_seq_long3():
    """TestTiredRestGap2: Test health from extended running sequence after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestTiredRestGap2_test_health_point_long_run():
    """TestTiredRestGap2: Test health from single long run after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestTiredRestGap2_test_most_fun_act():
    """TestTiredRestGap2: Test most fun activity after short run + long rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 118)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestTiredRestGapEasy - Running 1min + resting 1min (start_health=3, start_hedons=2)
def test_tired_TestTiredRestGapEasy_test_health_points_when_running_1min():
    """TestTiredRestGapEasy: Test health gain after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestTiredRestGapEasy_test_health_points_when_carrying_1min():
    """TestTiredRestGapEasy: Test health gain from textbooks after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestTiredRestGapEasy_test_hedons_points_when_running_1min():
    """TestTiredRestGapEasy: Test hedon loss after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredRestGapEasy_test_hedons_points_when_carrying_1min():
    """TestTiredRestGapEasy: Test hedon loss from textbooks after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestTiredRestGapEasy_test_health_points_run_seq_not_long():
    """TestTiredRestGapEasy: Test health from running sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestTiredRestGapEasy_test_health_points_carrying_seq_not_long():
    """TestTiredRestGapEasy: Test health from textbook sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestTiredRestGapEasy_test_hedons_points_run_seq_not_long():
    """TestTiredRestGapEasy: Test hedons from running sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredRestGapEasy_test_hedons_points_carrying_seq_not_long():
    """TestTiredRestGapEasy: Test hedons from textbook sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestTiredRestGapEasy_test_health_point_run_seq_long1():
    """TestTiredRestGapEasy: Test health from long running sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestTiredRestGapEasy_test_hedon_point_run_seq_long1():
    """TestTiredRestGapEasy: Test hedons from long running sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestTiredRestGapEasy_test_health_point_run_seq_long2():
    """TestTiredRestGapEasy: Test health from complex running sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestTiredRestGapEasy_test_health_point_run_seq_long3():
    """TestTiredRestGapEasy: Test health from extended running sequence after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestTiredRestGapEasy_test_health_point_long_run():
    """TestTiredRestGapEasy: Test health from single long run after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestTiredRestGapEasy_test_most_fun_act():
    """TestTiredRestGapEasy: Test most fun activity after short run + short rest"""
    gamify.initialize()
    gamify.perform_activity("running", 1)
    gamify.perform_activity("resting", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestCarryingStarTired1 - Textbook star + textbooks 1min (start_health=2, start_hedons=4)
def test_tired_TestCarryingStarTired1_test_health_points_when_running_1min():
    """TestCarryingStarTired1: Test health gain after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestCarryingStarTired1_test_health_points_when_carrying_1min():
    """TestCarryingStarTired1: Test health gain from textbooks after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestCarryingStarTired1_test_hedons_points_when_running_1min():
    """TestCarryingStarTired1: Test hedon loss from running after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1+3
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestCarryingStarTired1_test_hedons_points_when_carrying_1min():
    """TestCarryingStarTired1: Test hedon loss from textbooks after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1+3
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestCarryingStarTired1_test_health_points_run_seq_not_long():
    """TestCarryingStarTired1: Test health from running sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestCarryingStarTired1_test_health_points_carrying_seq_not_long():
    """TestCarryingStarTired1: Test health from textbook sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestCarryingStarTired1_test_hedons_points_run_seq_not_long():
    """TestCarryingStarTired1: Test hedons from running sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1+3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestCarryingStarTired1_test_hedons_points_carrying_seq_not_long():
    """TestCarryingStarTired1: Test hedons from textbook sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1+3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestCarryingStarTired1_test_health_point_run_seq_long1():
    """TestCarryingStarTired1: Test health from long running sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestCarryingStarTired1_test_hedon_point_run_seq_long1():
    """TestCarryingStarTired1: Test hedons from long running sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1+3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestCarryingStarTired1_test_health_point_run_seq_long2():
    """TestCarryingStarTired1: Test health from complex running sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestCarryingStarTired1_test_health_point_run_seq_long3():
    """TestCarryingStarTired1: Test health from extended running sequence after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestCarryingStarTired1_test_health_point_long_run():
    """TestCarryingStarTired1: Test health from single long run after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestCarryingStarTired1_test_most_fun_act():
    """TestCarryingStarTired1: Test most fun activity after textbook star activity"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestCarryingStarTired2 - Textbook star + running 1min (start_health=3, start_hedons=2)
def test_tired_TestCarryingStarTired2_test_health_points_when_running_1min():
    """TestCarryingStarTired2: Test health gain after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestCarryingStarTired2_test_health_points_when_carrying_1min():
    """TestCarryingStarTired2: Test health gain from textbooks after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestCarryingStarTired2_test_hedons_points_when_running_1min():
    """TestCarryingStarTired2: Test hedon loss from running after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestCarryingStarTired2_test_hedons_points_when_carrying_1min():
    """TestCarryingStarTired2: Test hedon loss from textbooks after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestCarryingStarTired2_test_health_points_run_seq_not_long():
    """TestCarryingStarTired2: Test health from running sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestCarryingStarTired2_test_health_points_carrying_seq_not_long():
    """TestCarryingStarTired2: Test health from textbook sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestCarryingStarTired2_test_hedons_points_run_seq_not_long():
    """TestCarryingStarTired2: Test hedons from running sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestCarryingStarTired2_test_hedons_points_carrying_seq_not_long():
    """TestCarryingStarTired2: Test hedons from textbook sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestCarryingStarTired2_test_health_point_run_seq_long1():
    """TestCarryingStarTired2: Test health from long running sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestCarryingStarTired2_test_hedon_point_run_seq_long1():
    """TestCarryingStarTired2: Test hedons from long running sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestCarryingStarTired2_test_health_point_run_seq_long2():
    """TestCarryingStarTired2: Test health from complex running sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestCarryingStarTired2_test_health_point_run_seq_long3():
    """TestCarryingStarTired2: Test health from extended running sequence after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestCarryingStarTired2_test_health_point_long_run():
    """TestCarryingStarTired2: Test health from single long run after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestCarryingStarTired2_test_most_fun_act():
    """TestCarryingStarTired2: Test most fun activity after textbook star offer + running"""
    gamify.initialize()
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestRunningStarTired1 - Running star + running 1min (start_health=3, start_hedons=5)
def test_tired_TestRunningStarTired1_test_health_points_when_running_1min():
    """TestRunningStarTired1: Test health gain after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestRunningStarTired1_test_health_points_when_carrying_1min():
    """TestRunningStarTired1: Test health gain from textbooks after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestRunningStarTired1_test_hedons_points_when_running_1min():
    """TestRunningStarTired1: Test hedon loss from running after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons = 2+3
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestRunningStarTired1_test_hedons_points_when_carrying_1min():
    """TestRunningStarTired1: Test hedon loss from textbooks after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons = 2+3
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestRunningStarTired1_test_health_points_run_seq_not_long():
    """TestRunningStarTired1: Test health from running sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestRunningStarTired1_test_health_points_carrying_seq_not_long():
    """TestRunningStarTired1: Test health from textbook sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestRunningStarTired1_test_hedons_points_run_seq_not_long():
    """TestRunningStarTired1: Test hedons from running sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons = 2+3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestRunningStarTired1_test_hedons_points_carrying_seq_not_long():
    """TestRunningStarTired1: Test hedons from textbook sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons = 2+3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestRunningStarTired1_test_health_point_run_seq_long1():
    """TestRunningStarTired1: Test health from long running sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestRunningStarTired1_test_hedon_point_run_seq_long1():
    """TestRunningStarTired1: Test hedons from long running sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons = 2+3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestRunningStarTired1_test_health_point_run_seq_long2():
    """TestRunningStarTired1: Test health from complex running sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestRunningStarTired1_test_health_point_run_seq_long3():
    """TestRunningStarTired1: Test health from extended running sequence after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestRunningStarTired1_test_health_point_long_run():
    """TestRunningStarTired1: Test health from single long run after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestRunningStarTired1_test_most_fun_act():
    """TestRunningStarTired1: Test most fun activity after running star activity"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestRunningStarTired2 - Running star + textbooks 1min (start_health=2, start_hedons=1)
def test_tired_TestRunningStarTired2_test_health_points_when_running_1min():
    """TestRunningStarTired2: Test health gain after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestRunningStarTired2_test_health_points_when_carrying_1min():
    """TestRunningStarTired2: Test health gain from textbooks after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestRunningStarTired2_test_hedons_points_when_running_1min():
    """TestRunningStarTired2: Test hedon loss from running after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestRunningStarTired2_test_hedons_points_when_carrying_1min():
    """TestRunningStarTired2: Test hedon loss from textbooks after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestRunningStarTired2_test_health_points_run_seq_not_long():
    """TestRunningStarTired2: Test health from running sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestRunningStarTired2_test_health_points_carrying_seq_not_long():
    """TestRunningStarTired2: Test health from textbook sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestRunningStarTired2_test_hedons_points_run_seq_not_long():
    """TestRunningStarTired2: Test hedons from running sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestRunningStarTired2_test_hedons_points_carrying_seq_not_long():
    """TestRunningStarTired2: Test hedons from textbook sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestRunningStarTired2_test_health_point_run_seq_long1():
    """TestRunningStarTired2: Test health from long running sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestRunningStarTired2_test_hedon_point_run_seq_long1():
    """TestRunningStarTired2: Test hedons from long running sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons = 1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestRunningStarTired2_test_health_point_run_seq_long2():
    """TestRunningStarTired2: Test health from complex running sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestRunningStarTired2_test_health_point_run_seq_long3():
    """TestRunningStarTired2: Test health from extended running sequence after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestRunningStarTired2_test_health_point_long_run():
    """TestRunningStarTired2: Test health from single long run after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestRunningStarTired2_test_most_fun_act():
    """TestRunningStarTired2: Test most fun activity after running star offer + textbooks"""
    gamify.initialize()
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestSimpleTiredRunningStarTired1 - Long run + running star + running 1min
def test_tired_TestSimpleTiredRunningStarTired1_test_health_points_when_running_1min():
    """TestSimpleTiredRunningStarTired1: Test health gain after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestSimpleTiredRunningStarTired1_test_hedons_points_when_running_1min():
    """TestSimpleTiredRunningStarTired1: Test hedon change after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestSimpleTiredRunningStarTired1_test_health_points_when_carrying_1min():
    """TestSimpleTiredRunningStarTired1: Test health gain from textbooks after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestSimpleTiredRunningStarTired1_test_hedons_points_when_carrying_1min():
    """TestSimpleTiredRunningStarTired1: Test hedon change from textbooks after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestSimpleTiredRunningStarTired1_test_health_points_run_seq_not_long():
    """TestSimpleTiredRunningStarTired1: Test health from running sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestSimpleTiredRunningStarTired1_test_health_points_carrying_seq_not_long():
    """TestSimpleTiredRunningStarTired1: Test health from textbook sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestSimpleTiredRunningStarTired1_test_hedons_points_run_seq_not_long():
    """TestSimpleTiredRunningStarTired1: Test hedons from running sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestSimpleTiredRunningStarTired1_test_hedons_points_carrying_seq_not_long():
    """TestSimpleTiredRunningStarTired1: Test hedons from textbook sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestSimpleTiredRunningStarTired1_test_health_point_run_seq_long1():
    """TestSimpleTiredRunningStarTired1: Test health from long running sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestSimpleTiredRunningStarTired1_test_hedon_point_run_seq_long1():
    """TestSimpleTiredRunningStarTired1: Test hedons from long running sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestSimpleTiredRunningStarTired1_test_health_point_run_seq_long2():
    """TestSimpleTiredRunningStarTired1: Test health from complex running sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestSimpleTiredRunningStarTired1_test_health_point_run_seq_long3():
    """TestSimpleTiredRunningStarTired1: Test health from extended running sequence after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestSimpleTiredRunningStarTired1_test_health_point_long_run():
    """TestSimpleTiredRunningStarTired1: Test health from single long run after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestSimpleTiredRunningStarTired1_test_most_fun_act():
    """TestSimpleTiredRunningStarTired1: Test most fun activity after very tired + running star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("running", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestSimpleTiredRunningStarTired2 - Long run + running star + textbooks 1min
def test_tired_TestSimpleTiredRunningStarTired2_test_health_points_when_running_1min():
    """TestSimpleTiredRunningStarTired2: Test health gain after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestSimpleTiredRunningStarTired2_test_hedons_points_when_running_1min():
    """TestSimpleTiredRunningStarTired2: Test hedon change after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons -= 2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestSimpleTiredRunningStarTired2_test_health_points_when_carrying_1min():
    """TestSimpleTiredRunningStarTired2: Test health gain from textbooks after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestSimpleTiredRunningStarTired2_test_hedons_points_when_carrying_1min():
    """TestSimpleTiredRunningStarTired2: Test hedon change from textbooks after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons -= 2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestSimpleTiredRunningStarTired2_test_health_points_run_seq_not_long():
    """TestSimpleTiredRunningStarTired2: Test health from running sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10

def test_tired_TestSimpleTiredRunningStarTired2_test_health_points_carrying_seq_not_long():
    """TestSimpleTiredRunningStarTired2: Test health from textbook sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestSimpleTiredRunningStarTired2_test_hedons_points_run_seq_not_long():
    """TestSimpleTiredRunningStarTired2: Test hedons from running sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons -= 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestSimpleTiredRunningStarTired2_test_hedons_points_carrying_seq_not_long():
    """TestSimpleTiredRunningStarTired2: Test hedons from textbook sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons -= 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestSimpleTiredRunningStarTired2_test_health_point_run_seq_long1():
    """TestSimpleTiredRunningStarTired2: Test health from long running sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestSimpleTiredRunningStarTired2_test_hedon_point_run_seq_long1():
    """TestSimpleTiredRunningStarTired2: Test hedons from long running sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_hedons -= 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestSimpleTiredRunningStarTired2_test_health_point_run_seq_long2():
    """TestSimpleTiredRunningStarTired2: Test health from complex running sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestSimpleTiredRunningStarTired2_test_health_point_run_seq_long3():
    """TestSimpleTiredRunningStarTired2: Test health from extended running sequence after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestSimpleTiredRunningStarTired2_test_health_point_long_run():
    """TestSimpleTiredRunningStarTired2: Test health from single long run after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestSimpleTiredRunningStarTired2_test_most_fun_act():
    """TestSimpleTiredRunningStarTired2: Test most fun activity after very tired + running star offer + textbooks"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("running")
    gamify.perform_activity("textbooks", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestSimpleTiredCarryingStarTired1 - Long run + textbook star + textbooks 1min
def test_tired_TestSimpleTiredCarryingStarTired1_test_health_points_when_carrying_1min():
    """TestSimpleTiredCarryingStarTired1: Test health gain from textbooks after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestSimpleTiredCarryingStarTired1_test_health_points_when_running_1min():
    """TestSimpleTiredCarryingStarTired1: Test health gain after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestSimpleTiredCarryingStarTired1_test_hedons_points_when_running_1min():
    """TestSimpleTiredCarryingStarTired1: Test hedon change after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2



def test_tired_TestSimpleTiredCarryingStarTired1_test_health_point_run_seq_long1():
    """TestSimpleTiredCarryingStarTired1: Test health from long running sequence after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestSimpleTiredCarryingStarTired1_test_hedon_point_run_seq_long1():
    """TestSimpleTiredCarryingStarTired1: Test hedons from long running sequence after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_hedons += (-2+3)*1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestSimpleTiredCarryingStarTired1_test_health_point_run_seq_long2():
    """TestSimpleTiredCarryingStarTired1: Test health from complex running sequence after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestSimpleTiredCarryingStarTired1_test_health_point_run_seq_long3():
    """TestSimpleTiredCarryingStarTired1: Test health from extended running sequence after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestSimpleTiredCarryingStarTired1_test_health_point_long_run():
    """TestSimpleTiredCarryingStarTired1: Test health from single long run after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    start_health = 3*170 + 2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestSimpleTiredCarryingStarTired1_test_most_fun_act():
    """TestSimpleTiredCarryingStarTired1: Test most fun activity after very tired + textbook star activity"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("textbooks", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestSimpleTiredCarryingStarTired2 - Long run + textbook star + running 1min
def test_tired_TestSimpleTiredCarryingStarTired2_test_health_points_when_running_1min():
    """TestSimpleTiredCarryingStarTired2: Test health gain after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 3

def test_tired_TestSimpleTiredCarryingStarTired2_test_hedons_points_when_running_1min():
    """TestSimpleTiredCarryingStarTired2: Test hedon change after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons += (-2)*1
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2



def test_tired_TestSimpleTiredCarryingStarTired2_test_health_point_run_seq_long1():
    """TestSimpleTiredCarryingStarTired2: Test health from long running sequence after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 3*180+20

def test_tired_TestSimpleTiredCarryingStarTired2_test_hedon_point_run_seq_long1():
    """TestSimpleTiredCarryingStarTired2: Test hedons from long running sequence after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    start_hedons = 20 + -2*160
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_hedons += (-2)*1
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestSimpleTiredCarryingStarTired2_test_health_point_run_seq_long2():
    """TestSimpleTiredCarryingStarTired2: Test health from complex running sequence after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 280*3+20

def test_tired_TestSimpleTiredCarryingStarTired2_test_health_point_run_seq_long3():
    """TestSimpleTiredCarryingStarTired2: Test health from extended running sequence after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 3*180 + 220

def test_tired_TestSimpleTiredCarryingStarTired2_test_health_point_long_run():
    """TestSimpleTiredCarryingStarTired2: Test health from single long run after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    start_health = 3*170 + 3
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 3*180+10

def test_tired_TestSimpleTiredCarryingStarTired2_test_most_fun_act():
    """TestSimpleTiredCarryingStarTired2: Test most fun activity after very tired + textbook star offer + running"""
    gamify.initialize()
    gamify.perform_activity("running", 170)
    gamify.offer_star("textbooks")
    gamify.perform_activity("running", 1)
    assert gamify.most_fun_activity_minute() == 'resting'

# TestLongRunningStarTired - Long run 180min (start_health=540, start_hedons=-320, long_run=True)
def test_tired_TestLongRunningStarTired_test_health_points_when_running_1min():
    """TestLongRunningStarTired: Test health gain after max running (long_run mode)"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity("running", 1)
    assert gamify.get_cur_health() == start_health + 1  # long_run mode gives +1 health

def test_tired_TestLongRunningStarTired_test_health_points_when_carrying_1min():
    """TestLongRunningStarTired: Test health gain from textbooks after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity("textbooks", 1)
    assert gamify.get_cur_health() == start_health + 2

def test_tired_TestLongRunningStarTired_test_hedons_points_when_running_1min():
    """TestLongRunningStarTired: Test hedon loss after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_hedons = 20-170*2
    gamify.perform_activity('running', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestLongRunningStarTired_test_hedons_points_when_carrying_1min():
    """TestLongRunningStarTired: Test hedon loss from textbooks after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_hedons = 20-170*2
    gamify.perform_activity('textbooks', 1)
    assert gamify.get_cur_hedons() == start_hedons - 2

def test_tired_TestLongRunningStarTired_test_health_points_run_seq_not_long():
    """TestLongRunningStarTired: Test health from running sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_health() == start_health + 3*10  # Normal +3 health per minute for 10 total minutes (1+2+3+4)

def test_tired_TestLongRunningStarTired_test_health_points_carrying_seq_not_long():
    """TestLongRunningStarTired: Test health from textbook sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_health() == start_health + 2*10

def test_tired_TestLongRunningStarTired_test_hedons_points_run_seq_not_long():
    """TestLongRunningStarTired: Test hedons from running sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_hedons = 20-170*2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 1)
    gamify.perform_activity('running', 2)
    gamify.perform_activity('running', 3)
    gamify.perform_activity('running', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestLongRunningStarTired_test_hedons_points_carrying_seq_not_long():
    """TestLongRunningStarTired: Test hedons from textbook sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_hedons = 20-170*2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('textbooks', 1)
    gamify.perform_activity('textbooks', 2)
    gamify.perform_activity('textbooks', 3)
    gamify.perform_activity('textbooks', 4)
    assert gamify.get_cur_hedons() == start_hedons - 2*10

def test_tired_TestLongRunningStarTired_test_health_point_run_seq_long1():
    """TestLongRunningStarTired: Test health from long running sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 1 + 3*180 + 19  # long_run mode adjustments

def test_tired_TestLongRunningStarTired_test_hedon_point_run_seq_long1():
    """TestLongRunningStarTired: Test hedons from long running sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_hedons = 20-170*2
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_hedons() == start_hedons - 2*200

def test_tired_TestLongRunningStarTired_test_health_point_run_seq_long2():
    """TestLongRunningStarTired: Test health from complex running sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    assert gamify.get_cur_health() == start_health + 1 + 3*180 + 19 + 3*100  # long_run mode adjustments

def test_tired_TestLongRunningStarTired_test_health_point_run_seq_long3():
    """TestLongRunningStarTired: Test health from extended running sequence after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 100)
    gamify.perform_activity('running', 200)
    assert gamify.get_cur_health() == start_health + 1 + 3*180 + 19 + 200  # long_run mode adjustments

def test_tired_TestLongRunningStarTired_test_health_point_long_run():
    """TestLongRunningStarTired: Test health from single long run after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    start_health = 3*180
    gamify.perform_activity('resting', 1)
    gamify.perform_activity('running', 190)
    assert gamify.get_cur_health() == start_health + 1 + 3*180 + 9  # long_run mode: +1 first, then +3*180, then +9

def test_tired_TestLongRunningStarTired_test_most_fun_act():
    """TestLongRunningStarTired: Test most fun activity after max running"""
    gamify.initialize()
    gamify.perform_activity("running", 180)
    assert gamify.most_fun_activity_minute() == 'resting'

if __name__ == '__main__':
    # Run all test_tired.py tests (168 total across 12 classes)
    print("Running TestTiredBasic tests...")
    # ... (run all 14 TestTiredBasic tests)

    print("Running TestSimpleTired tests...")
    # ... (run all 14 TestSimpleTired tests)

    print("Running TestTiredRestGap tests...")
    # ... (run all 14 TestTiredRestGap tests)

    print("Running TestTiredRestGap2 tests...")
    # ... (run all 14 TestTiredRestGap2 tests)

    print("Running TestTiredRestGapEasy tests...")
    # ... (run all 14 TestTiredRestGapEasy tests)

    print("Running TestCarryingStarTired1 tests...")
    # ... (run all 14 TestCarryingStarTired1 tests)

    print("Running TestCarryingStarTired2 tests...")
    # ... (run all 14 TestCarryingStarTired2 tests)

    print("Running TestRunningStarTired1 tests...")
    # ... (run all 14 TestRunningStarTired1 tests)

    print("Running TestRunningStarTired2 tests...")
    # ... (run all 14 TestRunningStarTired2 tests)

    print("Running TestSimpleTiredRunningStarTired1 tests...")
    # ... (run all 14 TestSimpleTiredRunningStarTired1 tests)

    print("Running TestSimpleTiredRunningStarTired2 tests...")
    # ... (run all 14 TestSimpleTiredRunningStarTired2 tests)

    print("Running TestSimpleTiredCarryingStarTired1 tests...")
    # ... (run all 14 TestSimpleTiredCarryingStarTired1 tests)

    print("Running TestSimpleTiredCarryingStarTired2 tests...")
    # ... (run all 14 TestSimpleTiredCarryingStarTired2 tests)

    print("Running TestLongRunningStarTired tests...")
    # ... (run all 14 TestLongRunningStarTired tests)

    print("All test_tired.py tests passed! (168 total)")
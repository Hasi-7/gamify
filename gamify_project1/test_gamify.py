# test_gamify.py
# Run with: python3 test_gamify.py
from gamify import (
    initialize,
    perform_activity,
    offer_star,
    get_cur_hedons,
    get_cur_health,
    most_fun_activity_minute,
    star_can_be_taken,
)

failed = []
test_count = 0
passed_count = 0


def report(name, expected, actual):
    global test_count, passed_count
    test_count += 1
    ok = expected == actual
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}\n  expected: {expected!r}\n  actual:   {actual!r}\n")
    if not ok:
        failed.append((name, expected, actual))
    else:
        passed_count += 1


# -------------------------
# Test 1: initial state
initialize()
report("T1 hedons initially", 0, get_cur_hedons())
report("T1 health initially", 0, get_cur_health())
report("T1 most_fun initially", "running", most_fun_activity_minute())

# -------------------------
# Test 2: running 30 (sample from handout)
initialize()
perform_activity("running", 30)
report("T2 hedons after running 30", -20, get_cur_hedons())
report("T2 health after running 30", 90, get_cur_health())
report("T2 most_fun after running 30", "resting", most_fun_activity_minute())

# -------------------------
# Test 3: full sample sequence from handout (checks many interactions)
initialize()
perform_activity("running", 30)
print("--- Sample sequence checkpoints ---")
# prints match handout sample. We report them below programmatically too.
report("T3-1 hedons after running 30", -20, get_cur_hedons())
report("T3-1 health after running 30", 90, get_cur_health())
report("T3-1 most_fun after running 30", "resting", most_fun_activity_minute())

perform_activity("resting", 30)
offer_star("running")
report("T3-2 most_fun after resting+offer_star(running)", "running", most_fun_activity_minute())

perform_activity("textbooks", 30)
report("T3-3 health after textbooks 30", 150, get_cur_health())
report("T3-3 hedons after textbooks 30", -80, get_cur_hedons())

offer_star("running")
perform_activity("running", 20)
report("T3-4 health after running 20", 210, get_cur_health())
report("T3-4 hedons after running 20", -90, get_cur_hedons())

perform_activity("running", 170)
report("T3-5 health after running 170", 700, get_cur_health())
report("T3-5 hedons after running 170", -430, get_cur_hedons())

# -------------------------
# Test 4: offer star then run 5 (not tired) -> big positive hedons
initialize()
offer_star("running")
report("T4 star_can_be_taken right after offer (running)", True, star_can_be_taken("running"))
perform_activity("running", 5)
report("T4 hedons after star+running5", 25, get_cur_hedons())  # 5*(2+3) = 25
report("T4 health after star+running5", 15, get_cur_health())

# -------------------------
# Test 5: star then run 5 then run 2 (star only for first perform_activity)
initialize()
offer_star("running")
perform_activity("running", 5)   # star applies, not tired
perform_activity("running", 2)   # new activity start => now tired => -2/min baseline
# hedons: first call 5*(2+3)=25 ; second call 2*(-2) = -4 => total 21
report("T5 hedons after star+run5 + run2", 21, get_cur_hedons())
report("T5 health total after run7", 21, get_cur_health())

# -------------------------
# Test 6: star then run 12 (covers star-limited 10 minutes)
initialize()
offer_star("running")
perform_activity("running", 12)
# first 10 min: (2+3)=5 => 50; next 2 min: -2 each => -4 => total 46
report("T6 hedons after star+running12", 46, get_cur_hedons())
report("T6 health after running12", 36, get_cur_health())

# -------------------------
# Test 7: star when tired
initialize()
perform_activity("running", 30)
offer_star("running")
perform_activity("running", 5)
# initial running gave -20 hedons. Now star when tired -> baseline -2 +3 = +1/min for 5 => +5
# total hedons -20 +5 = -15
report("T7 hedons after tired+star+running5", -15, get_cur_hedons())
report("T7 health after tired+star+running5", 105, get_cur_health())

# -------------------------
# Test 8: offer star then immediately do textbooks (star not taken)
initialize()
offer_star("running")
report("T8 star_can_be_taken immediately for running", True, star_can_be_taken("running"))
perform_activity("textbooks", 30)
# textbooks (not preceded by running) => first 20:+1, next 10:-1 => 20-10 = +10 hedons, health 60
report("T8 hedons after textbooks 30 (star wasted)", 10, get_cur_hedons())
report("T8 health after textbooks 30 (star wasted)", 60, get_cur_health())
report("T8 star_can_be_taken for running (should be False now)", False, star_can_be_taken("running"))

# -------------------------
# Test 9: boredom - three stars within 2 hours -> third star ineffective and thereafter no star bonuses
initialize()
# star 1
offer_star("running")
perform_activity("running", 1)  # star applies -> +5 hedons, +3 health
# offset a bit
perform_activity("resting", 10)
# star 2
offer_star("running")
perform_activity("running", 1)  # tired -> (-2 +3) = +1
perform_activity("resting", 10)
# star 3 (within 2 hours of star 1 & 2) -> ineffective
offer_star("running")
perform_activity("running", 1)  # tired & star ineffective => -2
# At this point hedons should be: 5 + 1 - 2 = 4 ; health = 3+3+3 = 9
report("T9 hedons after 3 stars within 2 hours (third ineffective)", 4, get_cur_hedons())
report("T9 health after 3 tiny runs", 9, get_cur_health())

# ensure subsequent stars are ineffective forever
offer_star("running")
report("T9 star_can_be_taken after boredom (should be False)", False, star_can_be_taken("running"))
perform_activity("running", 1)  # -2 more hedons
report("T9 hedons after additional run post-boredom", 2, get_cur_hedons())
report("T9 health after additional run post-boredom", 12, get_cur_health())

# -------------------------
# Test 10: stars spread out >2 hours -> not bored
initialize()
offer_star("running")
perform_activity("running", 1)  # +5
perform_activity("resting", 120)  # pass two hours exactly
offer_star("running")
report("T10 star_can_be_taken after 120-minute gap (not bored)", True, star_can_be_taken("running"))
perform_activity("running", 1)  # not tired (exactly 120 min gap -> not tired by "less than 2 hours"), star applies -> +5
# total hedons 5 + 5 = 10, health 6
report("T10 hedons after spaced stars", 10, get_cur_hedons())
report("T10 health after spaced stars", 6, get_cur_health())

# -------------------------
# Test 11: long continuous running health / hedons
initialize()
perform_activity("running", 200)
# health: 180*3 + 20*1 = 540 + 20 = 560
# hedons: first 10: +2*10 = 20 ; next 190: -2*190 = -380 => total -360
report("T11 health after running 200", 560, get_cur_health())
report("T11 hedons after running 200", -360, get_cur_hedons())
report("T11 most_fun after huge run (tired)", "resting", most_fun_activity_minute())

# -------------------------
# Test 12: running 150 -> textbooks 1 -> running 50 (health reset)
initialize()
perform_activity("running", 150)
perform_activity("textbooks", 1)
perform_activity("running", 50)
# health: first 150*3 = 450 ; textbooks +2 ; second run resets -> 50*3 = 150 ; total 602
# hedons: first run 150 -> 10*(+2)=20 + 140*(-2) = -280 => -260
# textbooks (tired) 1 min -> -2 => -262
# running 50 while tired -> 50 * (-2) = -100 => -362
report("T12 health after 150 run + textbooks 1 + run 50", 602, get_cur_health())
report("T12 hedons after 150 run + textbooks 1 + run 50", -362, get_cur_hedons())

# -------------------------
# Test 13: textbooks 25 (no tiredness)
initialize()
perform_activity("textbooks", 25)
# hedons: 20*1 + 5*(-1) = 15 ; health: 25*2 = 50
report("T13 hedons textbooks 25", 15, get_cur_hedons())
report("T13 health textbooks 25", 50, get_cur_health())

# -------------------------
# Test 14: invalid activity (should have no effect)
initialize()
perform_activity("swimming", 30)  # invalid: no effect
report("T14 hedons after invalid activity", 0, get_cur_hedons())
report("T14 health after invalid activity", 0, get_cur_health())

# -------------------------
# Test 15: offer star for textbooks and check most_fun
initialize()
perform_activity("resting", 30)
offer_star("textbooks")
report("T15 star_can_be_taken for textbooks", True, star_can_be_taken("textbooks"))
report("T15 most_fun immediately after offer(textbooks)", "textbooks", most_fun_activity_minute())
perform_activity("textbooks", 1)
# textbooks 1 minute: baseline +1 + star +3 => +4 hedons ; health +2
report("T15 hedons after taking textbooks-star for 1 minute", 4, get_cur_hedons())
report("T15 health after taking textbooks-star for 1 minute", 2, get_cur_health())

# -------------------------
# Test 16: star_can_be_taken returns False for wrong-activity queries
initialize()
offer_star("running")
report("T16 star_can_be_taken('textbooks') when 'running' offered", False, star_can_be_taken("textbooks"))

# -------------------------
# Test 17: offer star but immediately do textbooks then run (star lost; tiredness from textbooks)
initialize()
offer_star("running")
perform_activity("textbooks", 1)  # star for running wasted
perform_activity("running", 5)    # now tired (just finished textbooks) => baseline -2/min
# hedons: textbooks 1 -> +1 ; running 5 -> -10 ; total -9
# health: textbooks 2 + running 15 = 17
report("T17 hedons after offer->textbooks1->running5", -9, get_cur_hedons())
report("T17 health after offer->textbooks1->running5", 17, get_cur_health())

# -------------------------
# Summary
print("=== SUMMARY ===")
print(f"Total tests run: {test_count}")
print(f"Passed checks : {passed_count}")
print(f"Failed checks : {len(failed)}")
if failed:
    print("\nFailed details:")
    for name, exp, act in failed:
        print(f" - {name}: expected={exp!r} actual={act!r}")
else:
    print("All checks passed (expected if your gamify.py matches the spec).")

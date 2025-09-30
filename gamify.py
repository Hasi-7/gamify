
# initialize():
# Initialize all the global variables
# Set all starting values
# Parameters:
# None
# return:
# None

def initialize():
	global cur_hedons, cur_health

	global cur_time
	global last_activity, last_activity_duration
	global running_minutes
	
	global last_exercise_finished
	global bored_with_stars

	global cur_star, cur_star_activity, star_count
	global last_star_time, last_star_2_time

	global rested_2_hours

	cur_hedons = 0
	cur_health = 0
	
	cur_star = None
	cur_star_activity = None
	star_count = 0

	last_star_time = 0
	last_star_2_time = 0
	
	bored_with_stars = False
	
	last_activity = None
	last_activity_duration = 0
	running_minutes = 0

	cur_time = 0
	
	last_exercise_finished = 10000

	rested_2_hours = False

# variables_update():
# Update all general varaibles according to the duration and activity
# Parameters: 
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return:
# None

def variables_update(duration, activity):
	global cur_time, last_exercise_finished, last_activity, last_activity_duration, cur_star, last_star_time, last_star_2_time, cur_star_activity, rested_2_hours
	last_activity = activity
	last_activity_duration = duration
	cur_time += duration
	if activity == "running" or activity == "textbooks":
		last_exercise_finished = 0
	elif duration >= 120:
		rested_2_hours = True
		last_exercise_finished = duration
	else:
		last_exercise_finished = duration	
	if  cur_star and star_count == 1:
		last_star_time += duration
		cur_star_activity = None
	elif cur_star and star_count == 2:
		last_star_time += duration
		last_star_2_time += duration

# running_health(): 
# Check all the cases of when the user runs
# adjust cur_health accordingly
# Parameters: 
# duration (How long the acitvity is done for)
# activity (The activity that the user is performing)
# return: 
# None

def running_health(duration):
	global cur_health, running_minutes
	# First four if/elif statements check for all cases relevant to total consecutive running minutes being greater than 180
	if duration > 180:
		cur_health += (duration - 180) * 1 + 180 * 3
	elif running_minutes > 180:
		cur_health += duration * 1
	elif duration > 180:
		cur_health += 180 * 3 + (duration - 180) * 1
	elif duration + running_minutes > 180:
		cur_health += (180 - running_minutes) * 3 + (duration - (180 - running_minutes)) * 1	
	# The next else block is for when duration is less than 180 minutes, which has a constant amount of health points given for duration of running.
	else:
		cur_health += duration * 3

# running_hedons(): 
# Check all the cases of when the user runs
# Adjust hedons accordingly
# Parameters: 
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return: 
# None

def running_hedons(acitvity, duration):
	global bored_with_stars, cur_star_activity, cur_hedons, cur_star_activity, cur_star
	is_user_tired = is_tired()
	if bored_with_stars:
		pass
	else:
		# if x is 2 then the user is not tired and they will gain 2 hedons for the first 10 minutes then -2 for anything that follows
		# if x is -2 then the user is tired and will only gain -2 hedons for the total duration of their activity
		# is the multiplier for the hedons depending on if the user is tired or not
		x = 2
		if (is_user_tired):
			x = -2
		if cur_star and cur_star_activity == acitvity:
			star_bonus_running(duration, x)
		elif is_user_tired:
			cur_hedons += -2 * duration
		else:
			cur_hedons += 2 * 10 + (-2) * (duration - 10)

# star_bonus_running():
# Check how much star bonus the user recieves for having a star and using it immediately
# Adjust hedons according to the bonus for running
# Parameters:
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return:
# None

def star_bonus_running(duration, x):
	global cur_hedons, cur_star_activity, cur_star
	if duration <= 10:
		cur_hedons += (3+x)*duration
	else:
		cur_hedons += (3+x)*10 + (-2)*(duration-10) 
	cur_star_activity = None
	cur_star = False

# carrying_textbooks_health(): 
# Update cur_health based on duration
# Parameters: 
# duration (How long the activity is done for)
# return:
# None 

def carrying_textbooks_health(duration):
	global cur_health
	cur_health += duration*2

# carrying_textbooks_hedons(): 
# Check all the cases of when the user carries textbooks
# adjust hedons accordingly
# Parameters: 
# duration (How long the activity is done for)
# return:
# None

def carrying_textbooks_hedons(acitvity, duration):
	global bored_with_stars, cur_star_activity, cur_hedons, cur_star_activity, cur_star, last_star_time
	is_user_tired = is_tired()
	if bored_with_stars:
		pass
	else:
		# if x is 1 then the user is not tired and they will gain 1 hedons for the first 20 minutes then -1 for anything that follows
		# if x is -1 then the user is tired and will only gain -1 hedons for the total duration of their activity
		# x represents the hedons multiplier depending on if the user is tired or not
		x = 1
		if (is_user_tired):
			x = -2
		if cur_star and cur_star_activity == acitvity:
			star_bonus_textbooks(duration, x)
		else:
			if is_user_tired:
				cur_hedons += -2 * duration
			else:
				cur_hedons += 1 * 20 + ((-1) * (duration - 20))

# star_bonus_textbooks():
# Check how much star bonus the user recieves for having a star and using it immediately
# Adjust hedons according to the bonus for textbooks
# Parameters:
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return:
# None

def star_bonus_textbooks(duration, x):
	global cur_hedons, cur_star_activity, cur_star
	if duration <= 10:
		cur_hedons += (3+x) * duration
	else:
		if x == -2:
			cur_hedons += (3+x) * 10 + (x) * (duration - 10)
		else:
			cur_hedons += (3+x) * 10 + (x) * 10 + (-1) * (duration - 10)
	cur_star_activity = None
	cur_star = False

# perform_activity():
# Check which activity the user is performing
# Call functions accordingly which are associated with that activity
# Parameters:
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return:
# None

def perform_activity(activity, duration):
	global cur_star_activity, rested_2_hours
	update_running_minutes(activity)
	if activity == "running":
		running_health(duration)
		running_hedons(activity, duration)
		variables_update(duration, activity)
	elif activity == "textbooks":
		carrying_textbooks_health(duration)
		carrying_textbooks_hedons(activity, duration)
		variables_update(duration, activity)
	elif activity == "resting":
		variables_update(duration, activity)
	wasted_star(activity)

# wasted_star():
# Check if the user wasted their star
# Get rid of the star if it was wasted
# Parameters:
# activity (The activity that the user is performing)
# return:
# None

def wasted_star(activity):
	global cur_star_activity, cur_star
	if cur_star_activity != activity:
		cur_star_activity = None
		cur_star = False

# running_minutes():
# Check if the user is running consecutively
# Adjust the the minutes spent running
# Parameters:
# activity (The activity the user is running)
# return:
# None

def update_running_minutes(activity):
	global last_activity, last_activity_duration, running_minutes
	if last_activity == activity:
		running_minutes += last_activity_duration
	else:
		running_minutes = 0

# star_can_be_taken():
# Check if the activity is the same as the cur_star_activity
# And the user is not bored with stars
# And that the last star time is 0
# Parameters:
# activity (The activity that the user is performing)
# return:
# True if all the cases are true
# Else False if any one of the cases are false
	
def star_can_be_taken(activity):
	global cur_star_activity, bored_with_stars, last_star_time
	if (activity == cur_star_activity) and (not bored_with_stars) and (last_star_time == 0):
		return True
	return False

# get_cur_hedons():
# return the user's current hedons

def get_cur_hedons():
	global cur_hedons
	return cur_hedons
	
# get_cur_health():
# return the user's current health

def get_cur_health():
	global cur_health
	return cur_health
	
# offer_star():
# Offer the user a star for completing an activity
# Increment the number of active stars
# Set the current star activity to the activity that the user is being offered a star for
# Parameters:
# activity (The activity that the user is being offered a star for)
# return:
# None

def offer_star(activity):
	global cur_star, cur_star_activity, bored_with_stars, last_star_time, last_star_2_time, star_count
	# Resets the star count and timers if more than 2 hours have past since the first star
	if last_star_time >= 120:
		last_star_time = 0
		last_star_2_time = 0
		star_count = 0
	cur_star_activity = activity
	cur_star = True
	star_count += 1
	# if the user has recieved more than 2 stars within 2 hours since the first star,
	# then the user is now bored with stars and will not recieve anymore hedons for the rest of the game
	if star_count > 2 and last_star_time < 120:
		bored_with_stars = True

# most_fun_activity_minute():
# Check all cases for which the user can recieve hedons for
# return the activity that would give the user the most hedons per minute
# Parameters:
# None

def most_fun_activity_minute():
	global cur_star_activity
	if cur_star_activity != None:
		return cur_star_activity
	elif is_tired():
		return "resting"
	else:
		return "running"

# is_tired():
# Checks if the user is tired
# Parameters:
# None
# return:
# True if the user is tired
# False if the user is not tired

def is_tired():
	global last_exercise_finished
	if last_exercise_finished < 120:
		return True
	else:
		return False
				
if __name__ == '__main__':
	initialize()
	# perform_activity("textbooks", 30)
	# print(get_cur_hedons())
	# print(get_cur_health())
	# offer_star("textbooks")
	# perform_activity("textbooks", 70)
	# print(get_cur_hedons())
	# print(get_cur_health())  
	# perform_activity("textbooks", 4)
	# print(get_cur_hedons())
	# print(get_cur_health())
	# perform_activity("textbooks", 20)
	# print(get_cur_hedons())
	# print(get_cur_health())
	perform_activity("running", 30)    
	print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
	print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
	print(most_fun_activity_minute())  # resting                              # Test 3
	perform_activity("resting", 30)    
	offer_star("running")              
	print(most_fun_activity_minute())  # running                              # Test 4
	perform_activity("textbooks", 30)  
	print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
	print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
	offer_star("running")
	perform_activity("running", 20)
	print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
	print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
	perform_activity("running", 170)
	print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
	print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
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
	
	global last_finished
	global bored_with_stars

	global cur_star, cur_star_activity
	global last_star_time, last_star_2_time

	cur_hedons = 0
	cur_health = 0
	
	cur_star = 0
	cur_star_activity = None

	last_star_time = 0
	last_star_2_time = 0
	
	bored_with_stars = False
	
	last_activity = None
	last_activity_duration = 0
	
	cur_time = 0
	
	last_finished = -1000

# variables_update():
# Update all general varaibles according to the duration and activity
# Parameters: 
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return:
# None

def variables_update(duration, activity):
	global cur_time, last_finished, last_activity, last_activity_duration, cur_star, last_star_time, last_star_2_time
	if activity == "resting" and duration != 120:
		cur_time += duration
		last_finished = duration
	else:	
		cur_time += duration
		last_finished = duration
		last_activity = activity
		last_activity_duration = duration
	if cur_star == 1:
		last_star_time += duration
	elif cur_star == 2:
		last_star_time += duration
		last_star_2_time += duration


# running_health(): 
# Check all the cases of when the user runs
# adjust cur_health accordingly
# Parameters: 
# duration (How long the acitvity is done for)
# return: 
# None

def running_health(duration):
	global cur_health, last_activity, last_activity_duration
	# First three if/elif statements check for all cases relevant to duration/last_activity_duration being longer than 180 minutes
	if duration > 180:
		cur_health += (duration-180)*1 + 180*3
	elif (last_activity == "running" and last_activity_duration > 180) or (last_activity == "running" and last_activity_duration + duration > 180 and last_activity_duration > 180):
		cur_health += duration*1
	elif (last_activity == "running" and last_activity_duration + duration > 180 and last_activity_duration < 180):
		cur_health += (180-last_activity_duration)*3 + (duration - (180-last_activity_duration))*1
	# The next else block is for when duration is less than 180 minutes, which has a constant amount of health points given for x minutes of running.
	else:
		cur_health += duration*3

# running_hedons(): 
# Check all the cases of when the user runs
# Adjust hedons accordingly
# Parameters: 
# duration (How long the activity is done for)
# return: 
# None

def running_hedons(duration):
	global bored_with_stars, cur_star_activity, cur_hedons, cur_star_activity
	if bored_with_stars:
		pass
	elif not bored_with_stars and cur_star_activity == "running":
		if duration < 10:
			cur_hedons += (3+2)*duration
		else:
			cur_hedons += (3)*10 + (-2)*(duration) 
		cur_star_activity = None
	elif (is_tired()):
		cur_hedons += (-2)*duration
	else:
		cur_hedons += 10*2 + (-2)*(duration-10)

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

def carrying_textbooks_hedons(duration):
	global bored_with_stars, cur_star_activity, cur_hedons, cur_star_activity
	if bored_with_stars:
		pass
	elif not bored_with_stars and cur_star_activity == "textbooks":
		if duration < 10:
			cur_hedons += (3+2)*duration
		else:
			cur_hedons += 3*10 + (-2)*(duration)
		cur_star_activity = None
	elif (is_tired()):
		cur_hedons += (-2)*duration
	else:
		cur_hedons += 20*1 + (-1)*(duration-20)

# perform_activity():
# Check which activity the user is performing
# Call functions accordingly which are associated with that activity
# Parameters:
# duration (How long the activity is done for)
# activity (The activity that the user is performing)
# return:
# None

def perform_activity(activity, duration):
	if activity == "running":
		running_health(duration)
		running_hedons(duration)
		variables_update(duration, "running")
	elif activity == "textbooks":
		carrying_textbooks_health(duration)
		carrying_textbooks_hedons(duration)
		variables_update(duration, "textbooks")
	elif activity == "resting":
		variables_update(duration, "resting")

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
	global cur_star, cur_star_activity, bored_with_stars, last_star_time, last_star_2_time
	if last_star_time >= 120:
		cur_star = 0
		last_star_time = 0
		last_star_2_time = 0
	cur_star += 1
	cur_star_activity = activity
	if cur_star > 2 and last_star_time < 120:
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



def is_tired():
	global last_activity, last_finished
	if (last_activity == "running" or last_activity == "textbooks") and (last_finished < 120):
		return True
	else:
		return False
				
if __name__ == '__main__':
	initialize()
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
	
	
# This program is based on the article 
# "How to Calculate Your Leangain Macros", published by Andy Morgan
# Link: https://rippedbody.com/

# User input section
bodyWeight = float(input("input your body weight (kg): "))
bodyFat = float(input("input your body fat (%): "))
print("""1. Sedentary (little or no excercise)\n"""
      """2. Lightly active (training/sports 2-3 days/week)\n"""
      """3. Moderate active (training/sports 4-5 days/week)\n"""
      """4. Very active (training/sports 6-7 days/week)\n"""
      """5. Extremely active (twice per day, extra heavy workouts)""")
multiplierList = [1.2, 1.375, 1.55, 1.725, 1.9]
activityMultiplier = multiplierList[int(input("select your training intensity (index number): ")) - 1]

# Step 1. Calculate your BMR
LBM = bodyWeight * (1 - bodyFat / 100.0) # Lean body Mass
BMR = 370 + 21.6 * LBM 

# Step 2. Adjust for Activity
TDEE = BMR * activityMultiplier

# Step 3. Adjust Calorie Intake Based on Your Goal
# TODO: FAT LOSS
# GOAL: MUSCLE GAIN, Increase TDEE by 20%
calorieIntake = TDEE * 1.2 # kCal

# Step 4. Calculate Training & Rest Day Calorie Intake Targets
trainingIntake = calorieIntake * 1.2 # kCal
restIntake = calorieIntake * .8 # kCal

# Step 5. Set Your Protein Intake
targetProteinIntake = LBM * 2.5 # g

# Step 6. Set Your Fat Intake
targetAverageDailyFatIntake = calorieIntake * .3 / 9 # g
trainingFatIntake = targetAverageDailyFatIntake * 0.7 # g
restFatIntake = targetAverageDailyFatIntake * 1.3 # g

# Step 7. Calculate Carb Intake
trainingCarbIntake = (trainingIntake - targetProteinIntake * 4 - trainingFatIntake * 9) / 4.0
restCarbIntake = (restIntake - targetProteinIntake * 4 - restFatIntake * 9 ) / 4.0

# Report
print("Average Calorie Intake: {}kCal".format(calorieIntake))

print("\tCarbs\tProtein\tFat\tTotal\n" +
      "Trainin\t{}g\t{}g\t{}g\n".format(trainingCarbIntake, targetProteinIntake, trainingFatIntake) +
      "\t{}kCal\t{}kCal\t{}kCal\t{}kCal\n".format(trainingCarbIntake*4, targetProteinIntake*4, trainingFatIntake*9, (trainingCarbIntake + targetProteinIntake)*4 + trainingFatIntake*9) + 
      "{}\n".format("-"*20) +
      "Rest\t{}g\t{}g\t{}g\n".format(restCarbIntake, targetProteinIntake, restFatIntake) +
      "\t{}kCal\t{}kCal\t{}kCal\t{}kCal\n".format(restCarbIntake*4, targetProteinIntake*4, restFatIntake*9, (restCarbIntake + targetProteinIntake)*4 + restFatIntake*9)
      )

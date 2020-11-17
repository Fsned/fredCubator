import json
from datetime import datetime
import random
import sys

maxNumberOfExercises = 10
minNumberOfExercises = 6

maxIntensity = 100
totalIntensity = 0

def getWorkoutByTopic(exerciseCategory = "null", goalIntensity=50):
    global totalIntensity

    with open('/home/fsn/Documents/workoutGenerator/exerciseIndex.json', 'r') as exerciseIndexFile:
        exercises = json.loads(exerciseIndexFile.read())

    chosenExercises = []
    categoryIntensity = 0
    triesToFindExercise = 0
    while (triesToFindExercise < 6):
        triesToFindExercise += 1

        randomNumber = random.randint(1 , len(exercises[exerciseCategory]))
        exerciseName = str((exercises[exerciseCategory][randomNumber-1]['name']))            
        
        exerciseAlreadyChosen = False

        for a in chosenExercises:
            if exerciseName in a:
                exerciseAlreadyChosen = True
                continue
        
        if goalIntensity < (categoryIntensity + exercises[exerciseCategory][randomNumber-1]['intensity']):
            continue
        
        if (exerciseAlreadyChosen == False and exercises[exerciseCategory][randomNumber-1]['intensity'] + totalIntensity <= maxIntensity):
            numberOfSets = random.randint(exercises[exerciseCategory][randomNumber-1]['setsMin'], exercises[exerciseCategory][randomNumber-1]['setsMax'])
            numberOfReps = random.randint(exercises[exerciseCategory][randomNumber-1]['repsMin'], exercises[exerciseCategory][randomNumber-1]['repsMax'])
            categoryIntensity += exercises[exerciseCategory][randomNumber-1]['intensity']
            try:
                comment = exercises[exerciseCategory][randomNumber-1]['comment']
            except:
                comment = ""    
            
            chosenExercises.append(
                exerciseName + ": " + str(numberOfSets) + " sets of " + str(numberOfReps) + " " + exercises[exerciseCategory][randomNumber-1]['unit'] + "\t" + str(comment)
                )

    totalIntensity += categoryIntensity
    categoryJson = {}
    categoryJson['category'] = exerciseCategory
    categoryJson['exercises'] = chosenExercises
    workoutJson['Categories'] += categoryJson

    print (exerciseCategory)
    for a in chosenExercises:
        print ("- " + a)

## Read the workout scheme
with open('/home/fsn/Documents/workoutGenerator/workoutScheme.json', 'r') as workoutFile:
    data = json.loads(workoutFile.read())

currentWeek = int((datetime.now()).strftime("%W"))                          ## Read current week, save it as an integer
currentDay = str((datetime.now()).strftime("%A"))                           ## Read current day of week, as plain text to look up in the scheme afterwards
currentWorkoutWeek = str((currentWeek % int(data['weekPasses'])) + 1)       ## Figure out what workoutweek we're at
workoutTopics = json.dumps(data['weeks'][currentWorkoutWeek][currentDay])

weekDays = [    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    if (str(sys.argv[2] in weekDays)):
        currentDay = str(sys.argv[2])
except:
    print ("")

if (str(sys.argv[1]) == "--gen-workout"):
    print (currentDay)
    workoutsToNotCount = 0

    with open ('workout.json', 'w') as newFile:
        newFile.write("")
    if ("Mobility" in str(data['weeks'][currentWorkoutWeek][currentDay]) and len(data['weeks'][currentWorkoutWeek][currentDay]) > 1):
            workoutsToNotCount += 1

    workoutJson = {}
    workoutJson['Headline'] = currentDay
    workoutJson['Categories'] = []

    for a in data['weeks'][currentWorkoutWeek][currentDay]:
        print ()
        getWorkoutByTopic(exerciseCategory=data['weeks'][currentWorkoutWeek][currentDay][a], goalIntensity=(maxIntensity / (len(data['weeks'][currentWorkoutWeek][currentDay])-workoutsToNotCount)))

    with open('workout.json', 'w') as fp:
        json.dump(workoutJson, fp)

    print ("Total Intensity: " + str(totalIntensity))   

elif (str(sys.argv[1]) == "--gen-weekplan"):
    if len(sys.argv) == 3 and sys.argv[2] in weekDays:
        currentDay = str(sys.argv[2])
        print(currentDay)
        for a in data['weeks'][currentWorkoutWeek][currentDay]:
            output = json.dumps(data['weeks'][currentWorkoutWeek][currentDay][a])
            output = output[+1:-1]
            print (output)
    else:
        for a in weekDays:
            print (a)
            for key, value in data['weeks'][currentWorkoutWeek][a].items():
                print (value)
            print 
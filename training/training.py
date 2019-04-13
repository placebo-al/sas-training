class Workout(object):

    def __init__(self, name, sets, reps, exes):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.exes = exes
        if len(reps) == 1:
            reps += (len(exes)-1) * reps


#class Exercise(object):
#
#    def __init__(self, name, sets, reps):
#        self.name = name
#        self.sets = sets
#        self.reps = reps


programme1 = Workout('Programme 1',3 ,[5] , [
        'Push Ups',
        'Crunches',
        'Lunges',
        'Leg Raises',
        'Dips',
        'Bent Knee Sit-ups',
        'Calf Raises',
        'Thigh hand slides',
        'Chins',
        'Leg Raises',
        'Rear Scissors',
        'Bent Knee Sit-ups',
        ])

nov_weights = Workout('Novice Weights', 3, [10], exes = [ 
            'DB Laterals',
            'Flyes',
            'Bent Over Rows',
            'Standing Calf Raises',
            'BB Bicep Curls',
            'Squats',
            ])

abdominals = Workout(
    name = 'Abdominals',
    sets = 2,
    reps = [10],
    exes = [
            'V Crunches',
            'Twisting Crunches',
            'Bent Knee Sit Ups',
            'Wide Arm Press Ups',
            'Leg Raises',
            ])

everyday = Workout(
    name = 'Everyday Exercises',
    sets = 3,
    reps = [5],
    exes = [
            'Breathing Exercises',
            'Press ups',
            'Crunches',
            'Finger-tip Press ups',
            'Bent Knee Sit-ups',
            'Wide Arm Press ups',
            'Hand Slides',
            'Push ups',
            'Leg Raises',
            'Finger-tip Press ups',
            'Bent Knee Sit-ups',
            'Wide Arm Press ups',
            ])
    
programme2 = Workout(
    name = 'Programme 2',
    sets = 3,
    reps = [5],
    exes = [
            'Squat Thrusts',
            'Crunches',
            'Burpees',
            'Stride Jumps',
            'Bent Knee Sit Ups',
            'Alternate Strides',
            'Thigh Hand Slides',
            'Step Ups',
            'Leg Raises',
            'Jump Ups',
            'Sit Ups',
            ])
       
int_weights = Workout(
    name = 'Intermediate Strength',
    sets = 3,
    reps = [10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 5],
    exes = [
            'Flyes',
            'Bent Over Rows',
            'Standing Calf Raises',
            'BB Bicep Curls',
            'Squats',
            'Upright Rows',
            'Bench Presses',
            'One Arm Rows',
            'Standing Calf Raises',
            'Lying Triceps Presses',
            'Squats',
            ])

cycle = Workout(
    name = 'Cycle Workouts',
    sets = 1,
    exes = [
         'Stage 1',
         'Stage 2',
         'Stage 3',
         ],
    reps = [
        '16 km',
        '32 km',
        '80 km',
        ])


run = Workout(
    name = 'Run Workouts',
    sets = 1,
    exes = [
        'Short Run',
        'Fun Run',
        'Fast Run',
        'Long Run',
        ],
    reps = [
       '5 km, 30 minutes',
       '8.5 km',
       '5 km as fast as possible',
       '16 km',
       ])

timed_swim = Workout(
    name = 'Swimming Workout',
    sets = 1,
    reps =  [
            'Rest 3 mins',
            'Rest 6 mins',
            'Rest 6 mins',
            'Rest 3 mins',
            'Finish up',
            ],
    exes = [
            '4 Laps 3mins',
            '8 Laps 6mins',
            '16 Laps 12 mins',
            '8 Laps 6mins',
            '4 Laps 3mins',
            ])


fun_swim = Workout(
    name = 'Fun Swim',
    sets = 1,
    reps = [1],
    exes = ['30 mins vary strokes',])
    
programme3 = Workout(
    name = 'Programme 3',
    sets = 3,
    reps = [10],
    exes = [
            'Press Ups',
            'Crunches',
            'Squat Thrusts',
            'Straight Leg Raises',
            'Dips',
            'Bent Knee Sit Ups',
            'Burpees',
            'Thigh Hand Slides',
            'Chins',
            'Leg Raises',
            'Stride Jumps',
            'Sit Ups',
            'Calf Raises',
            'Crunches',
            'Step Ups',
            'Straight Leg Raises',
            'Lunges',
            'Bent Knee Sit Ups',
            'Jumps Ups',
            'Thigh Hand Slides',
            'Rear Scissors',
            'Leg Raises',
            ])

extras = Workout(
    name = 'Extra exercises',
    sets = 3,
    reps = [10],
    exes = [
            'Head Rolls',
            'Twisting Crunches',
            'Parallel Dips',
            'V Crunches',
            'Reverse Neck Rolls',
            'Rope Climb',
            'Chins Overhand',
            'Chins Underhand',
            ])

adv_weights = Workout(
    name = 'Advanced Weights',
    sets = 3,
    reps = [10],
    exes = [
            'DB Laterals',
            'Upright Rows',
            'Bent Over Laterals',
            'DB Presses',
            'Bench Presses',
            'Flyes',
            'Pullovers',
            'Squats',
            'Standing Calf Raises',
            'Leg Extensions',
            'Leg Curls',
            'BB Curls',
            'Lying Triceps Presses',
            'Wrist Curls',
            'Bent Over Rows',
            'One Arm Rows',
            'Deadlifts',
            'Squats',
            'Standing Calf Raises',
            'Leg Extensions',
            'Leg Curls',
            '''End of the week you can halve the weights and do 30then 40 and 50 reps before adding weight and starting again'''
            ])
    
    
class Weeks(object):
    
    def __init__(self, week):
        self.week = week

    def day(self):
        pass

beg_wk_1 = Weeks(
        [
        '40 mins run walk',
        'Stretch',
        'Programme 1 - 5 reps  -  Stretch',
        '5 x Sit ups, leg raises, Sit Ups, Crunches',
        'Novice Weights 2 sets  -  Stretch',
        'Rest',
        '30 mins Swim',
        ])
beg_wk_2 = Weeks(
        [
        'Abdominals 2 x 5',
        'Programme 1',
        'Abdominals 2 x 5',
        '40 mins run walk',
        'Abdominals 2 x 10',
        'Novice Weights',
        'Abdominals 2 x 10',
        ])
beg_wk_3 = Weeks(
        [
        '40 mins Run',
        'Abs and Pushups',
        'Programme 1',
        'Abs and Pushups',
        'Novice Weights',
        'Abs and Pushups',
        'Swim',
        ])
beg_wk_4 = Weeks(
        [
        'Abs and Pushups  -  40 mins Run',
        'Novice Weights',
        'Programme 1  -  40 mins Run',
        'Rest',
        'Abs and Pushups',
        'Novice Weights',
        'Programme 1',
        ])

int_wk_1 = Weeks(
        [
        "Run 5km  -  Programme 2  -  Stretch",
        "Rest",
        "Intermediate Weights",
        "Rest",
        "Cycling Stage one  -  Programme 2 - 10 reps  -  Stretch",
        "Rest",
        "Intermediate Weights",
        ])
int_wk_2 = Weeks(
        [
        "Timed Swim",
        "Run 5km - Stretch",
        "Rest",
        "Intermediate Weights",
        "Rest",
        "Cycle Stage 1 - Programme 2 - Stretch",
        "Timed Swim",
        ])
int_wk_3 = Weeks(
        [
        "Programme 2",
        "Rest",
        "Intermediate Weights",
        "Rest",
        "Cycle Stage 1 - Programme 2",
        "Rest",
        "Intermediate Weights",
        ])
int_wk_4 = Weeks(
        [
        "Swim",
        "Run - Programme 2",
        "Intermediate Weights",
        "Cycle - Programme 2",
        "Intermediate Weights",
        "Run - Programme 2",
        "Swim",
        ])


adv_wk_1 = Weeks(
        [
        "Run 8km  - Programme 3",
        "Rest",
        "Advanced Weights",
        "Timed Swim",
        "Cycling Stage 2  -  Advanced Weights 1 set",
        "Rest",
        "Fast Run  -  Programme 3",
        ])
adv_wk_2 = Weeks(
        [
        'Fun Swim',
        'Advanced Weights',
        'Rest',
        'Cycling Stage 2  - Advanced Weights + 2 reps',
        'Rest',
        'Advanced Weights',
        'Run 8km  -  Programme 3',
        ])
adv_wk_3 = Weeks(
        [
        'Timed Swim',
        'Advanced Weights',
        'Rest',
        'Cycling Stage 2  -  Programme 3',
        'Rest',
        'Advanced Weights',
        'Rest',
        ])
adv_wk_4 = Weeks(
        [
        'Programme 3',
        'Run 8kms',
        'Advanced Weights',
        'Cycling Stage 2',
        'Programme 3',
        'Advanced Weights',
        'Run 8kms',
        ])


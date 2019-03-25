class Exercise(object):
    def __init__(self):
        pass

    programme1 = { 
            'name': 'Programme 1',
            'tag': 'programme1',
            'sets': '3 sets',
            'reps': 5,
            'exes': [
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
                    ],
            }
    novice_weights = {
            'name': 'Novice Weights',
            'tag': 'nov_weights',
            'sets': '3 sets',
            'reps': 10,
            'exes': [ 
                    'DB Laterals',
                    'Flyes',
                    'Bent Over Rows',
                    'Standing Calf Raises',
                    'BB Bicep Curls',
                    'Squats',
                    ]
            }
    abdominals = {
            'name': 'Abdominals',
            'tag': 'abs',
            'sets': '2 sets',
            'reps': 10,
            'exes': [
                    'V Crunches',
                    'Twisting Crunches',
                    'Bent Knee Sit Ups',
                    'Wide Arm Press Ups',
                    'Leg Raises',
                    ]
            }
    everyday = {
            'name': 'Everyday Exercises',
            'tag': 'everyday',
            'sets': '3 sets',
            'reps': 5,
            'exes': [
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
                    ],
            }
    programme2 = {
            'name': 'Programme 2',
            'tag': 'programme2',
            'sets': '3 sets',
            'reps': 5,
            'exes': [
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
                    ],
            }
    int_strength = {
            'name': 'Intermediate Strength',
            'tag': 'int_strength',
            'sets': '3 sets',
            'reps': [10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 5],
            'exes': [
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
                    ],
            }
    cycle = {
            'name': 'Cycle Workouts',
            'tag': 'cycle',
            'sets': '',
            'exes': [
                 'Stage 1',
                 'Stage 2',
                 'Stage 3',
                 ],
            'reps': [
                '16 km',
                '32 km',
                '80 km',
                ],
            }
    run = {
            'name': 'Run Workouts',
            'tag': 'run',
            'sets': '',
            'exes': [
                 'Short Run',
                 'Fun Run',
                 'Fast Run',
                 'Long Run',
                 ],
            'reps': [
                '5 km, 30 minutes',
                '8.5 km',
                '5 km as fast as possible',
                '16 km',
                ],
            }
    timed_swim = {
            'name': 'Swimming Workout',
            'tag': 'timed_swim',
            'exes': [
                    '4 Laps 3mins',
                    '8 Laps 6mins',
                    '16 Laps 12 mins',
                    '8 Laps 6mins',
                    '4 Laps 3mins',
                    ],
            'reps': [
                'Rest 3 mins',
                'Rest 6 mins',
                'Rest 6 mins',
                'Rest 3 mins',
                'Finish up',
                ],
            }
    fun_swim = {
            'name': 'Fun Swim',
            'tag': 'fun_swim',
            'reps': '',
            'sets': '',
            'exes': ['30 mins vary strokes',]
            }

    programme3 = {
            'name': 'Programme 3',
            'tag': 'programme3',
            'sets': '3 sets',
            'reps': 10,
            'exes': [
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
                    ],
            }
    extras = {
            'name': 'Extra exercises',
            'tag': 'extras',
            'sets': '3 sets',
            'reps': 10,
            'exes': [
                    'Head Rolls',
                    'Twisting Crunches',
                    'Parallel Dips',
                    'V Crunches',
                    'Reverse Neck Rolls',
                    'Rope Climb',
                    'Chins Overhand',
                    'Chins Underhand',
                    ],
            }
    advancedweights = {
            'name': 'Advanced Weights',
            'tag': 'adv_weights',
            'sets': '3 sets',
            'reps': 10,
            'exes': [
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
                    ],
            }
            
class Weeks(object):
    def __init__(self):
        pass

    beginner_weeks = [
            [
            '40 mins run walk',
            'Stretch',
            'Programme 1 - 5 reps  -  Stretch',
            '5 x Sit ups, leg raises, Sit Ups, Crunches',
            'Novice Weights 2 sets  -  Stretch',
            'Rest',
            '30 mins Swim',
            ],
            [
            'Abdominals 2 x 5',
            'Programme 1',
            'Abdominals 2 x 5',
            '40 mins run walk',
            'Abdominals 2 x 10',
            'Novice Weights',
            'Abdominals 2 x 10',
            ],
            [
            '40 mins Run',
            'Abs and Pushups',
            'Programme 1',
            'Abs and Pushups',
            'Novice Weights',
            'Abs and Pushups',
            'Swim',
            ],
            [
            'Abs and Pushups  -  40 mins Run',
            'Novice Weights',
            'Programme 1  -  40 mins Run',
            'Rest',
            'Abs and Pushups',
            'Novice Weights',
            'Programme 1',
            ]
            ]

    intermediate_weeks = [
            [
            "Run 5km  -  Programme 2  -  Stretch",
            "Rest",
            "Intermediate Weights",
            "Rest",
            "Cycling Stage one  -  Programme 2 - 10 reps  -  Stretch",
            "Rest",
            "Intermediate Weights",
            ],
            [
            "Timed Swim",
            "Run 5km - Stretch",
            "Rest",
            "Intermediate Weights",
            "Rest",
            "Cycle Stage 1 - Programme 2 - Stretch",
            "Timed Swim",
            ],
            [
            "Programme 2",
            "Rest",
            "Intermediate Weights",
            "Rest",
            "Cycle Stage 1 - Programme 2",
            "Rest",
            "Intermediate Weights",
            ],
            [
            "Swim",
            "Run - Programme 2",
            "Intermediate Weights",
            "Cycle - Programme 2",
            "Intermediate Weights",
            "Run - Programme 2",
            "Swim",
            ],
        ]

    advanced_weeks = [
                [
                "Run 8km  - Programme 3",
                "Rest",
                "Advanced Weights",
                "Timed Swim",
                "Cycling Stage 2  -  Advanced Weights 1 set",
                "Rest",
                "Fast Run  -  Programme 3",
                ],
                [
                'Fun Swim',
                'Advanced Weights',
                'Rest',
                'Cycling Stage 2  - Advanced Weights + 2 reps',
                'Rest',
                'Advanced Weights',
                'Run 8km  -  Programme 3',
                ],
                [
                'Timed Swim',
                'Advanced Weights',
                'Rest',
                'Cycling Stage 2  -  Programme 3',
                'Rest',
                'Advanced Weights',
                'Rest',
                ],
                [
                'Programme 3',
                'Run 8kms',
                'Advanced Weights',
                'Cycling Stage 2',
                'Programme 3',
                'Advanced Weights',
                'Run 8kms',
                ],
    ]




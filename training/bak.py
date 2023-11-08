class Workout(object):

    def __init__(self, name, exes):
        self.name = name
        self.exes = exes


class Exercise(object):

    def __init__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps


def print_workout(printout):
    print(printout.name)
    print('_'*40)
    index = 0
    while index < len(printout.exes):
        print("{:25}sets: {:}\treps : {}".format(printout.exes[index].name, 
            printout.exes[index].sets, 
            printout.exes[index].reps))
        index += 1


class Weeks(object):
    
    def __init__(self, week):
        self.week = week

    def day(self):
        pass

def print_week(week):
    for line in week.week:
        print('Day: {}'.format(line))

p1a = Exercise(name = 'Push Ups', sets = 3, reps = 5)
p1b = Exercise(name = 'Crunches', sets = 3, reps = 5)
p1c = Exercise(name = 'Lunges', sets = 3, reps = 5)
p1d = Exercise(name = 'Leg Raises', sets = 3, reps = 5)
p1e = Exercise(name = 'Dips', sets = 3, reps = 5)
p1f = Exercise(name = 'Bent Knee Sit-ups', sets = 3, reps = 5)
p1g = Exercise(name = 'Calf Raises', sets = 3, reps = 5)
p1h = Exercise(name = 'Thigh hand slides', sets = 3, reps = 5)
p1i = Exercise(name = 'Chins', sets = 3, reps = 5)
p1j = Exercise(name = 'Leg Raises', sets = 3, reps = 5)
p1k = Exercise(name = 'Rear Scissors', sets = 3, reps = 5)
p1l = Exercise(name = 'Bent Knee Sit-ups', sets = 3, reps = 5)

programme1 = Workout(name = 'Programme 1', exes = [
    p1a, p1b, p1c, p1d, p1e, p1f, p1g, p1h, p1i, p1j, p1k, p1l
        ])

nwa = Exercise(name = 'DB Laterals', sets = 3, reps = 10)
nwb = Exercise(name = 'Flyes', sets = 3, reps = 10)
nwc = Exercise(name = 'Bent Over Rows', sets = 3, reps = 10)
nwd = Exercise(name = 'Standing Calf Raises', sets = 3, reps = 10)
nwe = Exercise(name = 'BB Bicep Curls', sets = 3, reps = 10)
nwf = Exercise(name = 'Squats', sets = 3, reps = 10)

nov_weights = Workout(name = 'Novice Weights', exes = [ 
    nwa, nwb, nwc, nwd, nwe, nwf
    ])

aba = Exercise('V Crunches', sets = 2, reps = 10)
abb = Exercise('Twisting Crunches', sets = 2, reps = 10)
abc = Exercise('Bent Knee Sit Ups', sets = 2, reps = 10)
abd = Exercise('Wide Arm Press Ups', sets = 2, reps = 10)
abe = Exercise('Leg Raises', sets = 2, reps = 10)

abdominals = Workout(name = 'Abdominals', exes = [
    aba, abb, abc, abd, abe
            ])


ea = Exercise(name = 'Breathing Exercises', sets = 3,reps = 5)
eb = Exercise(name = 'Press ups', sets = 3, reps = 5)
ec = Exercise(name = 'Crunches', sets = 3, reps = 5)
ed = Exercise(name = 'Finger-tip Press ups', sets = 3, reps = 5)
ee = Exercise(name = 'Bent Knee Sit-ups', sets = 3, reps = 5)
ef = Exercise(name = 'Wide Arm Press ups', sets = 3, reps = 5)
eg = Exercise(name = 'Hand Slides', sets = 3, reps = 5)
eh = Exercise(name = 'Push ups', sets = 3, reps = 5)
ei = Exercise(name = 'Leg Raises', sets = 3, reps = 5)
ej = Exercise(name = 'Finger-tip Press ups', sets = 3, reps = 5)
ek = Exercise(name = 'Bent Knee Sit-ups', sets = 3, reps = 5)
el = Exercise(name = 'Wide Arm Press ups', sets = 3, reps = 5)
 
everyday = Workout(name = 'Everyday Exercises', exes = [
    ea, eb, ec, ed, ee, ef, eg, eh, ei, ej, ek, el, 
    ])
    
p2a = Exercise(name = 'Squat Thrusts', sets = 3,reps = 5)
p2b = Exercise(name = 'Crunches', sets = 3, reps = 5)
p2c = Exercise(name = 'Burpees', sets = 3, reps = 5)
p2d = Exercise(name = 'Stride Jumps', sets = 3, reps = 5)
p2e = Exercise(name = 'Bent Knee Sit Ups', sets = 3, reps = 5)
p2f = Exercise(name = 'Alternate Strides', sets = 3, reps = 5)
p2g = Exercise(name = 'Thigh Hand Slides', sets = 3, reps = 5)
p2h = Exercise(name = 'Step Ups', sets = 3, reps = 5)
p2i = Exercise(name = 'Leg Raises', sets = 3, reps = 5)
p2j = Exercise(name = 'Jump Ups', sets = 3, reps = 5)
p2k = Exercise(name = 'Sit Ups', sets = 3, reps = 5)

programme2 = Workout(name = 'Programme 2', exes = [
    p2a, p2b, p2c, p2d, p2e, p2f, p2g, p2h, p2i, p2j, p2k,
    ])
       
iwa = Exercise(name = 'Flyes', sets = 3,reps = 10)
iwb = Exercise(name = 'Bent Over Rows', sets = 3, reps = 10)
iwc = Exercise(name = 'Standing Calf Raises', sets = 3, reps = 10)
iwd = Exercise(name = 'BB Bicep Curls', sets = 3, reps = 10)
iwe = Exercise(name = 'Squats', sets = 3, reps = 10)
iwf = Exercise(name = 'Upright Rows', sets = 3, reps = 5)
iwg = Exercise(name = 'Bench Presses', sets = 3, reps = 5)
iwh = Exercise(name = 'One Arm Rows', sets = 3, reps = 5)
iwi = Exercise(name = 'Standing Calf Raises', sets = 3, reps = 5)
iwj = Exercise(name = 'Lying Triceps Presses', sets = 3, reps = 5)
iwk = Exercise(name = 'Squats', sets = 3, reps = 5)

int_weights = Workout(name = 'Intermediate Strength', exes = [
    iwa, iwb, iwc, iwd, iwe, iwf, iwg, iwh, iwi, iwj, iwk, 
    ])

    
p3a = Exercise(name = 'Press Ups', sets = 3,reps = 10)
p3b = Exercise(name = 'Crunches', sets = 3, reps = 10)
p3c = Exercise(name = 'Squat Thrusts', sets = 3, reps = 10)
p3d = Exercise(name = 'Straight Leg Raises', sets = 3, reps = 10)
p3e = Exercise(name = 'Dips', sets = 3, reps = 10)
p3f = Exercise(name = 'Bent Knee Sit Ups', sets = 3, reps = 10)
p3g = Exercise(name = 'Burpees', sets = 3, reps = 10)
p3h = Exercise(name = 'Thigh Hand Slides', sets = 3, reps = 10)
p3i = Exercise(name = 'Chins', sets = 3, reps = 10)
p3j = Exercise(name = 'Leg Raises', sets = 3, reps = 10)
p3k = Exercise(name = 'Stride Jumps', sets = 3, reps = 10)
p3l = Exercise(name = 'Sit Ups', sets = 3, reps = 10)
p3m = Exercise(name = 'Calf Raises', sets = 3, reps = 10)
p3n = Exercise(name = 'Crunches', sets = 3, reps = 10)
p3o = Exercise(name = 'Step Ups', sets = 3, reps = 10)
p3p = Exercise(name = 'Straight Leg Raises', sets = 3, reps = 10)
p3q = Exercise(name = 'Lunges', sets = 3, reps = 10)
p3r = Exercise(name = 'Bent Knee Sit Ups', sets = 3, reps = 10)
p3s = Exercise(name = 'Jumps Ups', sets = 3, reps = 10)
p3t = Exercise(name = 'Thigh Hand Slides', sets = 3, reps = 10)
p3u = Exercise(name = 'Rear Scissors', sets = 3, reps = 10)
p3v = Exercise(name = 'Leg Raises', sets = 3, reps = 10)
  
programme3 = Workout(name = 'Programme 3', exes = [
    p3a, p3b, p3c, p3d, p3e, p3f, 
    p3g, p3h, p3i, p3j, p3k, p3l, 
    p3m, p3n, p3o, p3p, p3q, p3r, 
    p3s, p3t, p3u, p3v,
    ])
  
exa  = Exercise(name = 'Head Rolls', sets = 3,reps = 10)
exb  = Exercise(name = 'Twisting Crunches', sets = 3, reps = 10)
exc  = Exercise(name = 'Parallel Dips', sets = 3, reps = 10)
exd  = Exercise(name = 'V Crunches', sets = 3, reps = 10)
exe  = Exercise(name = 'Reverse Neck Rolls', sets = 3, reps = 10)
exf  = Exercise(name = 'Rope Climb', sets = 3, reps = 10)
exg  = Exercise(name = 'Chins Overhand', sets = 3, reps = 10)
exh  = Exercise(name = 'Chins Underhand', sets = 3, reps = 10)
 
extras = Workout(name = 'Extra exercises', exes = [
    exa, exb, exc, exd,
    exe, exf, exg, exh, 
    ])

awa  = Exercise(name = 'DB Laterals', sets = 3,reps = 10)
awb  = Exercise(name = 'Upright Rows', sets = 3, reps = 10)
awc  = Exercise(name = 'Bent Over Laterals', sets = 3, reps = 10)
awd  = Exercise(name = 'DB Presses', sets = 3, reps = 10)
awe  = Exercise(name = 'Bench Presses', sets = 3, reps = 10)
awf  = Exercise(name = 'Flyes', sets = 3, reps = 10)
awg  = Exercise(name = 'Pullovers', sets = 3, reps = 10)
awh  = Exercise(name = 'Squats', sets = 3, reps = 10)
awi  = Exercise(name = 'Standing Calf Raises', sets = 3, reps = 10)
awj  = Exercise(name = 'Leg Extensions', sets = 3, reps = 10)
awk  = Exercise(name = 'Leg Curls', sets = 3, reps = 10)
awl  = Exercise(name = 'BB Curls', sets = 3, reps = 10)
awm  = Exercise(name = 'Lying Triceps Presses', sets = 3, reps = 10)
awn  = Exercise(name = 'Wrist Curls', sets = 3, reps = 10)
awo  = Exercise(name = 'Bent Over Rows', sets = 3, reps = 10)
awp  = Exercise(name = 'One Arm Rows', sets = 3, reps = 10)
awq  = Exercise(name = 'Deadlifts', sets = 3, reps = 10)
awr  = Exercise(name = 'Squats', sets = 3, reps = 10)
aws  = Exercise(name = 'Standing Calf Raises', sets = 3, reps = 10)
awt  = Exercise(name = 'Leg Extensions', sets = 3, reps = 10)
awu  = Exercise(name = 'Leg Curls', sets = 3, reps = 10)
# '''End of the week you can halve the weights and do 30 then 40 and 50 reps before adding weight and starting again'''

adv_weights = Workout(name = 'Advanced Weights', exes = [
    awa, awb, awc, awd, 
    awe, awf, awg, awh, 
    awi, awj, awk, awl, 
    awm, awn, awo, awp, 
    awq, awr, aws, awt, awu, 
    ])


class Cardio(object):

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance



cy1 = Cardio(name = 'Stage 1', distance ='16 km')
cy2 = Cardio(name = 'Stage 2', distance = '32 km')
cy3 = Cardio(name = 'Stage 3', distance = '80 km')

cycle = Workout(name = 'Cycle Workouts', exes = [
    cy1, cy2, cy3
    ])
 


r1 = Cardio('Short Run', '5 km, 30 minutes')
r2 = Cardio('Fun Run', '8.5 km')
r3 = Cardio('Fast Run', '5 km as fast as possible')
r4 = Cardio('Long Run', '16 km')

run = Workout(name = 'Run Workouts', exes = [
    r1, r2, r3, r4
    ])

# timed_swim = Workout(name = 'Swimming Workout',
#     sets = 1,
#     reps =  [
#             'Rest 3 mins',
#             'Rest 6 mins',
#             'Rest 6 mins',
#             'Rest 3 mins',
#             'Finish up',
#             ],
#     exes = [
#             '4 Laps 3mins',
#             '8 Laps 6mins',
#             '16 Laps 12 mins',
#             '8 Laps 6mins',
#             '4 Laps 3mins',
#             ])
# 
# 

s1 = Cardio(name = 'Fun Swim', distance = '30 mins vary strokes')

fun_swim = Workout(name = 'Fun Swim', exes = [
    s1
    ])



beg_wk1 = Weeks(
        [
        '40 mins run walk',
        'Stretch',
        'Programme 1 - 5 reps  -  Stretch',
        '5 x Sit ups, leg raises, Sit Ups, Crunches',
        'Novice Weights 2 sets  -  Stretch',
        'Rest',
        '30 mins Swim',
        ])
beg_wk2 = Weeks(
        [
        'Abdominals 2 x 5',
        'Programme 1',
        'Abdominals 2 x 5',
        '40 mins run walk',
        'Abdominals 2 x 10',
        'Novice Weights',
        'Abdominals 2 x 10',
        ])
beg_wk3 = Weeks(
        [
        '40 mins Run',
        'Abs and Pushups',
        'Programme 1',
        'Abs and Pushups',
        'Novice Weights',
        'Abs and Pushups',
        'Swim',
        ])
beg_wk4 = Weeks(
        [
        'Abs and Pushups  -  40 mins Run',
        'Novice Weights',
        'Programme 1  -  40 mins Run',
        'Rest',
        'Abs and Pushups',
        'Novice Weights',
        'Programme 1',
        ])

int_wk1 = Weeks(
        [
        "Run 5km  -  Programme 2  -  Stretch",
        "Rest",
        "Intermediate Weights",
        "Rest",
        "Cycling Stage one  -  Programme 2 - 10 reps  -  Stretch",
        "Rest",
        "Intermediate Weights",
        ])
int_wk2 = Weeks(
        [
        "Timed Swim",
        "Run 5km - Stretch",
        "Rest",
        "Intermediate Weights",
        "Rest",
        "Cycle Stage 1 - Programme 2 - Stretch",
        "Timed Swim",
        ])
int_wk3 = Weeks(
        [
        "Programme 2",
        "Rest",
        "Intermediate Weights",
        "Rest",
        "Cycle Stage 1 - Programme 2",
        "Rest",
        "Intermediate Weights",
        ])
int_wk4 = Weeks(
        [
        "Swim",
        "Run - Programme 2",
        "Intermediate Weights",
        "Cycle - Programme 2",
        "Intermediate Weights",
        "Run - Programme 2",
        "Swim",
        ])


adv_wk1 = Weeks(
        [
        "Run 8km  - Programme 3",
        "Rest",
        "Advanced Weights",
        "Timed Swim",
        "Cycling Stage 2  -  Advanced Weights 1 set",
        "Rest",
        "Fast Run  -  Programme 3",
        ])
adv_wk2 = Weeks(
        [
        'Fun Swim',
        'Advanced Weights',
        'Rest',
        'Cycling Stage 2  - Advanced Weights + 2 reps',
        'Rest',
        'Advanced Weights',
        'Run 8km  -  Programme 3',
        ])
adv_wk3 = Weeks(
        [
        'Timed Swim',
        'Advanced Weights',
        'Rest',
        'Cycling Stage 2  -  Programme 3',
        'Rest',
        'Advanced Weights',
        'Rest',
        ])
adv_wk4 = Weeks(
        [
        'Programme 3',
        'Run 8kms',
        'Advanced Weights',
        'Cycling Stage 2',
        'Programme 3',
        'Advanced Weights',
        'Run 8kms',
        ])


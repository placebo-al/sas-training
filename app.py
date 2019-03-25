from flask import Flask
from flask import render_template
from training.training import *


app = Flask(__name__)

@app.route('/')

def index():
    exercises = Exercise()
    week = Weeks()
                    
    return render_template("index.html", 
            programme1=exercises.programme1, 
            novice_weights=exercises.novice_weights, 
            abdominals=exercises.abdominals,
            week=week.beginner_weeks,
            )


@app.route('/intermediate')

def intermediate():
    exercises = Exercise()
    week = Weeks()

    return render_template("int.html",
            everyday=exercises.everyday,
            programme1=exercises.programme1,
            programme2=exercises.programme2,
            int_strength=exercises.int_strength,
            cycle=exercises.cycle,
            timed_swim=exercises.timed_swim,
            week=week.intermediate_weeks,
            )


@app.route('/advanced')

def advanced():
    exercises = Exercise()
    week = Weeks()

    return render_template("adv.html",
            everyday=exercises.everyday,
            programme3=exercises.programme3,
            extras=exercises.extras,
            adv_weights=exercises.advancedweights,
            run=exercises.run,
            swim=exercises.fun_swim,
            week=week.advanced_weeks,
            )

if __name__ == "__main__":
    app.run()


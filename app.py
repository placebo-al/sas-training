from flask import Flask
from flask import render_template
from training.training import *


app = Flask(__name__)

@app.route('/')

def index():
    week = Weeks()
                    
    return render_template("index.html", 
            program1=programme1,
            nov_wts=novice_weights,
            abdominals=abdominals,
            week=week.beginner_weeks,
            )


@app.route('/intermediate')

def intermediate():
    week = Weeks()

    return render_template("int.html",
            everyday=everyday,
            program1=programme1,
            program2=programme2,
            int_strength=int_strength,
            cycle=cycle,
            timed_swim=timed_swim,
            week=week.intermediate_weeks,
            )


@app.route('/advanced')

def advanced():
    week = Weeks()

    return render_template("adv.html",
            everyday=everyday,
            programme3=programme3,
            extras=extras,
            adv_weights=advancedweights,
            run=run,
            swim=fun_swim,
            week=week.advanced_weeks,
            )

if __name__ == "__main__":
    app.run()


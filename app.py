from flask import Flask
from flask import render_template
from training.training import *


app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html", 
            program1=programme1,
            nov_weights=nov_weights,
            abdominals=abdominals,
            week1=beg_wk_1,
            week2=beg_wk_2,
            week3=beg_wk_3,
            week4=beg_wk_4,
            )


@app.route('/intermediate')

def intermediate():
    return render_template("int.html",
            everyday=everyday,
            program1=programme1,
            program2=programme2,
            int_weights=int_weights,
            cycle=cycle,
            timed_swim=timed_swim,
            week1=int_wk_1,
            week2=int_wk_2,
            week3=int_wk_3,
            week4=int_wk_4,
            )


@app.route('/advanced')

def advanced():
    return render_template("adv.html",
            everyday=everyday,
            programme3=programme3,
            extras=extras,
            adv_weights=adv_weights,
            run=run,
            swim=fun_swim,
            week1=adv_wk_1,
            week2=adv_wk_2,
            week3=adv_wk_3,
            week4=adv_wk_4,
            )

if __name__ == "__main__":
    app.run()


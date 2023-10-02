from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES_KEY = "responses"
app= Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension

@app.route("/")
def show_survey_start() :
    return render_template("survey_start.html", survey=survey)

@app.route("/begin", methods=["POST"])
def start_survey() :

    sessions[RESPONSES_KEY] = []
    return redirect("/questions/0")

@app.route("/answer", methods={"POST"})
def handle_questions():

    responses = sessions.get(RESPONSES_KEY)
    if (responses is None) :
        return redirect("/")
    if (len(responses) == len (survey.questions)) :
        return redirect("/complete")
    if (len(responses) !=qid):
        return redirect (f"/questions/{len(responses)}")
    questons = survey.questions[qid]
    return render_template(
        "questions.html", questions_num=qid, questions+questions)

@app.route("/complete")
def complete():
    return render_template("completion.html")
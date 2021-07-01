#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("trivia.html") # look for templates/trivia.html

@app.route("/submit_answer", methods = ["POST", "GET"])
def trivia_answer():
    if request.method == "POST":
        if request.form.get("user_answer"): # if user_answer as assigned via the POST
            my_user_answer = request.form.get("user_answer")
            if my_user_answer == "50":
                return redirect(url_for("correct_answer", correct_answer = my_user_answer))
            else:
                return redirect(url_for("landing_page"))
        else:
            return redirect(url_for("landing_page"))
        return "POST"
    else:
        return request.method

@app.route("/correct/<correct_answer>")
def correct_answer(correct_answer):
    correct_answer=str(correct_answer)
    return f"{correct_answer} is Correct!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application


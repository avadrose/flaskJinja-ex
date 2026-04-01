from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route("/")
def show_form():
    """Show form dynamically based on prompts"""
    return render_template("questions.html", prompts=story.prompts)

@app.route("/story")
def show_story():
    """Generate story from user input"""
    answers = {}

    for prompt in story.prompts:
        answers[prompt] = request.args[prompt]

    result = story.generate(answers)

    return render_template("story.html", story_text=result)
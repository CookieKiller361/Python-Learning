import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/exercise_task_week_3/templates/newspage.html")
def newspage():
    return render_template("/newspage.html")

if __name__ == "__main__":
    app.run(debug=True)   
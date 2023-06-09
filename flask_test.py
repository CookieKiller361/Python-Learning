from flask import Flask, render_template, url_for

app =Flask(__name__)

#route can executing a function by opening the link between the brackets
@app.route("/")
def start_page():
    return "<h1>Hello World<h1\>"

#make the route to index.html
@app.route("/helloworld")
def helloworld():
    return render_template("index.html")



#runs the Webapp by pressing debuggingkey
if __name__ == "__main__":
    app.run(debug=True)
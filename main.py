from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page - form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        class_name = request.form["class"]
        team = request.form["team"]
        project = request.form["project"]

        # For now, just show data on success page
        return render_template("success.html", name=name, class_name=class_name, team=team, project=project)
    return render_template("index.html")

# Success page
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)

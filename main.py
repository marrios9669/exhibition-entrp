from flask import Flask, render_template, request
import json
from pathlib import Path

app = Flask(__name__)
    if request.method == "POST":
        cls = request.form["class"].upper().strip()
        team = request.form["team"].strip()
        members = [m.strip() for m in request.form["members"].split(",") if m.strip()]
        location = request.form["location"].strip()

        if cls and team and members and location:
            data = load_data()  
DATA_FILE = Path("exhibition_data.json")

def load_data():
    if DATA_FILE.exists():
        return json.load(DATA_FILE.open())
    return {}

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
            if cls not in data:
                data[cls] = []
            data[cls].append({"team": team, "members": members, "location": location})
            save_data(data)
            message = f"Saved! {cls} - {team}"
        else:
            message = "Fill all fields!"

    return render_template("form.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

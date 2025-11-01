from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # handle form data here
        name = request.form.get("name")
        print(name)
        return "Form submitted!"
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run()

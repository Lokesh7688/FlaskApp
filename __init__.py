from flask import Flask
app = Flask(__name__)
@app.route("/")
def Flask():
    return "Hello, 1st Hosting!"
if __name__ == "__main__":
    app.run()

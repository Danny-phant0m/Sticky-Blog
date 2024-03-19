from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  """A basic route handler that returns a greeting."""
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)


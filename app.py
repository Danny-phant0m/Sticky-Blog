from flask import Flask, render_template, request, session
import sqlite3
import secrets

app = Flask(__name__)
connect = sqlite3.connect('database.db') 
connect.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)')
# Generate a random secret key
secret_key = secrets.token_hex(16)  # This generates a 32-character random string
app.secret_key = secret_key.encode('utf-8')


@app.route("/")
@app.route("/home")
def home():
  if session.get('logged_in'):
      return render_template("home.html")
  else:
      return render_template("index.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/SignUp", methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST': 
        email = request.form['email'] 
        password = request.form['password'] 
  
        with sqlite3.connect("database.db") as users: 
            cursor = users.cursor() 
            cursor.execute("INSERT INTO users (email,password) VALUES (?,?)", 
                (email,password)) 
            users.commit() 
            session['logged_in'] = True
            print(f"User '{email}' '{password}' saved to database!")
        return render_template("home.html") 
    else:
      return render_template("signup.html")

@app.route("/about")
def about():
  logged_in = session.get('logged_in', False)  # Check if the user is logged in
  return render_template("about.html", logged_in=logged_in)

@app.route("/contact")
def contact():
  logged_in = session.get('logged_in', False)  # Check if the user is logged in
  return render_template("contact.html", logged_in=logged_in)

if __name__ == "__main__":
  app.run(debug=True)


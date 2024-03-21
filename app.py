from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import secrets

app = Flask(__name__)
connect = sqlite3.connect('database.db') # Connects to the database
connect.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)')# creates a table if there is no table

# Generate a random secret key this is for like cookies stuff
secret_key = secrets.token_hex(16)  # This generates a 32-character random string
app.secret_key = secret_key.encode('utf-8')


@app.route("/")
@app.route("/home")
def home():
  if session.get('logged_in'): # checks if the user is logged in 
      return render_template("home.html")# if it is go to home page
  else:
      return render_template("index.html")# else home page without being logged in

@app.route("/login",  methods=['GET', 'POST'])
def login():
      if request.method == 'POST': #if it is a post request
            email = request.form['email'] # get the eamil from the form tag 
            password = request.form['password'] # get the password from the form tag

            # Connect to the database
            with sqlite3.connect("database.db") as conn:
                cursor = conn.cursor()

            # Check if a user with the provided email and password exists
            cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = cursor.fetchone()

            if user:
                # User exists, set logged_in session and redirect to home page
                session['logged_in'] = True # set the session to logged in 
                return redirect(url_for('home'))
            else:
                # User does not exist or incorrect credentials, redirect to sign up page
                return render_template('login.html', error = "Invalid Email or password")
      else:
        return render_template("login.html")

@app.route("/SignUp", methods=['GET', 'POST'])
def signUp():
     if request.method == 'POST':
        email = request.form['email'] 
        password = request.form['password'] 

        with sqlite3.connect("database.db") as users: 
            cursor = users.cursor() 
            
            # Check if the email already exists in the database
            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                return redirect(url_for('login'))  # Redirect to the login page
            else:
                cursor.execute("INSERT INTO users (email,password) VALUES (?,?)", 
                    (email,password)) 
                users.commit() 
                session['logged_in'] = True
                return redirect(url_for('home'))  # Redirect to the home page after signup
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

@app.route("/logout", methods=['GET', 'POST'])
def logout():
  # Invalidate user session basically log them out from the backend
  session.clear()
  return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)


from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
connect = sqlite3.connect('database.db') 
connect.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)') 

@app.route("/")
@app.route("/home")
def home():
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
            print(f"User '{email}' '{password}' saved to database!")
        return render_template("index.html") 
    else:
      return render_template("signup.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

if __name__ == "__main__":
  app.run(debug=True)


# flask se zaroori cheezein import kar rahe hain
from flask import Flask
# Is naye library ko import kar rahe hain jo database mein help karega
from flask_sqlalchemy import SQLAlchemy
import os # Yeh operating system ke saath kaam karne mein help karta hai

# --- DATABASE SETUP ---
# Project folder ka path nikal rahe hain
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Flask ko bata rahe hain ki hamari database file kahan save karni hai
# 'sqlite:///...' ka matlab hai ki hum SQLite database use kar rahe hain
# 'site.db' hamari database file ka naam hoga
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
# Yeh extra feature ko disable kar rahe hain jisse warning na aaye
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database object (db) bana rahe hain. Isi object ke through hum saare database operations karenge.
db = SQLAlchemy(app)

# --- DATABASE MODEL DEFINITION ---
# Yahan hum define kar rahe hain ki hamare 'Student' table mein kya-kya information hogi.
# Yeh ek blueprint jaisa hai.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Har student ke liye ek unique ID
    usn = db.Column(db.String(20), unique=True, nullable=False) # University Seat Number, unique hona chahiye
    name = db.Column(db.String(100), nullable=False) # Student ka naam
    phone_number = db.Column(db.String(15), unique=True, nullable=False) # Phone number, unique hona chahiye

    # Yeh function batata hai ki jab hum ek Student object ko print karein toh kya dikhe
    def __repr__(self):
        return f"Student('{self.usn}', '{self.name}')"

# --- API ROUTES ---
@app.route('/')
def home():
  return "Hello, DPI System! Database is connected."

# --- MAIN EXECUTION ---
if __name__ == '__main__':
    # Yeh check karega ki database file 'site.db' pehle se hai ya nahi.
    db_path = os.path.join(basedir, 'site.db')
    if not os.path.exists(db_path):
        print("Database not found, creating it...")
        # Agar database nahi hai, toh yeh app ke context mein
        # db.create_all() command chala dega, jo tables bana dega.
        with app.app_context():
            db.create_all()
        print("Database created!")

    # Ab server ko start karega
    app.run(debug=True)
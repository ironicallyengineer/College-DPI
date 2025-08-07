# Flask framework ko import kar rahe hain
# Flask humein aasani se web server banane mein help karta hai
from flask import Flask

# Ek naya Flask application bana rahe hain
# __name__ ek special Python variable hai jo Flask ko batata hai ki files kahan dhoondni hain
app = Flask(__name__)

# Yeh ek "route" hai. Yeh batata hai ki jab koi browser mein
# hamari website ka main page (जैसे http://127.0.0.1:5000/) kholeta hai,
# toh kya karna hai.
@app.route('/')
def home():
  # Yeh function chalega aur browser ko yeh text wapas bhejega
  return "Hello, DPI System!"

# Yeh check karta hai ki kya humne is file ko seedhe run kiya hai
# (na ki kisi aur file se import kiya hai).
# Agar haan, toh yeh server ko start kar dega.
if __name__ == '__main__':
  # app.run() server ko start karta hai.
  # debug=True ka matlab hai ki agar hum code mein koi change karke save karte hain,
  # toh server apne aap restart ho jayega. Yeh development ke liye bahut useful hai.
  app.run(debug=True)
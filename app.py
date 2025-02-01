from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

# Hashing function
def hashing(secret):
    return hashlib.sha256(secret.encode()).hexdigest()

# Route for index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Getting the key entered by the user
        user_key = request.form['key']
        
        # For simplicity, let's assume the expected key is "hello"
        expected_secret = "hello"
        
        # Hashing the entered key
        hashed_secret = hashing(user_key)

        # Verify the key
        if verifyPass(hashed_secret, expected_secret):
            message = "Voila! Both are same and you are authenticated"
        else:
            message = "Trespassing!! Not authenticated"
        
        return render_template_string(open('login.html').read(), message=message)

    # If it's a GET request
    return render_template_string(open('login.html').read(), message="Enter your key to sign in.")

# Function to verify the hashed key
def verifyPass(hashedSecret, expectedSecret):
    hashExpectedSecret = hashing(expectedSecret)
    return hashExpectedSecret == hashedSecret

if __name__ == "__main__":
    app.run(debug=True)

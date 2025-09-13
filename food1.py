# This is a simple Flask server for the Mood Foodie app.
# It serves the index.html file to a user's web browser.
#
# To run this server, you first need to install Flask:
# pip install Flask
#
# Then, you can run the server from your terminal:
# python server.py

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def home():
    """
    Renders the foodndex.html template.
    This is the main page of our Mood Foodie application.
    """
    return render_template('food.html')

# This block ensures the server runs only when the script is executed directly.
if __name__ == '__main__':
    # Run the Flask app on the local server.
    # debug=True allows for automatic reloading when you make changes.
    app.run(debug=True)

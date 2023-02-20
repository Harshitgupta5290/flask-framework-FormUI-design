#This code is written by Harshit Gupta.

# Defining global variables for username and password
username = 'Your email of Certifyme'
password = 'Your Certifyme Password'

# Import the Flask class and other necessary modules using pip install flask or name of the module in the terminal
from flask import Flask, render_template, request, jsonify
import base64
# It provides functions for encoding binary data to ASCII characters and decoding ASCII characters back to binary data.
import requests 
# The requests module is used for making HTTP requests in Python.
# It allows us to send HTTP/1.1 requests and provides support for various HTTP methods like GET, POST, PUT, DELETE, etc.

# Create a new Flask app instance
app = Flask(__name__, template_folder='template')
app.config['JSON_SORT_KEYS'] = False # Disable alphabetical sorting of JSON keys.
app.config['DEBUG'] = False # This configuration disables debug mode in Flask application.



# Set Cache-Control headers to prevent caching of responses
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    # This line of code sets the Cache-Control header of the response to "no-cache, no-store, must-revalidate".
    # This header instructs the client (e.g., web browser) to not cache the response, as it must be revalidated every time before it can be served again. #
    # This is important for ensuring that clients always receive the most up-to-date version of the response from the server.
    
    response.headers["Pragma"] = "no-cache" # Sets HTTP response header to disable caching.
    response.headers["Expires"] = "0"  # Setting the "Expires" header to 0 disables caching of the response.
    response.headers['Cache-Control'] = 'public, max-age=0'
    # This line sets the "Cache-Control" header of the HTTP response to allow caching by public caches for zero seconds.
    return response
    #The return response statement returns the modified response object back to the client.


# Define route for the home page
@app.route('/')
def home(): # This function returns the rendered home.html template.
    return render_template('home.html')

# Define route for creating credentials
@app.route('/Create_Credential', methods=['POST', 'GET'])
def create_credential():
    # Get name and email from form data
    name = request.form['name']
    email = request.form['email']
    # Encode the username and password as a token
    token = base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')
    # Define the data to be sent in the request
    data = {
        'name': name,
        'template_ID': 5020,
        'email': email,
        'text': 'VP Quadralogics',
        'license_number': 'TPR-1267Af23',
        'verify_mode': 'Passport Number',
        'verify_code': '13678AJKJY678JHGP0'
    }
    # Define headers for the request
    headers = {
        'Authorization': f'Basic {token}',
        # It sets the authorization header for basic authentication using the token variable which is the encoded username and password.
        'Content-Type': 'application/json'
        # 'Content-Type': 'application/json' sets the content type of the request to be sent as JSON.
    }
     # Send a POST request to create the credentials
    response = requests.post('https://my.certifyme.online/api/v1/credential', json=data, headers=headers)
    # Get the response data in JSON format
    responsedata = response.json()
    # Render the home page
    return render_template('home.html')

# Run the app on localhost
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

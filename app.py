from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has a file attached
    if 'file' not in request.files:
        return 'No file attached', 400
    
    file = request.files['file']
    
    # Save the file
    file.save(file.filename)
    
    # Read the file contents
    with open(file.filename, 'r') as f:
        file_contents = f.read()
    
    # Get the number of characters in the file
    num_characters = len(file_contents)
    
    # Get the number of capital letters in the file
    num_capital_letters = sum(1 for char in file_contents if char.isupper())
    
    # Prepare the response
    standard_response = {
        'standard_answer_score': num_characters,
        'optimized_answer_score': num_capital_letters,
        'standard_response': file_contents
    }
    
    return jsonify(standard_response)

if __name__ == '__main__':
    app.run()

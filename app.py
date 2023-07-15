from flask import Flask, request

app = Flask(__name__)

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
    
    return file_contents

if __name__ == '__main__':
    app.run()


# curl -X POST -F "file=@/path/to/your/file.txt" http://127.0.0.1:5000/upload

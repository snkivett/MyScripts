from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the home page!"

@app.route('/slides', methods=['GET'])
def get_slides():
    slides = [
        {"slide_number": 1, "elements_count": 5},
        {"slide_number": 2, "elements_count": 3},
        {"slide_number": 3, "elements_count": 4}
    ]
    return jsonify(slides)

@app.route('/lesson_workflow', methods=['POST'])
def lesson_workflow():
    # Add your lesson planning workflow logic here
    return jsonify({"message": "Workflow executed successfully"})

if __name__ == '__main__':
    app.run(port=5001)

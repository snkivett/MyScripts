from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the home page!"

@app.route('/slides', methods=['GET'])
def slides():
    # Dummy data to simulate Google Slides API response
    slides_data = {
        "slides": [
            {"title": "Slide 1", "content": "Content of Slide 1"},
            {"title": "Slide 2", "content": "Content of Slide 2"},
            {"title": "Slide 3", "content": "Content of Slide 3"}
        ]
    }
    return jsonify(slides_data)

if __name__ == '__main__':
    app.run(port=5001)

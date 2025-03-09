# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello, SlideForge!"

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


# @app.route('/generate', methods=['POST'])
# def generate_slides():
#     text = request.json.get('text', '')
#     slides = [{'title': 'SlideForge', 'content': line} for line in text.split('\n') if line]
#     return jsonify({'slides': slides})

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, SlideForge!"

@app.route('/generate', methods=['POST'])
def generate_slides():
    text = request.json.get('text', '')  # Grab 'text' from POST body
    lines = text.split('\n')  # Split by newlines
    slides = [{'title': 'SlideForge', 'content': line} for line in lines if line]
    return jsonify({'slides': slides})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
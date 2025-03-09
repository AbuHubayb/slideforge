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



# from flask import Flask, request, jsonify
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello, SlideForge!"

# @app.route('/generate', methods=['POST'])
# def generate_slides():
#     text = request.json.get('text', '')  # Grab 'text' from POST body
#     lines = text.split('\n')  # Split by newlines
#     slides = [{'title': f'Slide {i+1}', 'content': line} for i, line in enumerate(lines) if line]
#     return jsonify({'slides': slides})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, SlideForge!"

@app.route('/generate', methods=['POST'])
def generate_slides():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
        text = request.json.get('text')
        if text is None:
            return jsonify({'error': 'Missing "text" key in JSON'}), 400
        if not isinstance(text, str):
            return jsonify({'error': '"text" must be a string'}), 400
        lines = text.split('\n')
        slides = [{'title': f'Slide {i+1}', 'content': line.strip().capitalize()} for i, line in enumerate(lines) if line.strip().capitalize()]
        return jsonify({'slides': slides})
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, render_template_string
import target  # Assuming your code is in target.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <h1>Message Encoder/Decoder</h1>
        <form method="post" action="/encode">
            <label for="message">Enter your message:</label>
            <input type="text" id="message" name="message">
            <button type="submit">Encode</button>
        </form>
        <form method="post" action="/decode">
            <label for="message">Enter your message:</label>
            <input type="text" id="message" name="message">
            <button type="submit">Decode</button>
        </form>
    ''')

@app.route('/encode', methods=['POST'])
def encode():
    message = request.form['message']
    encoded_message = target.encode_message(message)  # Assuming you have an encode_message function
    return f'<h1>Encoded Message: {encoded_message}</h1>'

@app.route('/decode', methods=['POST'])
def decode():
    message = request.form['message']
    decoded_message = target.decode_message(message)  # Assuming you have a decode_message function
    return f'<h1>Decoded Message: {decoded_message}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

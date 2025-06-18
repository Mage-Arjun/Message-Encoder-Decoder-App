Message Encoder/Decoder Web & Desktop App

This project is a dual-interface Message Encoder/Decoder application that allows users to encode and decode text messages using a simple word-shuffling and obfuscation technique. The application is implemented in both a web-based interface using Flask and a desktop GUI using Tkinter.

🔐 Encoding/Decoding Logic

Encoding: For words with 3 or more characters, three random letters are prefixed and suffixed, and the first letter of the word is moved to the end. Shorter words are simply reversed.

Decoding: The encoded words have the random characters removed and the original first letter is moved back to the front. Short words are reversed again.

🌐 Web Interface (Flask)

Users can input a message into a form and choose to either encode or decode it.

The result is displayed directly on the webpage.

Assumes the logic is implemented in a separate Python file (target.py) with encode_message() and decode_message() functions.

🖥️ Desktop Interface (Tkinter)

A standalone GUI with input fields and buttons for encoding and decoding.

Results are shown in a text box within the application window.

Easy to use and ideal for local, offline use.


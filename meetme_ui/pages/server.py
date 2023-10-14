from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get("message")

    # For now, let's send back a simple acknowledgment. 
    # You can later replace this with more complex logic.
    response_message = f"Received: {user_message}"

    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(debug=True)

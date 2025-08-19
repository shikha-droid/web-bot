from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def get_reply(user):
    user = user.lower()
    if "hi" in user or "hello" in user:
        return random.choice(["Hey there! 👋", "Hiya! 😄", "Hello! How’s it going?", "Yo! What’s up? 😎"])
    elif "sup" in user or "what's up" in user:
        return random.choice(["Not much, just chilling. You?", "Just hanging out 😏", "All good here, what about you?", "Trying to be as fun as possible 😎"])
    elif "sad" in user or "bored" in user:
        return random.choice(["Aww, hope things get better! 💛", "Cheer up! Wanna joke? 😆", "Oh no! Want to chat about it?"])
    elif "bye" in user or "see ya" in user:
        return random.choice(["Goodbye! 👋", "See you later! Take care!", "Bye! Hope to chat soon!"])
    else:
        return random.choice([f"Haha, '{user}' sounds interesting! 😂", f"Wow! You said '{user}', tell me more!", "Ooooh, cool 😏", "Hmm… I didn’t expect that!"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    bot_reply = get_reply(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
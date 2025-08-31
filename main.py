from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def get_reply(user):
    user = user.lower()
    
    if "hi" in user or "hello" in user or "hey" in user:
        return random.choice([
            "Hey there, 🖐",
            "Oh, it's you… hi ",
            "Hello hello, lmao",
            "Yo, sup "
        ])
        
    elif "sup" in user or "what's up" in user:
        return random.choice([
            "Not much, just existing lol",
            "Chillin’ ",
            "All good here, you?",
            "Trying not to be boring, lmao"
        ])
        
    elif "sad" in user or "bored" in user:
        return random.choice([
            "Bruh, same mood ",
            "Don’t be sad, be sarcastic 😼",
            "Bored? Talk to me, lol",
            "Aww, come here "
        ])
        
    elif "bye" in user or "see ya" in user:
        return random.choice([
            "Later, and istg don’t ghost me",
            "Bye bye, lol",
            "See ya, don’t miss me ",
            "Aight, lmao, peace"
        ])
    
    elif "why" in user or "you" in user:
        return random.choice([
            "I'm just like this 😌",
            "User made me 💻",
            "Don't blame me, blame my code 🤖",
            "Running on Python energy 🐍"
        ])
    
    else:
        return random.choice([
            f"Lol, did you really just say '{user}'?",
            f"Wow, '{user}'… groundbreaking",
            f"Hmm, interesting… not really",
            f"Ooooh edgy, huh"
        ])

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

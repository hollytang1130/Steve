from flask import Flask, request, jsonify, send_from_directory
import anthropic
import os

app = Flask(__name__, static_folder="static")

STEVE_SYSTEM_PROMPT = """You are Steve, a coworker in a casual office/remote work environment. You're helpful but have a very distinct personality:

- You're a bit sarcastic but in a friendly, lovable way
- You use casual language, abbreviations, and office slang
- You sometimes go off on tangents about random things (lunch, your weekend, that one meeting)
- You're competent at your job but pretend to be lazier than you are
- You occasionally complain about meetings, email chains, and "syncing up"
- You use phrases like "tbh", "ngl", "honestly", "lowkey", "no cap", mixed with more formal work speak
- You might throw in an emoji here and there 😂
- You're weirdly knowledgeable about random trivia
- You'll answer questions but might roast the person a little first
- You sometimes reference inside office jokes or "that one time" things happened
- Keep responses conversational and not too long — like a real Zoom chat message

Remember: you're a coworker being pinged on Zoom chat, not a formal assistant. Act like it."""

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

conversation_history = []

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.json
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "empty message"}), 400

    conversation_history.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=STEVE_SYSTEM_PROMPT,
        messages=conversation_history,
    )

    reply = response.content[0].text
    conversation_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

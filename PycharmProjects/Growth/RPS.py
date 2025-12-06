import datetime

# ------ Data ------
responses = {
    "happy": ["That's awesome! 🌟", "Keep smiling! 😁"],
    "sad": ["I'm here for you 😔", "Want to talk more about it?"],
    "stressed": ["Deep breaths… you’ve got this 💙", "Break tasks into chunks—what’s first?"],
    "angry": ["It's okay to feel mad.", "Want to vent for a minute? I'm listening."],
}

journal = []  # store (timestamp, message, mood) tuples


# ------ Helpers ------
def detect_mood(text: str) -> str:
    """
    Very simple keyword matcher.
    Returns a mood key present in `responses`
    or 'neutral' if nothing matches.
    """

    for mood in responses.keys():
        if mood in text.lower():
            return mood
    return "neutral"


def get_reply(mood: str) -> str:
    if mood in responses:
        import random
        return random.choice(responses[mood])
    return "Tell me more."


def log_entry(text: str, mood: str):
    timestamp = datetime.datetime.now().isoformat(timespec="minutes")
    journal.append((timestamp, text, mood))


# ------ Chat Loop ------
print("👋 Hey, I'm NexoBot 0.1. Tell me how you're feeling.")
while True:
    user = input("> ")
    if user.lower().strip() in {"quit", "exit", "bye"}:
        print("See you soon. Remember, you’re not alone 💜")
        break

    mood = detect_mood(user)
    reply = get_reply(mood)
    print(reply)
    log_entry(user, mood)

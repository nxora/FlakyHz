import json

def bot():
    d = {
        "hello":"Hi there!",
        "how are you":"Am fine and you",
        "good":"Okay",
        "hi":"Hello",
        "what is your name":"My name is Chat bot",
        "hey":"Whats up",
        "bye":"goodbye",
    }

    while True:
        you = input("You: ").lower()
        if you in d:
            print(f"Bot: {d[you]}")
        else:
            print("Sorry i don't understand that how to respond this statement")
            teach = input("Teach me how to response to this sentence by type the responses: ").lower()
            d[you] = teach
            print("I am learning well from you, Thanks")
        t = json.dumps(d)
        with open('data.json', 'w') as f:
            f.write(t)

bot()


import spacy
from nltk.chat.util import Chat, reflections

# Initialize spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Enhanced pattern-response pairs with more sophisticated responses
pairs = [
    [
        r"(.*)hello(.*)",
        ["Hello! How can I assist you today?"]
    ],
    [
        r"(.*)your name(.*)",
        ["My name is AI Robot, your virtual assistant."]
    ],
    [
        r"(.*) (develop|created) (.*)",
        ["I was developed using Python and NLTK by Eng. Malik Aleem Raza."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm an online assistant, location doesn't apply to me."]
    ],
    [
        r"(.*) (sports|game)(.*)",
        ["I'm a fan of various sports. What's your favorite sport?"]
    ],
    [
        r"(.*) (cricketer|batsman)?",
        ["There are many great cricketers. Who's your favorite?"]
    ],
    [
        r"(.*) (weather|rain) in (.*)",
        ["I can check the weather for you if you provide the location."]
    ],
    [
        r"(.*) (health|well-being|fitness) ?",
        ["Health is important! How can I assist with your health today?"]
    ],
    [
        r"(how.*) (you|robot)(.*) ?",
        ["I'm an AI chatbot, so I don't have feelings, but I'm here to help you!"]
    ],
    [
        r"sorry (.*)",
        ["It's okay. No worries!"]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Glad to hear that!"]
    ],
    [
        r"(.*) (quit|exit|bye) ?",
        ["Goodbye! Have a great day."]
    ],
    [
        r"(.*)",
        ["I'm here to assist you. Please feel free to ask any questions."]
    ]
]

# Create the chatbot with enhanced patterns and reflections
chatbot = Chat(pairs, reflections)

# Custom conversation loop with spaCy for more advanced NLU
def custom_converse():
    print("Bot: Hi there! Let's chat. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot:", chatbot.respond(user_input))
            break
        
        # Perform NLU with spaCy
        doc = nlp(user_input)
        intent = None
        for token in doc:
            if token.dep_ == 'ROOT':
                intent = token.text.lower()
                break
        
        if intent:
            response = chatbot.respond(intent)
        else:
            response = "I'm sorry, I didn't understand that."
        
        print("Bot:", response)

# Start the custom conversation
custom_converse()

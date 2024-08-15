from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Mauju',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3',
)

list_to_train = [
    "hi",
    "hi there!",
    "what's your name?",
    "I am a chatbot",
    "your name",
    "I am a chatbot",
    "name",
    "I am a chatbot",
    "how old are you?",
    "I'am ageless",
    "how old",
    "I'am ageless",
    "old",
    "I'am ageless",
    "old you",
    "I'am ageless",
    "your old",
    "I'am ageless",
]

list_trainer = ListTrainer(bot)

print("Start training bot..")
list_trainer.train(list_to_train)
print("Training successfully")

while True:
    user_response = input("User: ")
    response = bot.get_response(user_response)
    print("Bot: " + str(response))

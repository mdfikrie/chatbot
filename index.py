from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot = ChatBot(
    'Mauju',
    read_only=False,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry I do not have an answer!',
            'maximum_similarity_threshold': 0.9
        },
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter'
    ],
)


# list_to_train = [
#     "hi",
#     "hi mate!",
#     "what website you have?",
#     "Please visit this link for more info: https://www.mauju.com",
#     "what is your contact info?",
#     "head on over https://www.mauju.com/contact"
#     "can you open start trial page?",
#     "Of course, visit this link https://invoice.mauju.com/register?step=try_for_free",
#     "can you open about info page?",
#     "Of course, visit this link https://www.mauju.com/about",

# ]

# list_trainer = ListTrainer(bot)

# print("Start training bot..")
# list_trainer.train(list_to_train)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
# print("Training successfully")

@app.route("/")
def main():
    return render_template('index.html')


# while True:
#     user_response = input("User: ")
#     response = bot.get_response(user_response)
#     print("Bot: " + str(response))

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get("userMessage");
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
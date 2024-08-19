from chatterbot import ChatBot

bot = ChatBot(
    "Math",
    logic_adapters = [
        "chatterbot.logic.MathematicalEvaluation"
        ]
    )

print("------------ Math -------------")

while True:
    user_text = input("Type math equation that you want to solve: ")
    print("Bot "+str(bot.get_response(user_text)))
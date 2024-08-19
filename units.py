from chatterbot import ChatBot

bot = ChatBot("Units", logic_adapters=["chatterbot.logic.UnitConversion"])

# must install pint

while True:
    response_user = input("Ask a question (Unit Conversion): ")
    bot_response = bot.get_response(response_user)
    print("Bot: " + str(bot_response))
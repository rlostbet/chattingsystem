from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from myTool import Line

from chatbot_cmds import GetWords, CheckForCmd
from chatbot_interact import respondSequence

from time import sleep

bot1 = ChatBot('Bot1')

print("Training BOT1")
Line()
bot1.set_trainer(ChatterBotCorpusTrainer)
bot1.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor",
    "chatterbot.corpus.english.botprofile"
)

# for multi lingual
# bot.train("chatterbot.corpus.korean")

# Human Training
while True:
    words = GetWords()

    if words[0].capitalize() == "Quit":
        break

    if CheckForCmd(words):# <--- it
        """If there is command it calls it."""

    else:
        message = " ".join(words)
        print(f"BOT: {bot1.get_response(message)}")


# Bot Training Each other.. ??
# False Loop. Just to make sure it don't work
while False:
    # ugly code >:(
    message = bot1.get_response(message)
    print(f"BOT1: {message} ")
    sleep(0.5)
    message = bot1.get_response(message)
    print(f"BOT2: {message}")


# study more about this function.
# Print("Exporting The Training Result..")
# bot.trainer.export_for_training('./export.yml')

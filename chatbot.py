from talk_file import readTalkFile, listDialogues
from chatbot_interact import respond, CheckForCmd, CheckForExit

# 미연시?
# Basic interaction
# - greeting
# - cmd descs
# - guides.
# - let it speak!  || https://pythonprogramminglanguage.com/text-to-speech/

# + unrelated, but I want to make a MP3 programm. maybe c#, there seem to be
#   some tutorial.


def Main():
    conv = readTalkFile("talks")
    conv2 = readTalkFile("a")
    # print("LISTING DIALOGUES:")
    # listDialogues(conv)
    # listDialogues(conv2)

    while True:
        try:
            userInput = input("[>]")

            while userInput == "":
                userInput = input("[>]")

            if CheckForExit(userInput):
                raise SystemExit

            if CheckForCmd(userInput):  # <--- it
                """If there is command it calls the command."""

            else:
                respond(userInput, conv)
                respond(userInput, conv2)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == '__main__':
    Main()

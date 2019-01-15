from talk_file import ReadTalkFile, ListDialogues
from chatbot_interact import Respond, CheckForCmd, CheckForExit, GetInput

# 미연시?
# Basic interaction
# - guides.
# - let it speak!  || https://pythonprogramminglanguage.com/text-to-speech/

# + unrelated, but I want to make a MP3 programm. maybe c#, there seem to be
#   some tutorial.


def Main():
    printDialogues = True

    fileNames = "b" #"talks","a"
    conversations = tuple(map(ReadTalkFile, fileNames))

    # equivalent of:
    # conversation = []
    # for fileName in fileNames
    #     conversation.append(ReadTalkFile(fileName))
    # conversation = tuple(conversation)

    if printDialogues:
        for conversation in conversations:
            ListDialogues(conversation)

    while True:
        try:
            userInput = GetInput()

            if CheckForExit(userInput):
                raise SystemExit

            if CheckForCmd(userInput):  # <--- it
                """If there is command it calls the command."""

            else:
                for conversation in conversations:
                    Respond(userInput, conversation)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == '__main__':
    Main()

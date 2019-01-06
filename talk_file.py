from dataclasses import dataclass

import re

# to do:
# - white space --> "what is up    "
# - .lower
# - compile
# - improve the line loop
#   something like continue yk


@dataclass
class Conversation:
    """near equivalent of the following code

    class Conversation:

    def __init__(self, heading, dialogues):
        self.heading = heading
        self.dialogues = list(dialogues)
    """
    heading: str
    dialogues: list


@dataclass
class Dialogue:
    """near equivalent of the following code

    class Dialogue:

    def __init__(self, toldPhrases, responses):
        self.tolds = list(toldPhrases)  # whatever
        self.responses = list(responses)
    """
    tolds: list
    responses: list


HEADING_PATTERN = r"( )*#+ .+ #+$( )*"  # --> "# sometext #"

TOLD_PATTERN = r"told(s)?:( )*"
RESPONSE_PATTERN = r"response(s)?:( )*"

ELEMENT_PATTERN = r"    - "

# ELEMENT_PATTERN = r"    -( )?"


def readTalkFile(fileName):
    collectTolds = None
    collectResponses = None

    # probably don't need this but
    # readability and i'm not really bothered
    toldsCollected = None
    responsesCollected = None

    dialogues = []

    # hm
    dialogue = Dialogue([], [])
    dialogues.append(dialogue)

    with open(f"{fileName}.talk", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip("\n")

        # creating new response
        if toldsCollected and responsesCollected:
            dialogue = Dialogue([], [])
            dialogues.append(dialogue)

            toldsCollected = False
            responsesCollected = False

        # excluding comment
        if "//" in line:
            i = line.find("//")
            line = line[:i]
            del i

        # Finding heading
        if re.match(HEADING_PATTERN, line):
            heading = line[2:-2]
            continue

        # Finding Told Phrases
        if re.match(TOLD_PATTERN, line):
            collectTolds = True

        else:
            if collectTolds:
                if re.match(ELEMENT_PATTERN, line):
                    dialogue.tolds.append(line[6:])

                else:
                    collectTolds = False
                    toldsCollected = True

        # Finding Response Phrases
        if re.match(RESPONSE_PATTERN, line):
            collectResponses = True

        else:
            if collectResponses:
                if re.match(ELEMENT_PATTERN, line):
                    dialogue.responses.append(line[6:])

                else:
                    collectResponses = False
                    responsesCollected = True

    return Conversation(heading, dialogues)


def listDialogues(aConversatoin):
    dialogues = aConversatoin.dialogues
    print(len(dialogues), "dialogues found.")

    for i, dialogue in enumerate(dialogues):
        print()
        print(f"- {i+1} - ")
        print("tolds:      ", dialogue.tolds)
        print("responses:  ", dialogue.responses)
        print()


if __name__ == '__main__':
    listDialogues(readTalkFile("talks"))

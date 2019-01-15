from dataclasses import dataclass

import re

# fun idea!
# improve battleships
# and use some famous 3rd party apps
# to show how many times I won, lose
# and save data
# varaiety of ships

# to do:
# - multi reading
# - what about !!! ???? all that?
#       - duplicate?
#          like if there's 'a?'-> 'a' & 'a?'
# - special option to capitalise
# - remember user's information
#
# - compile ?
# - improve the loop
#       - continue
#       - The extra looking variables you know
#
# - repeated dialogue? like 'your name' and 'yo' ?
# - using somewhat equivalent of f-string and regex

@dataclass
class Conversation:
    archive = dict()

    def __init__(self, heading, dialogues):
        self.heading = heading
        self.dialogues = dialogues
        Conversation.archive[self.heading] = self

    def __repr__(self):
        reprText = f"Conversation({self.heading}, {self.dialogues}) "

        i = 200

        if len(reprText) > i:
            reprText = reprText[:i-3] + "..."

        return  reprText


@dataclass
class Dialogue:
    tolds: list
    responses: list


def abbreviation():
    """
    // - change all abbreviation to norm (like 's -> is)
    //      - smart abbreviation haddle
    //          - create multiple responses?
    //          - let human decide?
    //          - MAGICAL DATA SCIENCE?
    """


HEADING_PATTERN = r"#+ .+ #"  # --> "# sometext #"

TOLD_PATTERN = r"told(s)?:"
RESPONSE_PATTERN = r"response(s)?:"

ELEMENT_PATTERN = r".*-( )?"


def HandleRegexChars():
    """Something like () -> \\(\\)"""


def ReadTalkFile(fileName):
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
        line = line.strip().lower()

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
                elementMatch = re.match(ELEMENT_PATTERN, line)
                if elementMatch:
                    dialogue.tolds.append(line[elementMatch.end():])

                else:
                    collectTolds = False
                    toldsCollected = True

        # Finding Response Phrases
        if re.match(RESPONSE_PATTERN, line):
            collectResponses = True

        else:
            if collectResponses:
                elementMatch = re.match(ELEMENT_PATTERN, line)
                if elementMatch:
                    dialogue.responses.append(line[elementMatch.end():])

                else:
                    collectResponses = False
                    responsesCollected = True

    return Conversation(heading, dialogues)


def ListDialogues(aConversatoin):
    dialogues = aConversatoin.dialogues
    print(len(dialogues), "dialogues found.")

    for i, dialogue in enumerate(dialogues):
        print()
        print(f"- {i+1} - ")
        print("tolds:      ", dialogue.tolds)
        print("responses:  ", dialogue.responses)
        print()


def MergeConversations(heading, *conversations):
    # __add__ ??
    # Merge++:
    # - no duplicate
    # - name
    # - MergeTo
    mergedConv = Conversation(heading, [])

    for conv in conversations:
        if isinstance(conv, str):
            conv = Conversation.archive[conv]

        mergedConv.dialogues.extend(conv.dialogues)


if __name__ == '__main__':
    a = ReadTalkFile("talks")
    b = ReadTalkFile("talks")
    assert(a == b)
    ListDialogues(c)

    MergeConversations

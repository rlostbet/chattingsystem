import re
import random
import os

from myTool import Line


def respond(userInput, Conversation, botName="BOT"):

    for dialogue in Conversation.dialogues:
        tolds = tuple(dialogue.tolds)
        responses = tuple(dialogue.responses)

        for told in tolds:
            if re.search(told, userInput):
                # print(told)
                print(f"{botName}: {random.choice(responses)}")


def CheckForExit(userInput):
    # "e" is such a common char you may enter by mistake
    exitKeyWords = ("exit", "quit", "exit()", "quit()", "q")

    for keywords in exitKeyWords:
        if re.match(keywords, userInput):  # not search yk.
            return True

    return False


winCmds = (
    "cd",
    "cd..",
    "cls",
    "tree",
    "find",
    "exit"
    # "shutdown"
)


def UseWindowTerminal(cmd, parameter=None):
    """Use Window Cmd"""
    if parameter is None:
        parameter = ""

    os.system(cmd + " " + parameter)

# def UseWindowTerminal(cmd, parameter=None):
#     """Use Window Cmd"""
#     if cmd in winCmds:
#         if parameter is not None:
#             os.system(cmd + " " + parameter)

#         else:
#             os.system(cmd)

#     else:
#         Line()
#         print(" - wrong window command")
#         Line()


def WinHelp():
    for i, cmd in enumerate(winCmds):
        print(f"{i + 1}. {cmd}")


def Help():
    """describes Basic Commands"""
    descs = (
        "\nHELP\n"
        "---------------------------------\n"
        "line       draws a Line\n"
        "help       describe commands\n"
        "winHelp    display a list of win\n"
        "           -dow Commands\n"
        "---------------------------------\n"
    )
    print(descs)


basicCmds = {
    "line": Line,
    "winHelp": WinHelp,
    "help": Help
}


def FindCmd(cmdName, cmdDict=basicCmds):
    if cmdName in cmdDict:
        return basicCmds.get(cmdName, None)

    else:
        Line()
        print(" - Command Not Found")
        Line()


def CheckForCmd(userInput):
    userInput = userInput.split()

    parameter = " ".join(userInput[2:]) if len(userInput) > 2 else None

    if userInput[0] in ("w>", "win>"):
        wCmd = userInput[1]
        UseWindowTerminal(wCmd, parameter)

    elif userInput[0] == ">":
        cmd = FindCmd(userInput[1])

        if cmd is not None:
            if len(userInput) == 2:
                cmd()

            else:
                cmd(parameter)

    else:
        return False

    return True

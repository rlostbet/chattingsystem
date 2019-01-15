import os
from myTool import Line, rLine

winCmds = (
    "cd",
    "cd..",
    "cls",
    "tree",
    "find",
    "exit"
    #"shutdown"
)


def UseWindowTerminal(cmd, parameter=None):
    """Use Window Cmd"""
    if cmd in winCmds:
        if parameter is not None:
            os.system(cmd + " " + parameter)

        else:
            os.system(cmd)

    else:
        Line()
        print(" - wrong window command")
        Line()


def WinHelp():
    for i, cmd in enumerate(winCmds):
        print(f"{i + 1}. {cmd}")

basicCmds = {
    "line": Line,
    "winHelp": WinHelp
    # "help" : describe Basic Commands
}


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


basicCmds["help"] = Help


def FindCmd(cmdName, cmdDict=basicCmds):
    if cmdName not in cmdDict:
        Line()
        print(" - Command Not Found")
        Line()
        # raise Err ?
    else:
        return basicCmds.get(cmdName, None)


def CheckForCmd(words):
    isCmd = None
    parameter = " ".join(words[2:]) if len(words) > 2 else None

    if words[0] in ("w>", "win>"):
        isCmd = True

        wCmd = words[1]
        UseWindowTerminal(wCmd, parameter)

    elif words[0] == ">":
        isCmd = True

        cmd = FindCmd(words[1])

        if cmd is not None:

            if len(words) == 2:
                cmd()

            else:
                cmd(parameter)

    else:
        isCmd = False

    return isCmd

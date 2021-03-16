# -*- coding: utf-8 -*-
"""
Created on Tue Mar  16 14:39:03 2021

@author: dyncoch
"""
class Colors:
    """
    Colors code from: https://pkg.go.dev/github.com/whitedevops/colors
    """
    ResetAll = "\033[0m"

    Bold = "\033[1m"
    Dim = "\033[2m"
    Italics = "\033[3m"
    Underlined = "\033[4m"
    Blink = "\033[5m"
    Reverse = "\033[7m"
    Hidden = "\033[8m"
    CrossedOut = "\033[9m"

    ResetBold = "\033[21m"
    ResetDim = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink = "\033[25m"
    ResetReverse = "\033[27m"
    ResetHidden = "\033[28m"

    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"

    BackgroundDefault = "\033[49m"
    BackgroundBlack = "\033[40m"
    BackgroundRed = "\033[41m"
    BackgroundGreen = "\033[42m"
    BackgroundYellow = "\033[43m"
    BackgroundBlue = "\033[44m"
    BackgroundMagenta = "\033[45m"
    BackgroundCyan = "\033[46m"
    BackgroundLightGray = "\033[47m"
    BackgroundDarkGray = "\033[100m"
    BackgroundLightRed = "\033[101m"
    BackgroundLightGreen = "\033[102m"
    BackgroundLightYellow = "\033[103m"
    BackgroundLightBlue = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan = "\033[106m"
    BackgroundWhite = "\033[107m"


def create_styled_text(text: str, *styles: Colors) -> str:
    """
    Creates a multiple styled text with styles passed.

    :param text: text to be colored
    :type text: str
    :param styles: constant styles
    :type styles: str

    :return: text colored
    """
    style = ''.join(map(str, styles))
    return f"{style}{text}{Colors.ResetAll}"


def create_colored_text(text: str, color: Colors) -> str:
    """
    Creates a colored text with color passed.

    :param text: text to be colored
    :type text: str
    :param color: constant styles
    :type color: Colors

    :return: text colored
    """
    return create_styled_text(text, color)


def create_error_msg(msg: str) -> str:
    """
    Creates a red colored message.

    :param msg: message to be colored in red
    :type msg: str

    :return: message colored in red
    :rtype: str
    """
    return create_styled_text(msg, Colors.White, Colors.Bold, Colors.BackgroundRed)


def create_warning_msg(msg: str) -> str:
    """
    Creates a yellow colored message.

    :param msg: message to be colored in red
    :type msg: str

    :return: message colored in yellow
    :rtype: str
    """
    return create_styled_text(msg, Colors.Black, Colors.Italics, Colors.BackgroundYellow)


if __name__ == "__main__":
    print(create_styled_text("This is a styled text", Colors.BackgroundGreen, Colors.Bold, Colors.Black,
                             Colors.Underlined))
    print(create_error_msg("This is an error message"))
    print(create_warning_msg("This is a warning message"))

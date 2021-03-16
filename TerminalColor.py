# -*- coding: utf-8 -*-
"""
Created on Tue Mar  16 14:39:03 2021

@author: dyncoch
"""

LIGHT_MAGENTA: str = '\033[95m'
LIGHT_BLUE = '\033[94m'
LIGHT_YELLOW = '\033[93m'
LIGHT_RED = '\033[91m'
RED = '\033[31m'
RESET_ALL = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def create_colored_text(text, *styles):
    """
    Creates a colored text with styles passed.

    :param text: text to be colored
    :type text: str
    :param styles: constant styles
    :type styles: str

    :return: text colored
    """
    style = ''.join(map(str, styles))
    return f"{style}{text}{RESET_ALL}"


def create_error_msg(msg: str):
    """
    Creates a red colored message.

    :param msg: message to be colored in red
    :type msg: str

    :return: message colored in red
    """
    return f"{RED}{msg}{RESET_ALL}"

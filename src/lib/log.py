# RKBD
# Remote keyboard in python
# GitHub: https://www.github.com/lewisevans2007/rkbd
# Licence: GNU General Public License v3.0
# By: Lewis Evans

from colorama import Fore, Back, Style


def log(msg):
    print("[" + Fore.CYAN+ "*" + Style.RESET_ALL + "] " + msg)


def success(msg):
    print("[" + Fore.GREEN + "+" + Style.RESET_ALL + "] " + msg)


def error(msg):
    print("[" + Fore.RED + "x" + Style.RESET_ALL + "] " + msg)


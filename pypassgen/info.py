from termcolor import *
import sys

global verbose
verbose = False

def info(string):
    text = colored('[INFO]:', 'grey', 'on_white', attrs=['bold'])
    print(text + " " + string);

def error(string, exit_code=1):
    text = colored('[ERROR]:', 'red', attrs=['bold'])
    print(text + " " + string)
    verbose_info("Exciting due to an error, exit code " + str(exit_code))
    sys.exit(exit_code) 

def warning(string):
    text = colored('[WARNING]:', 'red', attrs=['blink'])
    print(text + " " + string)

def verbose_warning(string):
    if verbose == True:
        warning(string)

def verbose_info(string):
    if verbose == True:
        info(string)

def verbose_is_true():
    global verbose
    verbose = True

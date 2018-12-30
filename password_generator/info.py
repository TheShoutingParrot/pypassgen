
#This file contains all the info giving functions in this program. Such as info(), warning(), error()

import main

def info(string):
    text = main.colored('[INFO]:', 'grey', 'on_white', attrs=['bold'])
    print(text + " " + string);

def verbose_info(string):
    if main.verbose == True:
        info(string)

def error(string, exit_code=1):
    text = main.colored('[ERROR]:', 'red', attrs=['bold'])
    print(text + " " + string)
    verbose_info("Exciting due to an error, exit code " + str(exit_code))
    main.sys.exit(exit_code) 

def warning(string):
    text = main.colored('[WARNING]:', 'red', attrs=['blink'])
    print(text + " " + string)

def verbose_warning(string):
    if main.verbose == True:
        warning(string)

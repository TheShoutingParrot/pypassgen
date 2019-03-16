import sys, getopt 
from termcolor import colored
from .password import *
from .info import *


def main():

    argv = sys.argv[1:]

    chars   = ''
    words   = True
    l       = None

    human_readable = False

    try:
        opts, args = getopt.getopt(argv, "hc:w:l:", ["chars=", "words=", "length=", "verbose", "help", "human-readable"])

    except getopt.GetoptError:
        error("Command line syntax error. For help on the usage/command line arguments run: foo.py -h", 2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            info("\nUsage: pypassgen -c <chars> -w <words> -l <length>\n" +
                    "Options: -c/--chars -w/--words -l/--length\n\n" +
                    "The <chars> are the characters to select from, for the password.\n" +
                    "Options for <chars>:\n" +
                    "-all:      A-Z, 0-9, special characters (such as: !, &, %, etc) [DEFAULT]\n" +
                    "-az:       A-Z only\n" +
                    "-09:       0-9 only\n" +
                    "-sp:       Special characters only\n" +
                    "-az09:     A-Z and 0-9\n" +
                    "-azsp:     A-Z and special characters\n" +
                    "-09sp:     0-9 and special characters\n" +
                    "-none:     No chars (outside of words).\n\n" +
                    "The <words> option is the option if words are included or not.\n" +
                    "Options for <words>:\n" +
                    "-yes:      Include words in password. The chars setting doesn't effect this option,\n" +
                    "            so if you set your <chars> to 09 the words will still use A-Z characters). [DEFAULT]\n" + 
                    "-no:       No words included\n\n" +
                    "The <length> is a value that is the length of the password. If 0 is set then the program will default to 10\n\n" +
                    "Verbose usage: pypassgen -c <chars> -w <words> -l <length> --verbose\n" +
                    "Verbose gives you more info then needed. Usually verbose tells you much more then you need, \n" +
                    "it's mainly used for debugging. If you want to report a issue, putting verbose will help the developers.\n\n" +
                    "--human-readable makes the password more human readable.\n")

            sys.exit(0)

        elif opt == "--verbose":
            verbose_is_true()

        elif opt == "--human-readable":
            human_readable = True

        elif opt in ("-c", "--chars"):
            chars = arg.lower()

        elif opt in ("-w", "--words"):
            if arg.lower() in ('no', 'n'):
                words = False

            elif arg.lower() in ('yes', 'y'):
                words = True

            else:
                error("Invalid option", 2);

        elif opt in ("-l", "--length"):
            try:
                l = int(arg)
            except:
                error("Command line syntax error. The length inputed is not a interger...", 2)


    if chars == '':
        verbose_warning("The chars weren't specified...")
        chars = 'all'
        verbose_info("Chars were changed to the default (all)...")

    if l == None:
        verbose_warning("No length defined...")
        l = 16
        verbose_info("The length was automically set to 15, because there was no length specified...")

    elif l < 1:
        error("Command line syntax error... The length inputed was under 1...")

    password = colored(create_password(set_up_chars(chars), words, l, human_readable), 'white', attrs=["bold"])
    print(password)

    sys.exit(0)

if __name__ == "__main__":
    main()

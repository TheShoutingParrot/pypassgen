from __main__ import *
from .info import *

import random

def set_up_chars(c):
    az = "abcdefghijklmnopqrstuvwxyz"
    az += az.upper()

    n = "0123456789"
    sp = "!\"#¤&/()=?£$€§|<>-_.:,;~*' "

    if c.lower() == 'all':
        return az + n + sp

    elif c.lower() == 'none':
        return ''

    elif c.lower() == 'az': 
        return az

    elif c.lower() == '09':
        return n

    elif c.lower() == 'sp':
        return sp

    elif c.lower() == 'az09':
        return az + n

    elif c.lower() == 'azsp':
        return az + sp

    elif c.lower() == '09sp':
        return n + sp

    else:
        verbose_warning("The chars option was invalid...")
        verbose_info("Changing to default (all)...")
        return az + n + sp 

def rand_chars(c, l):
    x = random.randint(0, round(l/2))
    s = ''
    for i in range(x):
        s += c[random.randint(0, len(c) - 1)]

    return s
        
def rand_word(l):
    # Some of the words here are from https://randomword.com... That is why some words are weird...
    w0 = ["word", "rust", "linux", "gnu", "foo", "hello", "love", "snow", "zoo", "truck", "elon", "musk", "nasa",
            "time", "goo", "grape", "by", "the", "way", "I", "use", "arch", "ufo", "dog", "bad", "good", "the",
            "ugly", "for", "god", "grunt", "ape", "food", "root", "boot", "loot", "duck", "go", "bit", "run", "rub",
            "gun", "sum", "math", "bavian"]
    w1 = ["password", "programmer", "secure", "kilometer", "stallman", "universe", "shadow", "something", "bowman", 
            "python", "odyssey", "adventure", "mathematical", "surgery", "language", "dummies", "summary", "daysure",
            "omnigatherum", "miscellaneous", "collection", "antechinus", "argentocracy", "knickerbockers", "nutarian",
            "factualism", "pluviometer", "parasitaster", "curmurring", "obedientiary", "embryogenesis", "kymatology"]


    if l > 15:  
        w = w0 + w1
    else:       
        w = w0

    s = w[random.randint(0, len(w) - 1)]

    for i in range(len(s)):
        x = random.randint(0, 1)
        if x == 0:
            s = list(s)
            s[i] = s[i].upper()
            s = ''.join(s)

    return s

def create_password(c, w, l):
    password = ''

    verbose_info("Starting password generation...")

    if l < 10:
        verbose_warning("All passwords under 10 chars are very weak (even 10 is very weak). I dont recommend using a password this short...")

    if l == 1:
        if c == '':
            verbose_warning("Unable to create password, because there were no characters to use and the length was too short...")
            error("Unable to create password...", 1)
        verbose_warning("The password length is set to 1, not good...")
        verbose_info("Due to the short length the normal process wont work, the program will select a random char from the chars list...")

        try:
            return c[random.randint(0,len(c))]
        except:
            verbose_warning("Unable to create password, reason unknown...")
            error("Unable to create password...", 1)

    if c == '':
        if w == True:
            while True:
                password += rand_word(l)
                if len(password) >= l:
                    break
            return password[:l]
        else:
            warning("No characters or words to generate password with...")
            verbose_info("This is most likely because 'none' was selected with chars, and 'no words' was selected...")

            info("Due to this exiting...")
            verbose_info("Exiting with exit code 0...")
            sys.exit(0)
    
    if w == True:
        while True:
            x = random.randint(0, 1)

            if x == 0:
                password += rand_chars(c, l)

            else:
                password += rand_word(l)
            
            if len(password) >= l:
                break

        password = password[:l]

    else:
        for i in range(l):
            password += c[random.randint(0, len(c) - 1)]

    verbose_info("Password generation succesfull...")

    return password
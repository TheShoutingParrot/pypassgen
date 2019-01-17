from __main__ import *
from .info import *

import random

def set_up_chars(c):
    az = "abcdefghijklmnopqrstuvwxyz"
    az += az.upper()

    chars = ''

    n = "0123456789"
    sp = "!\"#¤&/()=?£$€§|<>-_.:,;~*' "


    if c.lower() == 'all':
        return az + n + sp

    elif c.lower() == 'none':
        return ''

    if 'az' in c.lower(): 
        chars += az

    if '09' in c.lower():
        chars +=  n

    if 'sp' in c.lower():
        chars +=  sp

    if chars == '':
        verbose_warning("The chars option was invalid...")
        verbose_info("Changing to default (all)...")
        return az + n + sp 

    verbose_info("The characters that are gonna be used are: " + chars)
    return chars

def rand_chars(c, l):
    x = random.randint(0, round(l/2))
    s = ''
    for i in range(x):
        s += c[random.randint(0, len(c) - 1)]

    return s
        
def rand_word(l):
    # Some of the words here are from https://randomword.com... That is why some words are weird...
    short_w = ["word", "rust", "linux", "gnu", "foo", "hello", "love", "snow", "zoo", "truck", "elon", "musk", "nasa",
            "time", "goo", "grape", "by", "the", "way",  "use", "arch", "ufo", "dog", "bad", "good", "the",
            "ugly", "for", "god", "grunt", "ape", "food", "root", "boot", "loot", "duck", "go", "bit", "run", "rub",
            "gun", "sum", "math", "bavian", "xmas", "new", "year", "dice"]

    long_w = ["password", "programmer", "secure", "kilometer", "stallman", "universe", "shadow", "something", "bowman", 
            "python", "odyssey", "adventure", "mathematical", "surgery", "language", "dummies", "summary", "daysure",
            "omnigatherum", "miscellaneous", "collection", "antechinus", "argentocracy", "nutarian", "factualism", 
            "pluviometer", "parasitaster", "curmurring", "obedientiary", "embryogenesis", "kymatology", "christmas"]


    if l > 15:  
        w = short_w + long_w
    else:       
        w = short_w

    s = w[random.randint(0, len(w) - 1)]

    #This "dice" tells the program whether to just keep the word as it is, make the first letter
    #upper case, or just to go through the words letters and randomly make some of the letters uppercase.
    x = random.randint(0,6)

    if x == 0:
        return s

    elif x == 1:
        s = list(s)
        s[0] = s[0].upper()
        s = ''.join(s)

    else:
        
        #This for loop goes through the chosen (random) word, and replaces some of the letters with uppercase letters.
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
            error("No charaters or words to generate password with.", 1)
    
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

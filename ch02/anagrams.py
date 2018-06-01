#!/bin/python3

import math
import os
import random
import re
import sys


def anagrams(str1, str2):
    lst_str1 = list(str1)
    lst_str2 = list(str2)

    letters_keep = []
    print("Length of string 1 ", len(str1))
    print("Length of string 2 ", len(str2))
    for i in lst_str1:
        print(i)
        try:
            idx = lst_str2.index(i)
            print(idx)
            lst_str2.pop(idx)
            letters_keep.append(i)
            print(letters_keep)
        except:
            pass
    letters_to_remove = len(str1) + len(str2) - (2 * len(letters_keep))
    print(letters_keep)
    print(len(letters_keep))
    print(letters_to_remove)


if __name__ == '__main__':
    a = input()
    b = input()
    print(type(a))
    print(type(b))
    anagrams(a, b)


# fails for
# fcrxzwscanmligyxyvym
# jxwtrhvujlmrpdoqbisbwhmgpmeoke
# output 30

# and

# bugexikjevtubidpulaelsbcqlupwetzyzdvjphn
# lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk
# output 40
# and

# fsqoiaidfaukvngpsugszsnseskicpejjvytviya
# ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget
# output 42

# and

# imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesf
# xkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln
# output 102
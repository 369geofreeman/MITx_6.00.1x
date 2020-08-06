# monkey theorem


# Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
# 
# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.
# 
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.
# 
# Self Check Challenge
# 
# See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one._

import string
import random

alph = string.ascii_lowercase + '  '



def randLetters():
    return ''.join(random.choices(alph, k=28))


def isMatch(count, target, prevRes):
    if count % 10 == 0:
        print('Best guess so far is {} with {:.2f}% correct.'.format(prevRes, len(prevRes.replace(' ', ''))/28))
    return prevRes == target


def startMachine():
    target = "methinks it is like a weasel"
    count = 0
    prevRes = [' ']*28

    while True:
        count += 1
        newLetters = randLetters()
        for i,v in enumerate(newLetters):
            if v in target and target[i] != prevRes[i]:
                prevRes[i] = v
        if isMatch(count, target,"".join(prevRes)):
            break

    return "Phew! Found '{}' after {} tries!".format(target,count)


print(startMachine())



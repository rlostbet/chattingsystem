1.
def GetWords(charToReplace=()):
    """get input from the user"""

    userInput = input("[>] ").split()

    # no empty input
    while userInput == []:
        userInput = input("[>] ").split()

    for i in range(len(userInput)):
        for char in charToReplace:
            userInput[i] = userInput[i].replace(char, "")

    return userInput

2.
import os
import ranom

import myFile
import phraseHandling as phr

BOTNAME = "BOTY1"

# Load Saved File of User's properties(?)
if os.path.exists(myFile.FOLDER_PATH + "/USER_PROPERTIES.txt"):
    userProperties = dict(eval(myFile.Load("USER_PROPERTIES")))

else:
    userProperties = dict()
    myFile.Save(userProperties, "USER_PROPERTIES", "w")


def updateUserProperties(words):
    myFile.Save(userProperties, "USER_PROPERTIES", "w")

# respondSequence =  []

'''
# THE PERSONALITY OF CHATBOT:
# - female
# - tiny fairy
# - crazy
'''

reflections = {
    # https://towardsdatascience.com/build-your-first-chatbot-using-python-nltk-5d07b027e727
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"

}

abbreviation = {
    "I've": "I have",
    "I'm": "I am",
    "gonna": "going to",
    "are": "'re"
}


# https://apps.worldwritable.com/tutorials/chatbot/


def RespondForGreeting(words):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    # - multiple words
    # - nasty function..
    keyPhrases = ["hello", "hi", "hai", "how are you",
                  "what's up", "how's it going", "greetings", "sup", "hey"]
    response = ["Sup", "Hai", "Hello", "G'day", "Hey"]

    if phr.IsOneOfThePhrases(words, keyPhrases):
        print(random.choice(response))
        respondSequence.remove(RespondForGreeting)


def ExchangeName(words):
    global userName, userProperties
    """Bot exchange name with the user"""
    keyPhrases = ["my name is", "my name,"]
    response = ["my name is"]

    userInquireKeys = ["Do you know my name", "know my name", "I ask you my name"]

    # ending point of the matching phrase
    endingPoint = phr.FindEndingPoint(words, keyPhrases)

    if phr.IsOneOfThePhrases(words, userInquireKeys):
        print("Your name is {} !! right? :>".format(userProperties["USER_NAME"]))

    elif endingPoint is not None:
        userName = words[endingPoint + 1].capitalize()

        print(f"Got it! your name is {userName}!")

        print(random.choice(response) + " " + BOTNAME)
        userProperties["USER_NAME"] = userName


def addUserProperty(words, propertyName, keyPhrases, response=[]):
    """saves a property of the user"""
    global username, userProperties

    # ending point of the matching phrase
    endingPoint = phr.FindEndingPoint(words, keyPhrases)

    if endingPoint is not None:
        userProperties[propertyName] = words[endingPoint + 1].capitalize()
        print(random.choice(response) + userProperties(propertyName))


def ExchangeBirthday(words):
    propertyName = "USER_BIRTHDAY"
    keyPhrases = ["my birthday is", "my birth day is", "my birthday,", "my birth day,"]
    response = ["Got it", "I will remember your birthday"]
    addUserProperty(words, propertyName, keyPhrases, response)


def SaveVocab():
    myFile.Save(str(abbreviation), "abbreviation")
    myFile.Save(str(reflections), "reflections")


respondSequence = [RespondForGreeting, ExchangeName, ExchangeBirthday, updateUserProperties]


def Main():
    SaveVocab()

if __name__ == '__main__':
    Main()
import re

abbreviation = {
    "'ve": "have"
    "'s": "is"  # or has..
    "'m": "am"
    "gonna": "going to",
    "'re": "'are"
}

# user Re library to replace all abreviation.


def IsOneOfThePhrases(words, phrases):
    """find out if words contain one of the phrases"""
    IsOneOfThePhrases = False

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    IsOneOfThePhrases = True

    return IsOneOfThePhrases


def FindMatchingPhrases(words, phrases):
    """find the matching phrase"""
    matchingPhrase = None

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    matchingPhrase = candidateWords

    return matchingPhrase


def FindStartingPoint(words, phrases):
    """Find the phrase's starting point in words"""
    matchingPhrase = None

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    return j


def FindEndingPoint(words, phrases):
    """Find the phrase's ending point in words"""
    matchingPhrase = None

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    return j + len(phrase) - 1

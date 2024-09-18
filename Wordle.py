import random
wordbank = ["apple", "grape", "flint", "grain", "table", "chair", "music", "plant"]
def Randomword():
    return random.choice(wordbank)
def validateguess(guess):
    if len(guess) != 5:
        return "Not enough letters" if len(guess) < 5 else "Only 5-letter words"
    if not guess.isalpha():
        return "Letters only"
    return None
def Feedback(secretword, guess):
    feedback = ""
    for secretletter, guessedletter in zip(secretword, guess):
        if secretletter == guessedletter:
            feedback += "🤢"  
        elif guessedletter in secretword:
            feedback += "🍊"  
        else:
            feedback += "🗿" 
    return feedback
def Wordle():
    secretword = Randomword()
    print("Welcome to Wordle! You have 6 chances to guess a 5-letter word.")
    for attempt in range(1, 7):
        guess = input("Attempt {}/6: ").lower()
        validationresult = validateguess(guess)
        if validationresult:
            print(validationresult)
            continue
        feedback = Feedback(secretword, guess)
        print(feedback)
        if guess == secretword:
            print("Congratulations! You guessed '{}' correctly.".format(secretword))
            break
    else:
        print("Unfortunate! The word was '{}'.".format(secretword))
if __name__ == "__main__":
    Wordle()

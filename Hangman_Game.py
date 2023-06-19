import random
word=["Apple","Baboon","Monkey"]
choosen_Word=random.choice(word)
print(choosen_Word)
guess=input("Enter the word:").lower()
for letters in choosen_Word:
    if guess==letters:
        print("Right")
    else:
        print("Wrong")
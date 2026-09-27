import random


print("word scramble")
words = ("python", "apple", "juice", "fruit", "milk")
word = random.choice (words)

for word in words:
  scrambled = "".join(random.sample(word,len(word)))
  print(f"guess this word:{scrambled}")
  guess = input("guess the word attempts{1/3}:").lower()

  if guess == words:
    print("correct you win")

  else:
    attempts = 2
    while attempts <= 3:
      print("wrong answer")
      guess = input(f"guess the word attempts {attempts}/3:").lower()
      if guess == word:
         print("finally correct")
         break
      else:
        print("try again")
        attempts = attempts + 1

  if attempts == 4 and guess != word:
    print("game over")
    print("the correct word was:", word)
    break
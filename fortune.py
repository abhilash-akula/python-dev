import random

fortune_number = random.randint(1,100)
random_number = random.randint(1,3)
if random_number == 1:
  fortune_text = "You will be a Hero"
if random_number == 2:
  fortune_text = "You are Kind"
if random_number == 3:
  fortune_text = "You are Honest"

print(f"{fortune_text}, your fortune number is {fortune_number}")
print("{}, your fortune number is {}".format(fortune_text, fortune_number))



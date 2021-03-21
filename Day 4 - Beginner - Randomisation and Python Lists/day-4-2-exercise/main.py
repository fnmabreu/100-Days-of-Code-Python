# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

num_items = len(names)
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

# or using
# random_choice = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")


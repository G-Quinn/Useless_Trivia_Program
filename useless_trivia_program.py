# Useless Trivia
#
# Get Personal information from the user and then
# prints true but useless informtion about them

#Varibles
name =input ("Hi. What's your name?")

age=int(input("How old are you?"))

weight= int(input("Okay, last question. How many pounds do you weight? "))

called = name * 5

seconds = age * 365 * 24 * 60 * 60


moon_weight = weight / 6

sun_weight = weight * 27.1

#Code Start
print("\nIf poet ee cummings were to email you, he'd address you as.",
      name.lower())


print("\nIf ee cummings were mad , he'd call you.",
      name.upper())
  


print("\nIf  a small child were trying to get your attention.")

print( "Your name would become:")
print(called)

print("\nYou're over", seconds, "seconds old.")

print("\nDid you know that on the moon you would weigh only", moon_weight, "pounds?")

print("\nOn the sun, you'd weigh", sun_weight, "pounds ? (but, ah.... not for long).")








input ("\n\nPress the enter key to exit.")

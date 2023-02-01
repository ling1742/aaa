cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
   if car == 'bmw':
      print(car.upper())
   else:
      print(car.title())



age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)


age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 19
if age >= 18:
  print("\nYou are old enough to vote!")

age = 17
if age >= 18:
 print("You are old enough to vote!")
 print("Have you registered to vote yet?")
else:
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")







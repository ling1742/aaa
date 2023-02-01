magicians=['alice','david','carolina']
for magician in range(5):
    print(magician)



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")

number=list(range(1,6))
print(number)

num=[]
for value in range(1,11):
    num.append(value**2)
print(num)

dit=[1,2,3,4,5,6,7,8,9,10]
print(max(dit))
print(min(dit))
print(sum(dit))

squares = [value**2 for value in range(1, 11)]
print(squares)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 50)
dimensions[0] = 250
print(dimensions)
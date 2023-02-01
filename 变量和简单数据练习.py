
"1.用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单，下面是一个例子。"

name="ling"
text="would you like to learn some Python today?"
result=f"Hello {name.title()},{text}"
print(result)


"2.用变量表示一个人的名字，再以小写、大写和首字母大写的方式显示这个人名。"

name="ling"
print(name.title())
print(name.upper())
print(name.lower())


"3.找一句你钦佩的名人说的名言，将其姓名和名言打印出来。输出应类似于下面这样（包括引号）。"

print("马尔克斯 说过：”生命曾经有过的所有灿烂，终究都需要用寂寞来偿还“.")


"4.重复练习3，但用变量famous_person表示名人的姓名，再创建要显示的消息并将其赋给变量message，然后打印这条消息。"

famous_person="马尔克斯"
message="生命中曾经有过的所有灿烂，终究都需要用寂寞来偿还"
print(f"{famous_person} 说过：“{message}.”")


"5.　用变量表示一个人的名字，" \
"并在其开头和末尾都包含一些空白字符。" \
"务必至少使用字符组合\t和\n各一次。" \
"打印这个人名，显示其开头和末尾的空白。" \
"然后，分别使用剔除函数lstrip()、rstrip()和strip()对人名进行处理，" \
"并将结果打印出来。"

my_name="ling"
print(f"\t{my_name}\t\n")
my_name_1="      ling        "
print(my_name_1.rstrip())
print(my_name_1.lstrip())
print(my_name_1.strip())


"6.编写四个表达式，分别使用加法、减法、乘法和除法运算，但结果都是数字8。"

print(1*8)
print(3+5)
print(9-1)
print(8/1)


"7.练习2-9：最喜欢的数　" \
"用一个变量来表示你最喜欢的数，" \
"再使用这个变量创建一条消息，" \
"指出你最喜欢的数是什么，" \
"然后将这条消息打印出来。"

number=520
like="我最喜欢的数字"
print(like+"是：%s"%number)

"8.练习2-11：Python之禅　" \
"在Python终端会话中执行命令import this，" \
"并粗略地浏览一下其他的指导原则。"

import this


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print(motorcycles.pop())
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)




print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print(len(cars))
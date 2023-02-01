"1.　将一些朋友的姓名存储在一个列表中，"\
"并将其命名为names。"\
"依次访问该列表中的每个元素，"\
"从而将每个朋友的姓名打印出来。"

names=["lxc","xjx","lmh","wxl","xy"]
print(names[0])
print(names[1])
print(names[2])
print(names[-2])
print(names[-1])


"2.继续使用练习1中的列表，" \
"但不打印每个朋友的姓名，" \
"而为每人打印一条消息。" \
"每条消息都包含相同的问候语，" \
"但抬头为相应朋友的姓名。"

names=["lxc","xjx","lmh","wxl","xy"]
message="你好"
print(names[0],message)
print(names[1],message)
print(names[2],message)
print(names[-2],message)
print(names[-1],message)


"3.自己的列表　想想你喜欢的通勤方式，" \
"如骑摩托车或开汽车，" \
"并创建一个包含多种通勤方式的列表。" \
"根据该列表打印一系列有关这些通勤方式的宣言。"

vehicle=["car","bike","taxi"]
print("I\twould\tlike\tto  \town \ta\t",vehicle[1])



"4.如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），" \
"你会邀请哪些人？请创建一个列表，" \
"其中包含至少三个你想邀请的人，" \
"然后使用这个列表打印消息，" \
"邀请这些人来与你共进晚餐"

list=["lxc","xjx","lmh","xy"]
print(list)


"5.你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。"

list[0]="lhm"
print(list)

"6.添加嘉宾　你刚找到了一个更大的餐桌，" \
"可容纳更多的嘉宾。" \
"请想想你还想邀请哪三位嘉宾。"

list.append("lxm")
list.append("wxl")
list.append("wyh")
print(list)

"6.1使用insert()将一位新嘉宾添加到名单开头。"

list.insert(0,"ff")
print(list)

"6.2使用insert()将另一位新嘉宾添加到名单中间。"

list.insert(4,"ff")
print(list)


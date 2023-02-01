"4.1　想出至少三种你喜欢的比萨，"\
"将其名称存储在一个列表中，再使用for"\
"循环将每种比萨的名称打印出来"

pz=['Chicken Orleans','Super supreme','Durian']
for psz in pz:
    print(psz)
for pzs in pz:

    print(f'l\tlike\t{pzs.title()}\tpizza\t!')
else:
    print("\nl\treally\tlove\tpizza\t!")

"4.2　使用一个for 循环打印数1～20（含）。"

num=[value for value in range(1,21)]
print(num)

"4.3　创建一个包含数1～1 000 000的列表，再使用一个for 循环将这些数打印出来。"

nums=[value for value in range(1,1000001)]
print(nums)

"4.4创建一个包含数1～1 000 000的列表，再使用min()"\
"和max() 核实该列表确实是从1开始、到1 000 000结束的。另外，对这个列表"\
"调用函数sum() ，看看Python将一百万个数相加需要多长时间。"

nums=[value for value in range(1,1000001)]
print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))

"4.5通过给函数range() 指定第三个参数来创建一个列表，其中"\
"包含1～20的奇数，再使用一个for 循环将这些数打印出来。"

js=[value for value in range(1,10,2)]
print(js)


"4.6创建一个列表，其中包含3～30能被3整除的数，再使用一"\
"个for 循环将这个列表中的数打印出来。"

ch=list(range(3,31,3))
for chs in ch:
    print(ch)
    break


"4.7请创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for 循环将这些立方数打印出来。"

lf=[]
for lfs in range(1,11):
    lf.append(lfs**3)
print(lf)

print("The first three items in the list are:")
pul=['The','first','three','items','in','the','are:']
print(pul[0:3])
print(pul[2:5])
print(pul[-3:7])

"4.8有一家自助式餐馆，只提供五种简单的食品。请想出五种"\
"简单的食品，并将其存储在一个元组中。"\
"使用一个for 循环将该餐馆提供的五种食品都打印出来。"\
"尝试修改其中的一个元素，核实Python确实会拒绝你这样做。"\
"餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码"\
"块：给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来"

restaurant=('noodles','rice','steak','pasta','Fruit Salad')
for restaurants in restaurant:
    print(restaurant)
    break


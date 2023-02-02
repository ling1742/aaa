wage={"张三":300,"李四":400,"王五":550}
days={"张三":7,"李四":6,"王五":7}
wage["刘一"]=250
print(wage)
del wage["刘一"]
print(wage)
print(wage.get("张三"))

paid=0
for i in wage:
    paid=paid+(wage[i]*days[i])
print(paid)

print(wage.keys())

for name in sorted(wage.keys()):
    print(f'{name.title()},thank\tyou\tfor\ttaking\tthe\tpoll\t')


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())


for language in set(favorite_languages.values()):
 print(language.title())

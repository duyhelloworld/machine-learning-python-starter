# Comprehension
frameworks = ["AngolarJS", "Django", "Spring Boot", "StelveJS", "ReactJS", "VueJS", "NodeJS"]

fwOfJs = [x for x in frameworks if "JS" in x]
# print(fwOfJs)

# newlist = ['hello' for x in frameworks]
# print(newlist)

# List in list
fws = [frameworks]
# print(fws)

fwByAlphabet = [fw for fw in frameworks if fw.__contains__("JS")]
# fwByAlphabet.sort()
# fwByAlphabet.sort(reverse=True)
fwByAlphabet.sort(key=str.capitalize)
# print(fwByAlphabet)

fws2 = fws.copy()
# print(fws2)

# Unpacking by askterisk *
[Angolar, Django, Spring, *JS] = frameworks
print(Angolar)
print(JS)



n = int(input())

list_of_countries = []
while len(list_of_countries) < n:
    c = input()
    list_of_countries.append(c)

s = set(list_of_countries)
print(len(s))

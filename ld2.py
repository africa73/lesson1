phones = ["iPhone Xs", "Samsung 10 S", "Xiaomi Mi8"]

print(phones)
phones_count =len(phones)
print(phones_count)

#phones.append("iPhone 6")
#print(phones)
#подсчет встречаемых 
#print(phones.count("iPhone Xs"))

numbers = [3,5,7,9,10.5]

print(numbers)
numbers.append("Python")
print(numbers)
print(numbers[0])
print(numbers[-1])
numbers.remove('Python')
print(numbers)

u = {"city":"Москва","temperature": 20}
print(u["city"])
print(u["temperature"]+5)

print(u)
u.get("country", "Россия")
print(u)
#print(u["country"])

u["date"] ='27.05.2019'
print(u)

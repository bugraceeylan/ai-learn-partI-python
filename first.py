# No Dart/Flutter
# import requests

# numbers = 24
# for n in numbers:
#     print(n)

# def sum(a, b):
#     return a + b


# class User: 
#     def __init__(self, name): self.name = name  
#     def is_adult(self):
#         return self.age >= 18  

# res = requests.get('https://api.example.com/data')
# data = res.json()
# print(res.json())
# print(data["name"])

# print("Numbers from 1 to 10:")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def list_numbers(numbers):
#     for n in numbers:
#         print(n)

## list_numbers(numbers)

# def double(ikikati):
#     return ikikati * 2

# lists = [1, 2, 3, 4, 5]

# for item in lists:
#     print(item)

# for n in lists:
#     print(double(n))


## if __name__ == "__main__":

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = []
# def Olmbenzekiyim(n):
#      return n % 2 == 0

# for n in numbers:
#     if Olmbenzekiyim(n):  
#      print(n)

# for n in numbers:
#     if Olmbenzekiyim(n):  
#      even_numbers.append(n)
# print(even_numbers)


users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 25},
]

def get_adult_users(users):
    adult_users = []
    for u in users:
        if u["age"] >= 18:
            adult_users.append(u)
    return adult_users
adult_users = get_adult_users(users)
print(adult_users)



textls = ["ali", "mehmet", "can", "zeynep", "ece", "ibrahim"]

totalText = [n for n in textls if len(n) > 5]
print(totalText)

def convert_to_uppercase(texts):
    return [t.upper() for t in texts]

print(convert_to_uppercase(textls))
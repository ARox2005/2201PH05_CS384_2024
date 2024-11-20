def splitChoices(n):
    return [int(item.strip()) for item in n.split(",")]

def sepChars(c, s):
    caplet = []; samlet = []; number = []; specChar = []
    for i in range(len(c)):
      if c[i] == 1:
        capLet = [char for char in s if char.isupper()]
      elif c[i] == 2:
        samLet = [char for char in s if char.islower()]
      elif c[i] == 3:
        number = [char for char in s if char.isdigit()]
      elif c[i] == 4:
        specChar = [char for char in s if not char.isalnum()]
    return {
        1: capLet,
        2: samLet,
        3: number,
        4: specChar,
      }

def validator(S, c):
    for i in range(len(c)):
      if c[i] in range(1, 5):
        if len(S[c[i]]) == 0:
          return 0
        for j in S[4]:
          if j not in "!@#":
            return 0
    return 1

def input_pass_txt(file_name):
    password_list = []
    with open(file_name, 'r') as file:
        for line in file:
            password = line.strip()
            password_list.append(password)
    return password_list

print('''Choose the criterias you want int your password:
1: Uppercase letters (A-Z)
2: Lowercase letters (a-z)
3: Numbers (0-9)
4: Special characters (!, @, #) [Only 3 characters allowed]
''')

n = input("Enter your choices : ")
# m = int(input("Number of passwords you want to validate: "))
c = splitChoices(n)
password_list = input_pass_txt("passwords.txt")

for password in password_list:
  S = sepChars(c, password)
  if len(password)<8:
    print(f"Invalid password: {password}")
  elif validator(S, c)==1:
    print(f"Valid password: {password}")
  else:
    print(f"Invalid password: {password}")

isCorrect = True

usercode = str(input("Enter your postcode: "))
codelength = len(usercode)

def format():
    if codelength == 7:
        usercode = usercode[:4] + " " + usercode[4:] # ERROR - referenced before assignment
    else:
        print("Acknowledged")

usercode = usercode.upper()

if usercode[0] == usercode.isalpha():
    isCorrect = True
if usercode[1] == usercode.isalpha():
    isCorrect = True
if usercode[2] == usercode.isdigit():
    isCorrect = True
if usercode[3] == usercode.isdigit():
    isCorrect = True
if usercode[4] == usercode.isspace():
    isCorrect = True
if usercode[5] == usercode.isdigit():
    isCorrect = True
if usercode[6] == usercode.isalpha():
    isCorrect = True
if len(usercode) == 8:
    if usercode[7] == usercode.isalpha():
        isCorrect = True
else:
    autoformat = str(input("Incorrect format, format automatically (y/n)?: "))
    if autoformat == "y":
        format()
    if autoformat == "n":
        print(usercode)
    else:
        print("real funny")

print(usercode)
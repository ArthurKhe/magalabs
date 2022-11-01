abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

offset = 1

message = input("Message: ")

result = ""

for i in message:
    pos = abc.find(i)
    new_pos = pos + offset
    if i == "z":
        new_pos = 52
    if i == "Z":
        new_pos = 0
    if i in abc:
        result +=abc[new_pos]
    else:
        result += i

print(result)

with open("cesar.txt", "w") as f:
    f.write(result)

with open("deshifr.txt", "w") as f:
    f.write(message)


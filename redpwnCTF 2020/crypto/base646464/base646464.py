import base64

f = open("cipher.txt","rb")
line = f.readline()

for i in range(25):
    line = base64.b64decode(line)

print(line)

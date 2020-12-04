#Damien Jones


plaintext = open("plaintext.txt", "r+")


# Read file here
if plaintext.mode == 'r+':
    plaintext_in = plaintext.read()

file_length = len(plaintext_in)

print("Plain text in: " + plaintext_in)

temp = ord('a')
print("Int a = " + str(temp))
print("Binary: " + bin(temp))

y = bin(temp)

for i in range(len(y)):
    if i > 1:
        print("bin temp i: " + y[i])




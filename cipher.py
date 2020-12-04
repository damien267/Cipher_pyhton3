#Damien Jones


# Read file here
plaintext = open("plaintext.txt", "r+")
key = open("key.txt", "r")

if plaintext.mode == 'r+':
    plaintext_in = plaintext.read()

print("Plain text in: " + plaintext_in)


file_length = len(plaintext_in) - 1
print("File length: " + str(file_length))

if key.mode == 'r':
    key_in = key.read()
    if (len(key_in) - 1) != 16:
        print("Invalid key length, length is: " + str(len(key_in)))

if file_length % 8 != 0:
    print("This will require padding")

left = [0] * 4
right = [0] * 4


print("\n")




# Split into blocks: 8 char -> 16 bytes -> 64 bit blocks
j = 0
i = 0
left[j] = plaintext_in[i]
left[j+1] = plaintext_in[i+1]
left[j+2] = plaintext_in[i+2]
left[j+3] = plaintext_in[i+3]
right[j] = plaintext_in[i+4]
right[j+1] = plaintext_in[i+5]
right[j+2] = plaintext_in[i+6]
right[j+3] = plaintext_in[i+7]



temp = ord('a')
print("Int a = " + str(temp))
print("Binary: " + bin(temp))

y = bin(temp)

for i in range(0, len(y)):
    if i > 1:
        print("bin temp i: " + y[i])




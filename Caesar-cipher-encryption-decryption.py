text=input("Enter the plain text:")
k=int(input("Enter the key size:"))
char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

encryption=''
decryption=''

for i in text:
    x=char.find(i)
    n=(x+k)%26
    encryption+=char[n]
print("The encrypted message is:",encryption)

for i in encryption:
    y=char.find(i)
    n=(y-k)%26
    decryption+=char[n]
print("The decrypted message is:",decryption)

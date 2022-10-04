a=input("Enter Your Secret Message Here: ")

k1=int(input("Enter The Key1 (Number): "))
k2=input("Enter The Key2 (Word): ")

f=0
for i in k2:
    f+=(ord(i))

total=""
b=input("You Want To Encrypt Or Decrypt Your Message(E/D): ")

if(b=="E"):
    print("Encrypting Your Message ......")
    for i in a:
        total+=chr((ord(i)+k1)%f)
    print("Your Message Encrypted Successfully! ")
    print("Your Encrypted Message is: ",total)
        
elif(b=="D"):
    print("Decrypting Your Message ......")
    for i in a:
        total+=chr((ord(i)-k1)%f)
    print("Your Message Decrypted Successfully! ")
    print("Your Decrypted Message is: ",total)




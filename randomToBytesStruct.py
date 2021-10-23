import struct
import random

print("Custom Random Number to Bytes APP")
print("Set Min Number")
minNumber=input()

print("Set Max Number")
maxNumber=input()

#Result Random
result=random.randint(int(minNumber), int(maxNumber))
print("Result Random is : ", result)

#Converting to Bytes Struct
mystruct=struct.pack('iii',int(minNumber),int(maxNumber),int(result))

print('Struct Bytes Result',mystruct)
print('Struct Bytes Original',struct.unpack('iii',mystruct))

# Custom Random Number to Bytes APP
# Set Min Number
# 5
# Set Max Number
# 9
# Result Random is :  7
# Struct Bytes Result b'\x05\x00\x00\x00\t\x00\x00\x00\x07\x00\x00\x00'
# Struct Bytes Original (5, 9, 7)

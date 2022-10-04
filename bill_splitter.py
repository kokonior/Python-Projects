date=input("Enter Date (DD-MM-YY): ")
place=input("Enter The Name Of The Place/Event: ")
total=int(input("Enter The Total Amount: "))
p=int(input("Enter The Total Number Of Persons: "))
perhead=total/p
paid=int(input("Enter The Amount Paid By You: "))
a=int(paid-perhead)
print("*"*60)
print()
print("Date : ",date)
print("Name Of The Place : ",place)
print()
print("*"*60)
print()
print("The Total Amount To Be Paid : ",total)
print("Total Number Of Persons : ",p)
print()
print("*"*60)
print()
if(a>0):
    print("You Have To Take",a,"rupees :-)")
elif(a<0):
    print("You Have To Give",-a,"rupees :-(")
else:
    print("You Don't Have To Give/Take Money ^-^ ")
print()
print("*"*60)


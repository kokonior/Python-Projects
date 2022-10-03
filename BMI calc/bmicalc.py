#simple program to find if your are obese , fit or underwieght as per BMI

height = float(input("Enter height in cm: "))  
weight = float(input("Enter weight in kg: "))  
 
bmi = weight/(height/100)**2  
print("Your Body Mass Index is", bmi)   
if bmi <= 18.5:  
    print("underweight")  
elif bmi <= 24.9:  
    print("healthy")  
elif bmi <= 29.9:  
    print("overweight")  
else:  
    print("obese")  

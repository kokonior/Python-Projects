import random

# This function generates the password 
def generate_new_password(length):
    result = []
    for i in range(length):
        char = random.choice(
            "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$_`?=;")
        result.append(char)
    return result


if __name__ == "__main__":
    while True:
        length = input("Enter the length of the password you want: ")
        try:
            length = int(length)
            result = "".join(generate_new_password(length))
            print(f"The generated password is {result}")
            answer = input(
                "Do you want to generate another password. Please Type y or n: ")
            if answer == "n":
                break
            continue
        except:
            print("Please insert a number")

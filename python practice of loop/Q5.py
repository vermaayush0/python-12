import time
password = "ayush123"
attempt = 3

while 1:
    user_pass = input("\nEnter the password : ")
    if user_pass == password:
        print("Login Succesfull")
        break
    else:
        print("Worng Password,Try Again")
    attempt -= 1
    if attempt <= 0:
        print("Failed to Login ")
        print("Wait for a second ")
        count = 10
        while count:
            time.sleep(1)
            print(count, end=" ")
            count -= 1
        attempt = 3

User=input("Enter the username:")
password=input("Enter the password")

if User=='Python':
    if password=='welcome':
        print("login successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")

Player1=int(input("Enter score of A:"))
Player2=int(input("Enter score of B:"))

Sum=Player1+Player2

if Player1>300 or Player2>300:
    if Sum<500:
        print("Can Team Up")
    else:
        print("Cannot team up")

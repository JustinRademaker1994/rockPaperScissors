print("Welcome to rock, paper, scissors and smth..")
print("Reminder: If playing in front of others, hide your answer.. or else they can cheat")
print("Also, always spell rock, paper and scissors with a capital letter at the start because Im too lazy to make it case insensitive")
print("Such as 'Rock'")


A = input("Enter Rock, paper and scissors: ")
B=  input("Enter Rock, paper and scissors: ")


if A == B:
    print("It's a tie")


elif A == "Rock":
    if B == "Scissors":
        print("Player 1 wins")
    else:
        print("Player 2 wins")

elif A == "Rock":
    if B == "Paper":
        print("Player 2 wins")

elif A == "Paper":
    if B == "Rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")

elif A == "Paper":
    if B == "Scissors":
        print("Player 2 wins")

elif A == "Scissors":
    if B == "Paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")

else:
    print("https://manuall.my.canva.site/.")

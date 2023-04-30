player_1 = input("Player_1 your choice(rock/paper/scissor):: ")

player_2 = input("Player_2 your choice(rock/paper/scissor):: ") 


if player_1 == player_2:
    print("tie")

elif player_1=="rock":
    if player_2=="scissor":
        print("\n" "Player_1 congratulation you win..." "\n")
    elif player_2=="paper":
        print("\n" "Player_2 congratulation you win..." "\n")
elif player_1=="paper":
    if player_2=="rock":
        print("\n" "Player_1 congratulation you win...")
    elif player_2=="scissor":
        print("\n" "Player_2 congratulation you win...")
elif player_1=="scissor":
    if player_2=="paper":
        print("\n" "Player_1 congratulation you win...")
    elif player_2=="rock":
        print("\n" "Player_2 congratulation you win...")

        

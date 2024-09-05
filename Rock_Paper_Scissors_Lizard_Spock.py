import random

player_win = 0
pc_win = 0

print("The rules are Rock Paper Scissors Lizard Spock. \n1)Paper covers Rock."
        "\n2)Rock crushes Lizard."
        "\n3)Lizard poisons Spock.\n4)Spock smashes Scissors.\n5)Scissors beat Lizard."
        "\n6)Lizard eats Paper.\n7)Paper disproves Spock.\n8) Spock vaporizes Rock."
        "\n9)Rock breaks Scissors.")

print("================================\nRock Paper Scissors Lizard Spock\n================================")
print("1)✊\n2)✋\n3)✌️\n4)🦎\n5)🖖")

while player_win < 3 and pc_win < 3:
    
    player = int(input(""))
    pc = random.randint(1,5)

    if player < 5:
        
        if player == 1:
            print("player chose:✊")
        elif player == 2:
            print("player chose:✋")
        elif player == 3:
            print("player chose:✌️")
        elif player == 4:
            print("player chose:🦎")
        elif player == 5:
            print("player chose:🖖")
            
        if pc == 1:
            print("pc chose:✊")
        elif pc == 2:
            print("pc chose:✋")
        elif pc == 3:
            print("pc chose:✌️")
        elif pc == 4:
            print("pc chose:🦎")
        elif pc == 5:
            print("pc chose:🖖")
        
        if player == 3 and pc == 2 or player == 2 and pc == 1 or player == 1 and pc == 4 \
          or player == 4 and pc == 5 or player == 5 and pc == 3 or player == 3 and pc == 4 \
          or player == 4 and pc == 2 or player == 2 and pc == 5 or player == 5 and pc == 1 \
          or player == 1 and pc == 3:
            player_win +=1
            print("Gano el player")
        elif player == pc:
            print("Empate")
        else:
            pc_win +=1
            print("Gano el pc")

    else:
        print("A ocurrido un error")

if player_win > pc_win:
    print(f"The winner was the player with a total of {player_win} wins and the loser is the pc whith a total of {pc_win} wins")
else:
    print(f"the winner was the pc with a total of {pc_win} wins and the loser is the player whith a total of {player_win} wins ")
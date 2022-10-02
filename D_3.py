from math import ceil, floor

# Practice Problem 1
# num = float(input("Enter a floating number: "))
# print(f'Floor is {floor(num)} and Ceil is {ceil(num)}')

# Practice Problem 2
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# if num1 < 0:
#     num1 = (-num1)
# if num2 < 0:
#     num2 = (-num2)
# if num3 < 0:
#     num3 = (-num3)

# print(f'Num1: {num1}\nNum2: {num2}\nNum3: {num3}')

# Practice Problem 3
player1 = input("Player 1: ")
player2 = input("Player 2: ")
if player1 == player2:
    print('Draw')
if (player1 == 'rock' and player2 == 'scissors') or (player2 == 'rock' and player1 == 'scissors'):
    print(f'Player {player1=="rock" and "1" or "2"} is the winner')
elif (player1 == 'paper' and player2 == 'rock') or (player2 == 'paper' and player1 == 'rock'):
    print(f'Player {player1=="paper" and "1" or "2"} is the winner')
elif (player1 == 'scissors' and player2 == 'paper') or (player2 == 'scissors' and player1 == 'paper'):
    print(f'Player {player1=="scissors" and "1" or "2"} is the winner')

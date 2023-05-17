import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "무승부"
    elif (player_choice == "가위" and computer_choice == "보") or (player_choice == "바위" and computer_choice == "가위") or (player_choice == "보" and computer_choice == "바위"):
        return "플레이어 승리!"
    else:
        return "컴퓨터 승리!"

def play_game():
    choices = ["가위", "바위", "보"]
    
    while True:
        player_choice = input("가위, 바위, 보 중 하나를 선택하세요 (끝내려면 '끝'을 입력하세요): ")
        
        if player_choice == "끝":
            print("게임을 종료합니다.")
            break
        
        if player_choice not in choices:
            print("잘못된 선택입니다. 다시 선택해주세요.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"플레이어: {player_choice}")
        print(f"컴퓨터: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        print()
        
play_game()

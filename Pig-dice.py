import random

# 주사위 굴리기


def roll_dice():
    return random.randint(1, 6)


# 플레이어 구현
def pig_dice(max_score):
    score = {
        "player1": 0,
        "player2": 0
    }
    current_player = "player1"
    value = score.values()
    # roll_dice를 통한 모은 임시 점수
    temp_score = 0
    while max(value) < max_score:
        roll = roll_dice()
        # 주사위가 1이 나온경우 모은 스코어
        if roll == 1:
            print("rolled 1")
            temp_score = 0
            # 다음사람으로 넘어가는 기능
            current_player = next_player(current_player)
        # 주사위가 1외의 숫자인 경우
        else:
            temp_score += roll
            print(f"{current_player} rolled : {roll}")
            print(f"Total Score : {score[current_player]}")
            print(f"Current Score : {temp_score}")
            ans = input("Do you want to roll again? Y/N")
            if ans.lower() == "n":
                score[current_player] += temp_score
                temp_score = 0
                # 다음사람으로 넘어가는 기능
                current_player = next_player(current_player)
        return current_player


def next_player(current_player):
    return "player2" if current_player == "player1" else "player1"


max_score = 100
winner = pig_dice(max_score)
print(f"winner is  {winner}")

import random

# 주사위 굴리기


def roll_dice():
    return random.randint(1, 6)


# 플레이어 구현
score = {
    "player1": 0,
    "player2": 0
}
current_player = "player1"
value = score.values()
# 목표점수
max_score = 100
# roll_dice를 통한 모은 임시 점수
temp_score = 0
while value < max_score:
    roll = roll_dice()
    # 주사위가 1이 나온경우 모은 스코어
    if roll == 1:
        temp_score = 0
        # 다음사람으로 넘어가는 기능 구현해야함
    # 주사위가 1외의 숫자인 경우
    else:
        temp_score += roll
        ans = input(f"{current_player} rolled {roll}"
                    f"Current Score {temp_score}"
                    "Do you want to roll again? Y/N")
        if ans.lower() != "y":
            score[current_player] += temp_score
            # 다음사람으로 넘어가는 기능 구현해야함

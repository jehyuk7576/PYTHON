import random
import os

while True:

    print("청기 백기를 시작하겠습니다.")
    print("게임은 상대방과 자신이 같아질때까지 진행 됩니다.")
    print("컴퓨터가 랜덤으로 청기와 백기중 하나를 들겁니다")
    print("\n")

    print("청기 = 1")
    print("백기 = 2")

    user = int(input("원하는 숫자를 입력하세요"))
    print("\n")
    com = random.randint(1,2)

    if (user == 1):

        if (com == 1):
            print("상대가 청기를 선택해서 비겼습니다. 게임을 종료합니다.")
            break
        else:
            print("상대가 백기를 선택해서 이겼습니다. 게임을 진행합니다.")
            os.system('cls')

    elif (user == 2):

        if (com == 1):
            print("상대가 청기를 선택해서 이겼습니다. 게임을 진행합니다.")
            break
        else:
            print("상대가 백기를 선택해서 비겼습니다. 게임을 종료합니다. ")
            os.system('cls')
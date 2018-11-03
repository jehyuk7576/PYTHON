import random
import os

while True:  # 여기에 while문을 입력하게되면 여기 아래쪽에 포함하는 모든 코드들이 무한 반복이되는거야!

    print("참참참을 시작합니다")
    print("오른쪽, 왼쪽, 가운데에 지정되어 있는 숫자 하나를 고르세요")
    print("컴퓨터가 오른쪽, 왼쪽, 가운데 중 하나를 선택할겁니다 당신은 컴퓨터가 선택 한 답과 달라야 이깁니다")
    print("\n")

    print("오른쪽 = 1")
    print("왼쪽 = 2")
    print("가운데 = 3")
    print("종료 = 4")

    user = int(input("원하는 숫자를 입력하세요"))
    print("\n")
    com = random.randint(1, 3)

    if (user == 1):

        if (com == 1):
            print("상대가 오른쪽을 선택해서 젔습니다. 게임을 종료합니다")
            break  # 그리고 이렇게 break 문을 사용하면 무한루프에서 벗어나게 되는거야!
        elif (com == 2):
            print("상대가 왼쪽을 선택해서 이겼습니다. 게임을 종료합니다")
            os.system('cls')  # 이걸 넣은 이유는 게임종료가 아니라 계속 게임을 진행하는데 화면이 깔끔해지게 하기위해서 한번 싹 지워주는 역할이야! 나중에 자세하게 알려줄게~
        else:
            print("상대가 가운데를 선택해서 이겼습니다. 게임을 종료합니다")
            os.system('cls')

    elif (user == 2):

        if (com == 1):
            print("상대가 오른쪽을 내서 이겼습니다. 게임을 종료합니다")
            break
        elif (com == 2):
            print("상대가 왼쪽을 내서 젔습니다. 게임을 종료합니다")
            os.system('cls')
        else:
            print("상대가 가운데를 내서 이겼습니다. 게임을 종료합니다")
            os.system('cls')

    elif (user == 3):

        if (com == 1):
            print("상대가 오른쪽을 내서 이겼습니다. 게임을 종료합니다")
            break
        elif (com == 2):
            print("상대가 왼쪽을 내서 이겼습니다. 게임을 종료합니다")
            os.system('cls')
        else:
            print("상대가 가운데를 내서 젔습니다. 게임을 종료합니다")
            os.system('cls')

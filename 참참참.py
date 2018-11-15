import random
import os

print("참참참을 시작합니다")
print("오른쪽, 왼쪽, 가운데에 지정되어 있는 숫자 하나를 고르세요")
print("컴퓨터가 오른쪽, 왼쪽, 가운데 중 하나를 선택할겁니다 당신은 컴퓨터가 선택 한 답과 달라야 이깁니다")
print("\n")

while True:  # 여기에 while문을 입력하게되면 아래의 코드가 무한반복이 된다

    print("오른쪽 = 1")
    print("왼쪽 = 2")
    print("가운데 = 3")
    print("종료 = 4")

    user = int(input("원하는 숫자를 입력하세요 :"))
    print("\n")
    com = random.randint(1, 3)

    if (user == 1):#만약 사용자가 1(오른쪽)을 입력 했을때

        if (com == 1):#컴퓨터가 1(오른쪽)을 입력 했을때
            print("상대가 오른쪽을 선택해서 젔습니다. 게임을 종료합니다")
            break  # 그리고 이렇게 break 문을 사용하면 무한루프에서 벗어나게 된다
        elif (com == 2):#컴퓨터가 2(왼쪽)을 입력했을때
            print("상대가 왼쪽을 선택해서 이겼습니다. 게임을 종료합니다")
            os.system('cls')  # 게임 진행에 필요하지 않은 글을 지운다
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

import random

print("가위 바위 보 게임을 시작합니다")
print("가위 바위 보에 지정되 있는 숫자 하나를 누르세요")
print("\n")

print("가위 = 1")
print("바위 = 2")
print("보 = 3")

user = int(input("원하는 숫자를 입력하세요"))
print("\n")
com = random.randint(1, 3)

for x in range(1,2):

    if(user == 1):

        if(com == 1):
            print("상대가 가위를 내서 비겼습니다. 게임을 종료합니다")
        elif(com == 2):
            print("상대가 바위를 내서 젔습니다. 게임을 종료합니다")
        else:
            print("상대가 보를 냈습니다 이겼습니다. 게임을 종료합니다")

    elif (user == 2):

        if (com == 1):
            print("상대가 가위를 내서 이겼습니다. 게임을 종료합니다")
        elif (com == 2):
            print("상대가 바위를 내서 비겼습니다. 게임을 종료합니다")
        else:
            print("상대가 보를 냈습니다 젔습니다. 게임을 종료합니다")

    elif (user == 3):

        if (com == 1):
            print("상대가 가위를 내서 젔습니다. 게임을 종료합니다")
        elif (com == 2):
            print("상대가 바위를 내서 이겼습니다. 게임을 종료합니다")
        else:
            print("상대가 보를 냈습니다 비습니다. 게임을 종료합니다")
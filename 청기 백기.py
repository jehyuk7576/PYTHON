import datetime
import time
import random
import os
print("청기 = 1")
print("백기 = 2")
input("enter를 누르면 게임을 시작합니다")
count = 0
while True:
    ran_flag = random.randint(1,2)
    if ran_flag == 1:
        print("청기들어!\n")
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=3)
        flag = input(">> ")
        if datetime.datetime.now() <= endTime:
            if flag == "1":
                print("정답")
                count += 1
                time.sleep(1)
                os.system("cls")
            elif flag == "2":
                print("틀렸습니다")
                print("{} 번 성공!".format(count))
                break
            else:
                print("잘못된 숫자입니다")
                print("{} 번 성공!".format(count))
                break
        else:
            print("time out")
            print("{} 번 성공!".format(count))
            break

    if ran_flag == 2:
        print("백기들어!\n")
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=3)
        flag = input(">> ")
        if datetime.datetime.now() <= endTime:
            if flag == "2":
                print("정답")
                count += 1
                time.sleep(1)
                os.system("cls")
            elif flag == "1":
                print("틀렸습니다")
                print("{} 번 성공!".format(count))
                break
            else:
                print("잘못된 숫자입니다")
                print("{} 번 성공!".format(count))
                break
        else:
            print("time out")
            print("{} 번 성공!".format(count))
            break

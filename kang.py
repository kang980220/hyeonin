

fuk = ['총알발사','오른쪽이동','왼쪽이동','게임종료하기']

hyeon = [1,2,3,4,5,6,7,8,9,10]


print("갤러그 게임 시작")


name = input("사용자 닉네임은?")

# 딕셔너리
score = {

    'hy1' : '강현인',  

    'hy2' : '노진구',

    'hy3' : '김계란',

    'hy4' : name
    
}

count = 0



for hyeonin in hyeon: 

    count += 1
    print("적 비행기 발생")

    print("1.발사 2.오른쪽이동 3.왼쪽이동 4.게임 종료하기" )

    number = input("숫자를 입력하세요: ")

    print("당신의 입력값? ", number )

    # 만약에 1번을 누르면 총알 발사
    if number == "1":
        print(fuk[0])

    # 만약에 2번을 누르면 오른쪽
    if int(number) == 2:
        print(fuk[1])

    # 만약에 3번을 누르면 왼쪽'
    if number == "3":
        print(fuk[2])

    if number == "4":
        print(fuk[3])
        break


print(name , " 님 수고하셨습니다.")

print(name , " 님은 10번 중  " , count , " 번 선택 했습니다")

print("1위",score["hy1"])
print("2위",score["hy2"])
print("3위",score["hy3"])
print("4위",score["hy4"])

 
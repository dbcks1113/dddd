print("롤로코스터를 타러 오셨군요!")
height = int(input("키가 몇 cm 입니까?"))
bill = 0
if height >= 120:
    print("롤러코스터를 타실 수 있습니다!")
    age = int(input("당신은 몇살입니까?"))
    if age <= 12:
        bill=0
        print("무료입니다!")
    elif age <=18:
        bill=7000
        print("7천원입니다")
    else:
        bill = 12000
        print("만2천원입니다")

wants_photo = input("사진을 찍기를 원합니까? yes(y) or no(n).")
if wants_photo == "y":
#천원 추가
bill += 1000
print(f"지불하실 총 금액은 {bill}")

else:

    print("죄송하지만 롤러코스터를 탈 수 없어요.")


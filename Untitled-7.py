print("1부터 45번까지 숫자를 입력하세요")
num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))
num3 = int(input("세번째 숫자 : "))
num4 = int(input("네번째 숫자 : "))
num5 = int(input("다섯번째 숫자 : "))
num6 = int(input("여섯번째 숫자 : "))
my_nums = [num1,num2,num3,num4,num5,num6]
my_nums.sort()
print(f"당신이 선택한 로또 번호는 {my_nums} 입니다.")
import random
com1 = random.randint(1,46)
com2 = random.randint(1,46)
com3 = random.randint(1,46)
com4 = random.randint(1,46)
com5 = random.randint(1,46)
com6 = random.randint(1,46)
com_nums = [com1,com2,com3,com4,com5,com6]
com_nums.sort()
print("추첨된 로또 번호는", com_nums, "입니다.")
if(my_nums == com_nums):
    print("*** 축! 당첨 ***")
else:
    print("꽝 다음기회에")

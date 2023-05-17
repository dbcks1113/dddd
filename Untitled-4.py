import random
#1~10사이의 정수 난수를 출력
random_integer = random.randint(1,10)
print(random_integer)
#0~1 사이의 부동 소수점 출력
random_float = random.random()*5
print(random_float)

my_score = random.randint(1,100)
print(f"당신의 예상 스코어는 {my_score}")

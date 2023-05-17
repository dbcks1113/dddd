import random
name_string = input("아이스크림 내기에 참여할 사람들 이름을 입력,쉼표를 사용해서 이름을 구분해줘:")
names = name_string.split(",")
num_item = len(names)
random_choice = random.randint(0,num_item -1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "(은)는 아이스크림 사기!")
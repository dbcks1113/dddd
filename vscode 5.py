height = input("당시느이 키는 몇 m:")
weight = input("당신의 몸무게는 몇 kg:")

bmi = int(weight)/float(height)**2

bmi = round(bmi,2)

print(bmi)
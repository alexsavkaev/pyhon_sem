# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.

n= int(input('Введите количество арбузов: '))
mass1 = int(input('Введите массу арбуза: '))
min = mass1
max = mass1
i = 2
while i <=n:
    mass = int(input('Введите массу арбуза: '))
    if mass < min:
        min = mass
    if mass > max: 
        max = mass
    i=i+1
print("Себе:", max)    
print("Тёще:", min)

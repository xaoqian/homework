#1.через какое-то время.медведь ходит к рыбе
#2.через какое-то время.рыба ходит к медведе
#3.через какое-то время.рыба и медведь не двигаются
#4.через какое-то время.медведь и рыба сорят друг с другом
#5.через какое-то время.рыба умерает
n = int(input('введите число одно из 1,2,3,4,5： '))
bear = [1]
fish = [1]
new = []
river = [bear,fish] or [None]

if bear and fish in river:
    if n == 1:
        fish = fish.append(1)
    elif n == 2:
        bear = bear.append(1)
    elif n == 3:
        bear = bear
        fish = fish
    elif n == 4:
        new = new.append(1)
    elif n == 5:
        fish = 0

if fish == 2:
    bear = 0

print('количество рыб: ', fish )
print('количество медведей: ', bear)
print('количество нового: ', new)


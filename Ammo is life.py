import random

count = 2
floor = 1
ammo = random.randint(100, 200)
difficulty = 1

i = 1

print("Вы входите в подземелье, у вас", ammo, "патрон")
while i == 1:
    escapecount = random.randint(1, 3)
    elitebosschance = random.randint(1, 5)
    satandamage = random.randint(300, 750) * difficulty
    lesserdemondamage = 10 * difficulty
    middledemondamage = 25 * difficulty
    highdemondamage = 40 * difficulty
    bossdamage = random.randint(75, 100) * difficulty
    ammoregen = random.randint(1, 2)
    regencount = random.randint(50, 100) * difficulty
    enemy = random.randint(1, 3)
    prodolz = input("Продолжить ?\n")
    if prodolz == "да":
        if enemy == 1:
            print("Вы встретили низшего демона, придётся потратить", lesserdemondamage, "патрон")
            atack = input("Напасть? да/нет\n")
            if atack == "да":
                print("Вы потратили", lesserdemondamage, "патрон\n")
                ammo -= lesserdemondamage
                if ammoregen == 1:
                    print("Вы нашли коробку патрон и восстановили", regencount, "патрон\n")
                    ammo += regencount
            if atack == "нет":
                if escapecount == 1:
                    print("Вы смогли сбежать")
                else:
                    print("Вы не смогли сбежать и разозлили демона, придётся тратить", lesserdemondamage * 2, "патрон")
        if enemy == 2:
            print("Вы встретили среднего демона, придётся потратить", middledemondamage, "патрон")
            atack = input("Напасть? да/нет\n")
            if atack == "да":
                print("Вы потратили", middledemondamage, "патрон\n")
                ammo -= middledemondamage
                if ammoregen == 1:
                    print("Вы нашли коробку патрон и восстановили", regencount, "патрон\n")
                    ammo += regencount
            if atack == "нет":
                if escapecount == 1:
                    print("Вы смогли сбежать")
                else:
                    print("Вы не смогли сбежать и разозлили демона, придётся тратить", middledemondamage * 2,
                          "патрон")
        if enemy == 3:
            print("Вы встретили высшего демона, придётся потратить", highdemondamage, "патрон")
            atack = input("Напасть? да/нет\n")
            if atack == "да":
                print("Вы потратили", highdemondamage, "патрон\n")
                ammo -= highdemondamage
                if ammoregen == 1:
                    print("Вы нашли коробку патрон и восстановили", regencount, "патрон\n")
                    ammo += regencount
            if atack == "нет":
                if escapecount == 1:
                    print("Вы смогли сбежать")
                else:
                    print("Вы не смогли сбежать и разозлили демона, придётся тратить", highdemondamage * 2,
                          "патрон")
        if count < 4:
            print("Вы прошли в комнату", count)
        count += 1
    if count > 4:
        ammo += regencount
        if elitebosschance == 5:
            bossdamage *= 2
            print("БОСС ЭЛИТНЫЙ СЛУГА САТАНЫ")
            print("Вы получили бонус равный", regencount, "патрон")
            print("Вы встретили элитного слугу сатаны\n")
            ammo -= bossdamage
            print("Вы потратили", bossdamage, "патрон")
            difficulty += 1
            print("Сложность выросла и теперь она равна", difficulty, )
            floor += 1
            print("Вы перешли на этаж", floor)
            count = 2
            print("У вас осталось", ammo, "патрон")
        else:
            print("БОСС СЛУГА САТАНЫ")
            print("Вы получили бонус равный", regencount, "патрон")
            print("Вы встретили слугу сатаны\n")
            ammo -= bossdamage
            print("Вы потратили", bossdamage, "патрон")
            difficulty += 1
            print("Сложность выросла и теперь она равна", difficulty, )
            floor += 1
            print("Вы перешли на этаж", floor)
            count = 2
            print("У вас осталось", ammo, "патрон")
    if floor % 5 == 0:
        if elitebosschance == 5:
            print("БОСС ЭЛИТНЫЙ САТАНА")
            print("Перед битвой с элитным сатаной вы получите бонус равный", ammo * difficulty, "патрон\n")
            print("Вы встретили элитного сатану и вам придётся потратить", satandamage, "патрон")
            print("Если вы нападёте то умножете ваши очки на", difficulty, "\n")
            pobeg = input("У вас есть возможность сбежать или драться, что будете делать?\n")
            if pobeg == "драться":
                ammo *= difficulty
                ammo *= difficulty
                print("У вас", ammo, "патрон")

            if pobeg == "бежать":
                print("Вы сбежали")
                print("У вас осталось", ammo, "патрон")
                i = 0
        else:
            print("БОСС САТАНА")
            print("Перед битвой с сатаной вы получите бонус равный", ammo * difficulty, "патрон\n")
            print("Вы встретили сатану и вам придётся потратить", satandamage, "патрон")
            print("Если вы нападёте то умножете ваши очки на", difficulty)
            pobeg = input("У вас есть возможность сбежать или драться, что будете делать?")
            if pobeg == "драться":
                ammo *= difficulty
                ammo *= difficulty
                print("У вас", ammo, "патрон")

            if pobeg == "бежать":
                print("Вы сбежали")
                print("У вас осталось", ammo, "патрон")
                i = 0
    if prodolz == "нет":
        print("Вы сбежали с", ammo, "патрон")
        i = 0
    if ammo <= 0:
        print("Вы погибли, жаль")
        i = 0

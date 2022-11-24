# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and ⋁ - or ¬ - not

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if ((not x) or (not y) or (not z)) == ((not x) and (not y) and (not z)):
                print(True)
            else:
                print(False)

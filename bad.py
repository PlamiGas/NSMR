def calculate(x):
    if 100<=x<200:
        rat= 10
    elif x>= 200:
        rat= 15
    else:
        return "Тогда ты Артур"
    coe = rat
    qua = rat
    return {
        "Ass": coe,
        "ХИХИХА": qua
    }
h = float(input("Негр"))
res = calculate(h)
print(res)

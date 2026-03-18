money=0
mone=0
mon=0
mo=0
m=0
print('Запушен фарм монеток. Ваши монетки фармятся.')
while True:
    m+=1
    if m==100:
        m=0
        mo+=1
        if mo==100:
            mo=0
            mon+=1
            if mon==100:
                mon=0
                mone+=1
                if mone==100:
                    mone=0
                    money+=1
                    print('Вы получили монетку!',"""
Текущий баланс:""", money)
import math
#n ile razy było prawiłodwy streak,
#interval za ile ma byc nastepne powtorzenie
#poczatkwe EF to chyba 2.5 

def superMemo(user_grade, prev_n, prev_EF, prev_interval):
    if prev_n == 0:
         prev_EF= 2.5

    if user_grade == 3:
        if prev_n == 0:
            interval= '10 minut'
        elif prev_n == 1:
            interval= '15 minut'  #dostosowac to
        else:
             if prev_interval == "10 minut" or prev_interval == '15 minut':
                 interval= 2
             else: 
                interval= math.floor(prev_interval*prev_EF*1)
        n= prev_n +1

    elif user_grade == 4:
     if prev_n == 0:
            interval= '15 minut'
     elif prev_n == 1:
            interval= 1  #dostosowac to
     else:
            if prev_interval == "10 minut" or prev_interval == '15 minut':
                 interval= 3
            else: 
                interval= math.floor(prev_interval*prev_EF*2)
     n= prev_n +1

    elif user_grade == 5:
     if prev_n == 0:
            interval= 1
     elif prev_n == 1:
            interval= 3  #dostosowac to
     else:
            if prev_interval == "10 minut" or prev_interval == '15 minut':
                 interval= 5
            else: 
                interval= math.ceil(prev_interval*prev_EF*3)
     n= prev_n +1
        
    else: #jeśli odpowiedz uzytkownika była mniej niz 3 czyli źle odpowiedzial
        n= 0
        interval= '10 minut'
    EF= prev_EF + ( 0.1-(5-user_grade) * ( 0.08 + (5-user_grade)*0.02 ) )
    EF= max(EF, 1.3)

    return(n, EF, interval)


def anki(prev_n, prev_EF, prev_interval):
    for i in range(6):
        print(superMemo(i, prev_n, prev_EF, prev_interval))

#print(superMemo(4, 2, 2.46, 6))
anki(4, 2.46, 13)
#anki(2, 2.21, '15 minut')

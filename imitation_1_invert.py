#Штакельберг с обратной связью по управлению - 1 агент
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#объявление переменных


def Shtackelberg_1_invert():   
    
    N = 10
    T_min = 5000 #супервайзер u  (5000-7000)
    T_max = 7000
    tao_min = 0.1 #агент v
    tao_max = 1

    h_T = (T_max - T_min)/N
    h_tao = (tao_max - tao_min)/N
    z0 = 0.1
    z_abs = 0.6 #то с чем сравниваем - наш показатель "эффективности" - идеальный 
    a = 0.8 #коэфф
    #m1 = 1 #коэфф
    outlay = 0.007
    lambd = - 100000
    lambd_1 = -100 
    salary = 10000
    k_c = 7
    bet = 0.5
    #определяем функции - тестовые 
    def J_0(T, tao, z):
        return (T * tao) * 0.8 * (1 - z) - outlay - lambd * (T ** lambd_1)
    def J_1(T, tao, z):
        return 0.87 * salary * ((1 + z) ** 2) - tao * T * (1 - z) + k_c * (z**bet) * ((tao_max - tao)**(1 - bet))
    def z_tao(tao):
         return round(z0 + a * tao, 5)

    
    def L_T():       #гарантированный выигрыш агента - посчитали, это число
        J1_min_list = [] #список по которому будем искать максимум по tao - состоит из минимумов по Т
        for i_tao in range (N):
            tao = tao_min + i_tao * h_tao

            J1_list = []
            for j_T in range (N):
                T = T_min + j_T * h_T
                #находим минимум J1 по T и запоминаем Т
                J1_list.append(round(J_1(T, tao, z_tao(tao)), 7))
            J1_min = min(J1_list)
            T_J1 = J1_list.index(J1_min) * h_T + T_min
    #         print ("min", J1_min)
    #         print("T, при котором достигается min", T_J1)
            J1_min_list.append(J1_min)           
            #находим максимум по tao с учетом найденного Т
        print("все минимумы", J1_min_list)   
        return max(J1_min_list)
    L = L_T()        
    #цикл
    print("гарантированный выигрыш агента:", L )

    # нашли гарантированный выигрыш агента
    J0_list = [] 
    for i_tao in range(N):
        tao = tao_min + i_tao * h_tao


        for i_T in range(N):
            T = T_min + i_T * h_T
            if (round(z_tao(tao), 7) > z_abs) and (L < round(J_1(T, tao, z_tao(tao)), 7)):
                J0_list.append(J_0(T, tao, z_tao(tao)))
    print (J0_list)           
    J0_max = max(J0_list)

    print(J0_max)

    print('коэффициент согласованности', round(J0_max/J_0(T_max, tao_max, z0), 5))    


#Shtackelberg_1_invert()






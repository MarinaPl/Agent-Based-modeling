#���������� ������� - 1 �����
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import time
#start = time.time()


    
def Shtackelberg_1():    
    #���������� ����������
    N = 10
    T_min = 5000 #����������� u  (5000-7000)
    T_max = 7000
    tao_min = 0.1 #����� v
    tao_max = 1

    h_T = (T_max - T_min)/N
    h_tao = (tao_max - tao_min)/N
    z0 = 0.1
    z_abs = 0.6 #�� � ��� ���������� - ��� ���������� "�������������" - ��������� 
    a = 0.8 #�����
    #m1 = 1 #�����
    outlay = 0.007
    lambd = - 100000
    lambd_1 = -100 
    salary = 10000
    k_c = 7
    bet = 0.5
    #���������� ������� - �������� 
    def J_0(T, tao, z):
        return (T * tao) * 0.8 * (1 - z) - outlay - lambd * (T ** lambd_1)
    def J_1(T, tao, z):
        return 0.87 * salary * ((1 + z) ** 2) - tao * T * (1 - z) + k_c * (z**bet) * ((tao_max - tao)**(1 - bet))
    def z_tao(tao):
        return round(z0 + a * tao, 5)

    #����
    J0_list = []
    for i_T in range (N):
        T = T_min + i_T * h_T

        J1_list = []
        for i_tao in range (N):
            tao = tao_min + i_tao * h_tao
            J1_list.append(round(J_1(T, tao, z_tao(tao)), 7))
        J1_max = max(J1_list)
        tao_ind = round (J1_list.index(J1_max) * h_tao + tao_min, 7) #����� tao ��� ������� ����������� ��������

        print("��� �������� ������� �������� ��� ������� T", J1_list)
        print("max", max(J1_list)) 
        print("tao ��� ������� max", tao_ind, "������ ����� ��������", J1_list.index(J1_max))
        print("�������� ����������", z_tao(tao_ind))

        if z_tao(tao_ind) > z_abs:
            print("cool")
            J0_list.append(round(J_0(T, tao_ind, z_tao(tao_ind)), 7))
            print("�������� z ��� ����������� tao", z_tao(tao_ind) )
        else:
            print("fale") #���� �� ����������� ������ 4 �� ������ �������� ���������� �� ���� ������ ������� �� ����.��� ����� �� �
            continue 
        print(T) #��-�� continue ������ �������� ������ �� T, ������� ������������� ������� 4
        print("*************************************")
    print("��� ���������� �������� J_0")   
    print(J0_list)  
    print('�������� ������� ������� ������������', max(J0_list))
    #print ('����� ���������� ���������:', time.time() - start, '������')
    print('����������� ���������������', round(max(J0_list)/J_0(T_max, tao_max, z0), 5))
   
#Shtackelberg_1()
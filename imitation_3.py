#обычный Штакельберг, 3 агента - используем равновесие Нэша
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import time
#start = time.time()

#объявление переменных
    
#имитация

def Shtackelberg_3():
    
    N_ag = 3

    N_1, N_2, N_3 = 2, 2, 2    #по агентам - u         для 5 нужно что-то оптимизировать - ошибка i/o
    M_1, M_2, M_3 = 2, 2, 2    #по супервайзеру - v

    v1_min, v2_min, v3_min = 1, 1, 1 
    v1_max, v2_max, v3_max = 3, 3, 3

    u1_min, u2_min, u3_min = 1, 1, 1 
    u1_max, u2_max, u3_max = 3, 3, 3

    h_v1 = round((v1_max - v1_min)/M_1, 3)
    h_v2 = round((v2_max - v2_min)/M_2, 3)
    h_v3 = round((v3_max - v3_min)/M_3, 3)

    h_u1 = round((u1_max - u1_min)/N_1, 3)
    h_u2 = round((u2_max - u2_min)/N_2, 3)
    h_u3 = round((u3_max - u3_min)/N_3, 3)

    z0 = 0.1
    z_abs = 0.6 #то с чем сравниваем - наш показатель "эффективности" - идеальный 

    #определяем функции - тестовые!!!! 
    def J_0(v1, v2, v3, u1, u2, u3):
        return round(v1*u1 + v2*u2 + v3*u3, 5)
    def J1_1(v1, u1):
        return round(v1*v1*u1, 5)
    def J1_2(v2, u2):
        return round(2*v2 + 1/u2, 5)
    def J1_3(v3, u3):
        return round((v3*v3*v3)/ u3, 5)
    def z_current(v1, v2, v3, u1, u2, u3):
         return round(z0 + (v1 + v2 + v3)/10, 5)
         #return round(z0 + u1 * u2 * u3 / (v1 + v2 + v3), 5)



    print('шаги')
    print (h_v1, h_v2, h_v3, h_u1, h_u2, h_u3)
    qt = 0 #"номер комбинации управлений" - счетчик для проверки
    #так как кажому значению функции соответстует набор управлени для хранения наборов, которые яляются 
    #равновесиями Нэша можно использовать словарь {key_qt: [J1, J2, J3, v1, v2, v3, u1, u2, u3]}
    #НО!!! если равновесий Нэша несколько, могут ли целевые функции одного агента для разных равновесий быть равны?? 
    Ji_Nash_dic = {}

    # #берем до m а не m+1 потому что в последний момент времени нам не нужно знать управление

    #все возможные наборы управлений:
    #нужно подумать, почему от 0 до м+1,хотя по идее должно быть 0,1,2 - 3 значения
    # for i_v1 in range (0, M_1 + 1):
    #     v1 = round(v1_min + i_v1 * h_v1, 5)
    #     for i_v2 in range (0, M_2 +1):
    #         v2 = round(v2_min + i_v2 * h_v2, 5)
    #         for i_v3 in range (0, M_3 + 1):
    #             v3 = round(v3_min + i_v3 * h_v3, 5)
    #             for i_u1 in range (0, N_1 + 1):
    #                 u1 = round(u1_min + i_u1 * h_u1, 5)
    #                 for i_u2 in range (0, N_2 + 1):               
    #                     u2 = round(u2_min + i_u2 * h_u2, 5)
    #                     for i_u3 in range (0, N_3 + 1):
    #                         u3 = round(u3_min + i_u3 * h_u3, 5)
    #                         qt += 1
    #                         print(qt, '***', v1,v2,v3,u1,u2,u3)

    # print('STOP', time.time() - start)


    #J0_lst = [] - не нужно
    for i_v1 in range (0, M_1 + 1):
        v1 = round(v1_min + i_v1 * h_v1, 5)
        for i_v2 in range (0, M_2 + 1):
            v2 = round(v2_min + i_v2 * h_v2, 5)
            for i_v3 in range (0, M_3 + 1):
                v3 = round(v3_min + i_v3 * h_v3, 5)
                print("набор управлений супервайзера:", v1, v2, v3)   

                #J1_lst = [] - это может быть нужно использовать для нескольких равновесий Нэша - тогда выбираем то,
                #при котором J0 минимально
                for i_u1 in range (0, N_1 + 1):
                    u1 = round(u1_min + i_u1 * h_u1, 5)

                    #J2_lst = []
                    for i_u2 in range (0, N_2 + 1):               
                        u2 = round(u2_min + i_u2 * h_u2, 5)

                        #J3_lst = []
                        for i_u3 in range (0, N_3 + 1):
                            u3 = round(u3_min + i_u3 * h_u3, 5)
                            print("набор управлений агентов:", u1, u2, u3)
                            qt += 1
                            print(qt)

                            #J3_lst.append(round(J1_3(v3, u3), 5))
                            #J1_lst.append(round(J1_1(v1, u1), 5))
                            #J2_lst.append(round(J1_2(v2, u2), 5))

                            J1_test = round(J1_1(v1, u1), 5)
                            J2_test = round(J1_2(v2, u2), 5)
                            J3_test = round(J1_3(v3, u3), 5)

                            #проверка на Нэша для всех Ji                      
                            J1_Nash_lst = []
                            J2_Nash_lst = []
                            J3_Nash_lst = []

                            #max_J1 = max(J1_lst)
                            #max_J2 = max(J2_lst)
                            #max_J3 = max(J3_lst)
                            #print('max J1', max_J1, 'max J2', max_J2, 'max J3', max_J3)
                            print('TEST: J1', J1_test, ' J2', J2_test, ' J3', J3_test)

                            Nash =  False #флаг

                            for k_1 in range (0, N_1 + 1): 
                                u1_n = round(u1_min + k_1 * h_u1, 5)
                                J1_Nash_lst.append(round(J1_1(v1, u1_n), 5))
                            print('набор значений J1 по управлениям',v1, v2, v3, 'u1_n', u2, u3, 'выглядит следующим образом:', J1_Nash_lst)
                            max_J1_Nash = max(J1_Nash_lst)
                            print(max_J1_Nash)

                            if  J1_test >= max_J1_Nash:
                            #if  max_J1 != max_J1_Nash:
                                Nash = True
                                #print('переходим к следующему шагу из-за J1')
                            else:
                                print('переходим к следующему шагу из-за J1')

                            if Nash:    
                                for k_2 in range (0, N_2 + 1): 
                                    u2_n = round(u2_min + k_2 * h_u2, 5)
                                    J2_Nash_lst.append(round(J1_2(v2, u2_n), 5))
                                print('набор значений J2 по управлениям',v1, v2, v3, u1, 'u2_n', u3, 'выглядит:', J2_Nash_lst)
                                max_J2_Nash = max(J2_Nash_lst)
                                print(max_J2_Nash)
                                if  J2_test < max_J2_Nash:
                                #if  max_J2 != max_J2_Nash :
                                    Nash = False 
                                    print('переходим к следующему шагу из-за J2')

                            if Nash:
                                for k_3 in range (0, N_3 + 1): 
                                    u3_n = round(u3_min + k_3 * h_u3, 5)
                                    J3_Nash_lst.append(round(J1_3(v3, u3_n), 5))
                                print('набор значений J3 по управлениям',v1, v2, v3, u1, u2, 'u3_n', 'равен:',  J3_Nash_lst)
                                max_J3_Nash = max(J3_Nash_lst)
                                print(max_J3_Nash)
                                if  J3_test < max_J3_Nash:
                                #if  max_J3 != max_J3_Nash :
                                    Nash = False  
                                    print('переходим к следующему шагу из-за J3')
                            print(Nash)         

                            #если условия выполнены - добавляем в наш словарь
                            if Nash:
                                if qt not in Ji_Nash_dic.keys():
                                    Ji_Nash_dic[qt] = [J1_test, J2_test, J3_test, v1, v2, v3, u1, u2, u3]
                                print("значение z при оптимальных управлениях", z_current(v1, v2, v3, u1, u2, u3))
                                if z_current(v1, v2, v3, u1, u2, u3) < z_abs:
                                    print("fale_z_current") #если не выполняется уловие 4 мы должны поменять управление то есть просто переход не след.шаг цикла по Т
                            print('******************************************************************')



    #            print('J1:', J1_lst)   
    #            print('J2:', J2_lst) 
    #            print('J3:', J3_lst)                

    print ('общее количество вариантов наборов управлений', qt) 
    for item in Ji_Nash_dic.keys():
        print (item, ':', Ji_Nash_dic[item])
        #словари не упорядочены по порядку(ключу), поэтому печать не зависит от порядкового номера
    print('количество наборов оптимальных управлений агентов:', len(Ji_Nash_dic))   

    #теперь на основе этого набора значений, которые подходят агентам находим оптимальное для супервайзера. 
    #набор его гарантированных выигрыш определяестся в поиске р. Нэш, сейчас из них выбираем max

    J0_dic = {} 
    for item in Ji_Nash_dic.keys():
        if item not in J0_dic.keys():
            #J_0(v1, v2, v3, u1, u2, u3):
            J0_dic[item] = J_0(Ji_Nash_dic[item][3], Ji_Nash_dic[item][4], Ji_Nash_dic[item][5], Ji_Nash_dic[item][6], Ji_Nash_dic[item][7], Ji_Nash_dic[item][8])

    print('значение целевой ф. ведущего')  
    #for item in J0_dic.keys():
    #    print(J0_dic[item])

    #print('min J0_dic', min(J0_dic.values()))   
    #min_J0 = min(J0_dic.values())

    print('max J0_dic', max(J0_dic.values()))   
    max_J0 = max(J0_dic.values())

    #проверка на совпадение значений: если несколько одинаковых J0 для разных наборов управлений - печатаем все
    for item in J0_dic.keys():
        if J0_dic[item] == max_J0:
        #if J0_dic[item] == min_J0:
            print(item, 'набор управлений:', Ji_Nash_dic[item][3], Ji_Nash_dic[item][4], Ji_Nash_dic[item][5], Ji_Nash_dic[item][6], Ji_Nash_dic[item][7], Ji_Nash_dic[item][8])
            print('для этого набора значение показателя равно:', z_current(v1, v2, v3, u1, u2, u3))
            print('коэффициент согласованности', round(J_0(v1_max, v2_max, v3_max, u1_max, u2_max, u3_max)/J0_dic[item], 5))
            if z_current(v1, v2, v3, u1, u2, u3) < z_abs:
                print("Не выполняется условие устойчивого развития")


    #print ('время выполнения программы:', time.time() - start)  
    
    
#Shtackelberg_3()                


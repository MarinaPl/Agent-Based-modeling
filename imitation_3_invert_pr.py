#3 агента, принуждение, обратный Штакельберг
#Штакельберг с обратной связью по управлению, один супервайзер, 3 агента
import numpy as np

#функция имитации
def Shtackelberg_3_invert_pr():
    
    N_ag = 3
    #принуждение работает
    N_1, N_2, N_3 = 2, 2, 2    #по агентам - u         
    M_1, M_2, M_3 = 2, 2, 2    #по супервайзеру - v

    v1_min, v2_min, v3_min = 1, 1, 1 
    v1_max, v2_max, v3_max = 3, 3, 3

    u1_min, u2_min, u3_min = 1, 1, 1 
    u1_max, u2_max, u3_max = 3, 3, 3

    h_v1 = round((v1_max - v1_min)/M_1, 3)
    h_v2 = round((v2_max - v2_min)/M_2, 3)
    h_v3 = round((v3_max - v3_min)/M_3, 3)

    #h_u1 = round((u1_max - u1_min)/N_1, 3)
    #h_u2 = round((u2_max - u2_min)/N_2, 3)
    #h_u3 = round((u3_max - u3_min)/N_3, 3)

    z0 = 5
    z_abs = 10 #то с чем сравниваем - наш показатель "эффективности" - идеальный 

    #определяем функции - тестовые пока
    def J_0(v1, v2, v3, u1, u2, u3):
        return round(v1*u1 + v2*u2 + v3*u3, 5)
    def J1_1(v1, u1):
        return round(v1*v1*u1, 5)
    def J1_2(v2, u2):
        return round(2*v2 + 1/u2, 5)
    def J1_3(v3, u3):
        return round((v3*v3*v3)/ u3, 5)
    def z_current(v1, v2, v3, u1, u2, u3):
        return round(z0 + v1 + v2 + v3, 5)

    
    
    
    print('шаги')
#    print (h_v1, h_v2, h_v3, h_u1, h_u2, h_u3)
    #аналогично обычному Штакельбергу - Нэш, потом ищем стратегию наказания
    qt = 0 #"номер комбинации управлений" - счетчик для проверки
    
    Ji_Nash_dic = {}
    for i_v1 in range (0, M_1 + 1):
        v1 = round(v1_min + i_v1 * h_v1, 5)
        for i_v2 in range (0, M_2 + 1):
            v2 = round(v2_min + i_v2 * h_v2, 5)
            for i_v3 in range (0, M_3 + 1):
                v3 = round(v3_min + i_v3 * h_v3, 5)
                print("набор управлений супервайзера:", v1, v2, v3)   

                #J1_lst = [] - это может быть нужно использовать для нескольких равновесий Нэша - тогда выбираем то,
                #при котором J0 минимально
                h_u1 = round((u1_max - v1)/N_1, 3)
                for i_u1 in range (0, N_1 + 1):
                    u1 = round(v1 + i_u1 * h_u1, 5)

                    #J2_lst = []
                    h_u2 = round((u2_max - v2)/N_1, 3)
                    for i_u2 in range (0, N_2 + 1):               
                        u2 = round(v2 + i_u2 * h_u2, 5)

                        #J3_lst = []
                        h_u3 = round((u3_max - v3)/N_1, 3)
                        for i_u3 in range (0, N_3 + 1):
                            u3 = round(v3 + i_u3 * h_u3, 5)
                            print("набор управлений агентов:", u1, u2, u3)
                            qt += 1
                            print(qt)

                            J1_test = round(J1_1(v1, u1), 5)
                            J2_test = round(J1_2(v2, u2), 5)
                            J3_test = round(J1_3(v3, u3), 5)

                            #проверка на Нэша для всех Ji                      
                            J1_Nash_lst = []
                            J2_Nash_lst = []
                            J3_Nash_lst = []

                            print('TEST; J1', J1_test, ' J2', J2_test, ' J3', J3_test)

                            Nash =  False #флаг

                            for k_1 in range (0, N_1 + 1): 
                                u1_n = round(v1 + k_1 * h_u1, 5)
                                J1_Nash_lst.append(round(J1_1(v1, u1_n), 5))
                            print('набор значений J1 по управлениям',v1, v2, v3, 'u1_n', u2, u3, 'выглядит следующим образом:', J1_Nash_lst)
                            max_J1_Nash = max(J1_Nash_lst)
                            print(max_J1_Nash)

                            if  J1_test >= max_J1_Nash:
                                Nash = True
                            else:
                                print('переходим к следующему шагу из-за J1')

                            if Nash:    
                                for k_2 in range (0, N_2 + 1): 
                                    u2_n = round(v2 + k_2 * h_u2, 5)
                                    J2_Nash_lst.append(round(J1_2(v2, u2_n), 5))
                                print('набор значений J2 по управлениям',v1, v2, v3, u1, 'u2_n', u3, 'выглядит:', J2_Nash_lst)
                                max_J2_Nash = max(J2_Nash_lst)
                                print(max_J2_Nash)
                                if  J2_test < max_J2_Nash:
                                    Nash = False 
                                    print('переходим к следующему шагу из-за J2')

                            if Nash:
                                for k_3 in range (0, N_3 + 1): 
                                    u3_n = round(v3 + k_3 * h_u3, 5)
                                    J3_Nash_lst.append(round(J1_3(v3, u3_n), 5))
                                print('набор значений J3 по управлениям',v1, v2, v3, u1, u2, 'u3_n', 'равен:',  J3_Nash_lst)
                                max_J3_Nash = max(J3_Nash_lst)
                                print(max_J3_Nash)
                                if  J3_test < max_J3_Nash:
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
    
    print ('общее количество вариантов наборов управлений', qt) 
    for item in Ji_Nash_dic.keys():
        print (item, ':', Ji_Nash_dic[item])
        #словари не упорядочены по порядку(ключу), поэтому печать не зависит от порядкового номера
    print('количество вариантов:', len(Ji_Nash_dic))   #'количество равновесий:'
      
    #тут уже найдены равновесия для каждого набора управлений супервайзера
    #ищем стратегию наказания
    
    J0_dic = {} 
    for item in Ji_Nash_dic.keys():
        if item not in J0_dic.keys():
            #J_0(v1, v2, v3, u1, u2, u3):
            J0_dic[item] = J_0(Ji_Nash_dic[item][3], Ji_Nash_dic[item][4], Ji_Nash_dic[item][5], Ji_Nash_dic[item][6], Ji_Nash_dic[item][7], Ji_Nash_dic[item][8])

    print('выигрыш ведущего')
    print (min(J0_dic.values()))  #'min J0_dic 
    min_J0 = min(J0_dic.values())
    
        #проверка на совпадение значений: если несколько одинаковых J0 для разных наборов управлений - печатаем все
    for item in J0_dic.keys():
        if J0_dic[item] == min_J0:
            print(item, 'набор управлений:', Ji_Nash_dic[item][3], Ji_Nash_dic[item][4], Ji_Nash_dic[item][5], Ji_Nash_dic[item][6], Ji_Nash_dic[item][7], Ji_Nash_dic[item][8])
            print('для этого набора значение показателя равно:', z_current(v1, v2, v3, u1, u2, u3))
            #L[i]- гарантированный выигрыш i-го агента
            print('значение целевой функции 1-го агента для текущих управлений', J1_1(Ji_Nash_dic[item][3], Ji_Nash_dic[item][6]))
            print('значение целевой функции 2-го агента для текущих управлений', J1_2(Ji_Nash_dic[item][4], Ji_Nash_dic[item][7]))
            print('значение целевой функции 3-го агента для текущих управлений', J1_3(Ji_Nash_dic[item][5], Ji_Nash_dic[item][8]))
            print('коэффициент согласованности', round(J_0(v1_max, v2_max, v3_max, u1_max, u2_max, u3_max)/J0_dic[item], 5))
            if z_current(v1, v2, v3, u1, u2, u3) < z_abs:
                print("Не выполняется условие устойчивого развития")
                    
#вызов ф-ции    
  
#Shtackelberg_3_invert_pr()









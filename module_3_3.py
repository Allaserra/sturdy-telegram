                      #Задача "Распаковка":
     #   1.Функция с параметрами по умолчанию:

def  print_params(a=1,b='строка',c=True):
    print(a,b,c)
print_params(1,'rere',True)
print_params(1,25,True)
print_params(1,'ay',[1,2,3])
print_params()

        # 2.Распаковка параметров:

def  print_params(a=1,b='строка',c=True):
    return a,b,c
values_list = [2, [22, 33, 444], 'python']
values_dict = {'a':25,'b':'слово','c':False}
print(*print_params(* values_list))
print(*print_params(** values_dict))

#  3.Распаковка + отдельные параметры:

values_list_2 = ['python',99]
print(print_params(*values_list_2, 42))
print(*print_params(*values_list_2, 42))

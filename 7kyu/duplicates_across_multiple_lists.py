'''
Given multiple lists (name, age, height), each of size n :

An entry contains one name, one age and one height. The attributes corresponding to each entry are determined by the index of each list.
For example, the first entry is comprised of the first elements of each list, the second entry is comprised of the second elements of each list, etc.

A duplicate entry is one in which the name, age and height are ALL the same.

Write a function which takes in the attributes for each entry and returns an integer for the number of duplicated entries.
For a set of duplicates, the original entry should not be counted as a duplicate.
'''

'''
Cada lista tiene n elementos, la entrada se obtiene del indice de cada lista,
se considera un elemento repetido el que el nombre, edad, y altura coincida con otro.

Escribe una funcion que devuelva un integer con el numero de duplicados. No debe contarse el duplicado original.
'''

#Muy lento

# def test_count_duplicates(name,age,height):
#     total = 0
#     i = 0
#     while i < len(name):
#         j = i+1
#         while j < len(name):
#             if (name[i], age[i], height[i]) == (name[j], age[j], height[j]):
#                 total+=1
#                 name.pop(j)
#                 age.pop(j)
#                 height.pop(j)
#             else:
#                 j+=1
#         i+=1
#     return total


#Muy lento

# def count_duplicates(name,age,height):
#     new_list = list(zip(name,age,height))
#     total = 0
#     ignorar = list()
#     x = 0
#     while x < len(name):
#         if x in ignorar:
#             x+=1
#         else:
#             y = x+1
#             while y < len(name):
#                 print(f'COMPARA PARA x: {x} -- VALOR: {new_list[x]} CON: {new_list[y]} PARA UN y: {y}')
#                 if y in ignorar:
#                     pass
#                 elif new_list[x] == new_list[y]:
#                         ignorar.append(y)
#                         total += 1
#                 y+=1
#             x+=1
#     print(total)
#     return total

def count_duplicates(name,age,height):
    lista_zip = list(zip(name,age,height))
    conjunto = set(zip(name,age,height))
    repetidos = len(lista_zip) - len(conjunto)
    return repetidos


if __name__ == "__main__":
    name = ['John','Beth','Beth','Beth','Bill','Bill']
    age = [37,23,23,23,46,46]
    height = [183,170,170,170,175,175]
    count_duplicates(name,age,height)
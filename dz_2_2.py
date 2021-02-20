lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_item = []
i = 0
my_list = []
while i < len(lst):
    list_item = ''.join(lst[i])
    idx = 0
    id = 0
    new_lst = []
    while idx < len(list_item):
        if list_item[idx].isdigit() == True:
            if len(list_item) == 1:
                list_item = f'"0{list_item}"'
                break
            elif list_item[idx].isdigit() == True and list_item[0] == "+": #len(list_item[1:]) == 1:
                list_item = f'"{list_item[0]}0{list_item[1:]}"'
                id += 1
                break
            else:
                list_item = f'"{list_item}"'
                #new_lst.append(list_item)
                #print(new_lst)
                break
        idx = idx + 1
    i += 1
    my_list.append(list_item)
print(f'Новый список - {my_list}')

rez_new = ""
for idx,list_item in enumerate(my_list):
    rez_new += f"{list_item} "
print(f'Новоя строка: {rez_new}')
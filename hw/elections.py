# Выборы в США

dict_vote = {}
n = int(input())                                             # количество записей
for i in range(n):
    name_vote = str(input())
    name, vote = [str(j) for j in name_vote.split()]         # разделяем строку на имя и голоса
    if name in dict_vote.keys():
        dict_vote.get(name)[0] += int(vote)                  # суммируем голоса для уже существующего ключа
    else:
        dict_vote.setdefault(name)                           # добавляем значение ключа, если его нет
        dict_vote[name] = [int(vote)]                        # добавляем количество голосов

list_name = list(dict_vote.keys())                           # добавляем значения ключей в список
list_name.sort()                                             # сортируем в алфавитном порядке
for k in list_name:                                          # выводим список Имя Количество_голосов
    print(k, *dict_vote[k])

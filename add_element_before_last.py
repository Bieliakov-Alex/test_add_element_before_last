# демонстрация добавления элемента в список перед последним

test_list = [-1]
print(test_list)
print(test_list[-1])  # вывод последнего элемента списка
test_list.insert(-1, 2)  # для добавления перед последним в списке используется индекс -1
print(test_list)
test_list.insert(-1, 3)
print(test_list)
test_list.insert(-1, 4)
print(test_list)

# проверка при пустом списке
test_list = []
test_list.insert(-1, 1)  # тогда добавляется в конец
print(test_list)

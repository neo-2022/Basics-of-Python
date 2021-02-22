"""2. Дан список:
 ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
    Сформировать из обработанного списка строку:
          в "05" часов "17" минут температура воздуха была "+05" градусов
    Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
    Как модифицировать это условие для чисел со знаком?
    Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
    Главное: дополнить числа до двух разрядов нулём! """

myList = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
b = 0
for i, j in enumerate(myList):
    c = list(j)
    sum_num = 0
    # Сделаем проверку и добавим нули только для чисел с одним разрядом
    for n in c:
        if n.isdigit():
            sum_num += 1
    if sum_num == 1:
        c.insert(- 1, '0')
        myList[i] = ''.join(c)
    if i >= b:
        for jj in c:
            # Добавим кавычки
            if jj.isdigit():
                myList.insert(i, '"')
                myList.insert(i + 2, '"')
                b = i + 2
                break
print(' '.join(myList))

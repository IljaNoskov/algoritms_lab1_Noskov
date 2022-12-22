# Лабораторная работа по алгоритмам и структурам данных №1. 
### Выполнил Носков Илья 21ПИ1.
Все графики и таблицы, помимо скринов, будут доступны по ссылке  https://docs.google.com/spreadsheets/d/178wBsA4Ej7er1Lw6KCcvod7N_EzcOONQ4hkRDZkI2FI/edit?usp=sharing
Также один из файлов является копией этой таблицы.
Код запускал в IDLE, python 3.10.
# Коды алгоритмов.
### Генерация матриц.
Генерация первой матрицы:
A[i][k]=(N/M*i+k)*2;
target=2*N+1.
```python
def make_matrix_1(bar,string):
    matrix=[]
    for i in range(bar):
        matrix.append([])
    for i in range(bar):
        for k in range(string):
            matrix[i].append((string/bar*i+k)*2)
    return 2*(string)+1,matrix
```
Генерация второй матрицы:
A[i][k]=(N/M*i*k)*2;
target=16*N+1.
```python
# генерация матрицы 2
def make_matrix_2(bar,string):
    matrix=[]
    for i in range(bar):
        matrix.append([])
    for i in range(bar):
        for k in range(string):
            matrix[i].append(((string)/bar*i*k)*2)
    return 16*(string)+1,matrix
```
### Бинарный поиск.
#### Оценка времени работы - O(N*log(M))
Бинарный поиск в массиве
```python
def bins(arr,start,stop,n):
    mid=(start+stop)//2
    #print(start,stop,mid, len(arr))
    if start>stop:
        return([-1,start])
        print(mid)
    if n==arr[mid]:
        return([1,mid])
    elif n<arr[mid]:
        return(bins(arr,start,mid-1,n))
    else:
        return(bins(arr,mid+1,stop,n))
```
Бинарный поиск в матрице. Идём по каждой строке, пока не найдём наш элемент. По строке ищем бинарным поиском.
```python
def find_matrix(matrix,bar_n,string_n,num):
    for i in range(bar_n):
        n=bins(matrix[i],0,string_n,num)
        if n[0]==1:
            return(i,n[1]," - Индексы нашего элемента")
    return("Элемента в матрице нет")
```
### Поиск "Лесенкой".
#### Оценка времени работы - O(N+M)
Начинаем поиск из правого верхнего угла, в зависимости от сравнения текущего элемента идём либо вниз (если нужен элемент больше), либо влево (если нужен элемент меньше).
```python
def find_lest(matrix,bar_n,string_n,num):
    i=0
    j=string_n-1
    while i<=(bar_n-1) and j>=0:
        if num!=matrix[i][j]:
            if num>matrix[i][j]:
                i+=1
            else:
                j-=1
        else:
            return(i,j,"- Индексы нашего элемента")
    return("Элемента в матрице нет")
```
### Экспоненциальный поиск "Лесенкой"
#### Оценка времени работы O(log(N)-log(M)+1)
Экспоненциальный поиск в массиве. Двинаем размеры диапазона согласно экспоненциальному. Как нашли диапазон, ищем в нём уже бинарным.
```python
def exp_serch(arr,start,end,num,exp=1):
    s_end=min(start+2**exp,end)
    if arr[s_end]==num:
        return [1,s_end]
    elif arr[s_end]>num or s_end==end:
        return bins(arr,start,s_end,num)
    else:
        return exp_serch(arr,s_end,end,num,exp+1)
```

Начинаем поиск с поиска строки, выше которой точно находиться наше число. А далее идём вверх до конца матрицы, или же до строки, последнее число которой менше нашего элемента. Ну или пока не найдём наш элемент.
```python
def exp_s_matrix(matrix,bar_len,string_len,num):
    rez=exp_serch(matrix[0],0,string_len,num)
    #print(rez)
    if rez[0]==1:
        return 'Элемент найден',rez[1],0
    for i in range(1,bar_len):
        #print (i,rez[1])
        rez=exp_serch(matrix[i],0,rez[1]-1,num)
        if rez[0]==1 or (rez[1]==0 and matrix[i][0]>num):
            return i,rez[1]
```

# Результаты и выводы.
Все графики смотрите по ссылке на гугл диск, тут лишь основные - log сравнение трёх алгоритмов на первой матрице и log сравнение эксп. поиска на 1 и 2 матрице.
https://docs.google.com/spreadsheets/d/178wBsA4Ej7er1Lw6KCcvod7N_EzcOONQ4hkRDZkI2FI/edit?usp=sharing
### Алгоритмы на 1 матрице.
<img width="438" alt="image" src="https://user-images.githubusercontent.com/99073996/209152701-9083006d-f69f-4356-86bf-1c56cdd1bbf4.png">
<img width="416" alt="image" src="https://user-images.githubusercontent.com/99073996/209152762-95e3a0aa-59cd-4c3f-962e-bcfb3e5e32f8.png">

### Вывод по первому графику
1) Лесенка ожидаемо оказалась быстрее на более "квадратных" матрицах. А бинарный и экспоненциальные поиски оказались быстрее на более узких матрицах.
2) Бинарный и экспоненциальный поиск оказались очень похожи по времени выполнения, но экспоненциальный поиск становиться заметно быстрее на данных с большим количеством строк - он может закончиться заранеe, не просматривая всю таблицу. Я бинарный нет.
3) Неожиданно, бинарный и логарифмический поиски по времени растут почти одинаково, хотя у эксп. имеется оптимизация, сокращающая количество проверенных строк.
4) Лесенка показала очень странный рост после проверки на первой строке. Думаю, дело в том, что алгоритм в этом случае сразу понимает, что таргета в строке нет и пишет об его отсутствии, не пробегая по всей строке.

### Экспоненциальный поиск на 1 и 2 матрицах.
<img width="441" alt="image" src="https://user-images.githubusercontent.com/99073996/209152851-d7305df3-b032-4cec-8991-ec57dbcb59c2.png">
<img width="445" alt="image" src="https://user-images.githubusercontent.com/99073996/209152908-d056f7c2-6da5-46af-8032-b57cc15e3797.png">

### Выводы по второму графику
1) Мы видим, что поиск на втрой матрице заметно быстрее, начиная матрицы размером с 4х строк и более. Это получается благодаря возможности закончить поиск заранее. Из-за особенностей заполнение матрицы такое встречается только в о втором случае.
2) Рост обоих графиков всё равно логарифмический, как и ожидалось


# Лабораторная работа по алгоритмам и структурам данных №1. 
### Выполнил Носков Илья 21ПИ1.
Все графики и таблицы, помимо скринов, будут доступны по ссылке [https://docs.google.com/spreadsheets/d/1kYcRv7BlsV4xKhjwWECqlUIWNOCdl0h3meINKqnm-dc/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1O7C6GYKZfmwLcnTAWSsHm-Yq3RG5AUnM2H3ZAyKF3UM/edit?usp=sharing)
Также один из файлов является копией этой таблицы.
Код запускал в IDLE, python 3.7.8.
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
def exp_search(arr,start,end,num,exp=1):
    s_end=min(start+2**exp,end)
    #print(start,s_end,num,arr[s_end])
    if arr[s_end]>=num or s_end==end:
        return bin_search(arr,start,s_end,num)
    else:
        #print(exp+1)
        return exp_search(arr,s_end,end,num,exp+1)
```

Начинаем поиск из верхнего правого угла, в зависимости от сравнения текущего элемента начинаем поиск либо вниз (если нужен элемент больше), либо влево (если нужен элемент меньше).
```python
def exp_matrix_s(matrix,bar,string,num):
    i=0
    j,rez=exp_search(matrix[0],0,string,num)
    #print(j,rez,num,matrix[i][j+1])
    while (i<bar and j<string and j>=0 and rez==False):
        if bar==2**13:
            print(i,j)
        if num>matrix[i][j]:
            i,rez=exp_search_bar(matrix,i,num,j)
        else:
            j,rez=exp_search(matrix[i],0,j,num)
        #print(i<bar,rez==False)
    if rez==True:
        return i,j
    else:
        return "В матрице нет такого элемента"
```

# Результаты.
Смотрите по ссылке на гугл диск
[https://docs.google.com/spreadsheets/d/1kYcRv7BlsV4xKhjwWECqlUIWNOCdl0h3meINKqnm-dc/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1O7C6GYKZfmwLcnTAWSsHm-Yq3RG5AUnM2H3ZAyKF3UM/edit?usp=sharing)

# Выводы
1) Бинарный поиск ожидаемо самый медленный на квадратных данных, но самый быстрый на "узкой" матрице
2) Лесенка показала странный результат, почти равный 0 на массиве. Видимо, таргет был больше последнего элемента массива и алгоритм сразу понял, что элемента в матрице нет
3) Алгоритмы не показывают значительной разницы на разных данных. Думаю, дело в том, что бинарным поиском я всё равно просматриваю каждую строку, а для экспоненциального начинаю поиск сначала по строке
4) Что график лестничного алгоритма, что график бинарного, показывают красивые графики, а экспоненциальный постоянно ломаются. Возможно, имеется ошибка в экспоненциальном алгоритме, но выявить её не удалось.
5) Бинарный ожидаемо растёт также, как и количество строк.
6) Лесенка показывает Небольшой рост, так как один из коэффицентов уже с 0 имеет одну из констант равной 2^13


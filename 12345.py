import time

# Длина строк - константа
string_len=2**13
max_bar_len=2**13

#функция для печати матриц (нужна была для проверки правильности заполнения)
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])
#print_matrix(matrix)
        
#бинарный поиск в массиве
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
#поиск элемента в матрице при помощи бинарного поиска
def find_matrix(matrix,bar_n,string_n,num):
    for i in range(bar_n):
        n=bins(matrix[i],0,string_n,num)
        if n[0]==1:
            return(i,n[1]," - Индексы нашего элемента")
    return("Элемента в матрице нет")

# поиск элемента матрицы при помощи лестницы
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

#экспоненциальный поиск в массиве
def exp_search(arr,start,end,num,exp=1):
    s_end=min(start+2**exp,end)
    #print(start,s_end,num,arr[s_end])
    if arr[s_end]>=num or s_end==end:
        return bin_search(arr,start,s_end,num)
    else:
        #print(exp+1)
        return exp_search(arr,s_end,end,num,exp+1)
# эксп. поиск в столбик  
def exp_search_bar(matrix,start,num,ind,exp=1):
    s_end=min(start+2**exp,len(matrix)-1)
    if matrix[s_end][ind]>=num or (s_end==len(matrix)-1):
        #print(bin_search_bar(matrix,start,s_end,num,ind))
        return bin_search_bar(matrix,start,s_end,num,ind)
    else:
        #print(exp+1)
        return exp_search_bar(matrix,s_end,num,ind,exp+1)
    
# бинарны поиск в строчку. Да, ещё один, просто писал разные куски кода с дистанцией в неделю, легче было написать с 0, чем редактировать
def bin_search(arr,start,end,num):
    mid=(start+end)//2
    #print(start,end,mid)
    if arr[mid]==num:
        return mid,True
    if start>=end:
        while arr[end]>num and end>0:
            end-=1
        return end,False
    if arr[mid]>num:
        return bin_search(arr,start,mid-1,num)
    else:
        return bin_search(arr,mid+1,end,num)
# бинарный поиск в столбик
def bin_search_bar(matrix,start,end,num,ind):
    mid=(start+end)//2
    #print(start,end,mid)
    if matrix[mid][ind]==num:
        return mid,True
    if start>=end:
        while matrix[end][ind]>num and end>0:
            end-=1
        return end,False
    if matrix[mid][ind]>num:
        return bin_search_bar(matrix,start,mid-1,num,ind)
    else:
        return bin_search_bar(matrix,mid+1,end,num,ind)
# эксп. поиск в матрице (при помощи лесенки
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


# переменные в которых степень 2 и основание
step=0
bar=2
# генерация матрицы 1
def make_matrix_1(bar,string):
    matrix=[]
    for i in range(bar):
        matrix.append([])
    for i in range(bar):
        for k in range(string):
            matrix[i].append((string/bar*i+k)*2)
    return 2*(string)+1,matrix
# генерация матрицы 2
def make_matrix_2(bar,string):
    matrix=[]
    for i in range(bar):
        matrix.append([])
    for i in range(bar):
        for k in range(string):
            matrix[i].append(((string)/bar*i*k)*2)
    return 16*(string)+1,matrix
# основной код. Порядок вывода - степень, время бинарным, лесенкой и эксп.
print('start task 1')
flag=0
while step<13:
    if flag>=1:
        flag=0
        step+=1
    #Пересчитываю количество строк (то есть длину столбцов)
    bar_len=bar**step
    #заполняю матрицу (можно изменить цифру)
    n,matrix=make_matrix_1(bar_len,string_len)
    #print(matrix)
    print(step,end=' ')
    #считаю время поиска бинарным
    start_time = time.time()
    for i in range(1000):
        binar=['число',n,find_matrix(matrix,bar_len,string_len-1,n)]
    print((time.time()-start_time)/1000,end=' ')
    #print(binar)
    #считаю время поиска лесенкой
    start_time = time.time()
    for i in range(1000):
        linear=['число',n,find_lest(matrix,bar_len,string_len,n)]
    print((time.time()-start_time)/1000,end=' ')
    #print(linear)
    #считаю время поиска эксп. лесенкой
    start_time = time.time()
    for i in range(1000):
        exp=['число',n,exp_matrix_s(matrix,bar_len-1,string_len-1,n)]
    print((time.time()-start_time)/1000)
    #print(exp,'\n')
    #увеличиваю степень 2, а значит и размер таблицы
    flag+=1

# аналогичный код, но для второй матрицы
print('start task 2')
flag=0
step=0
while step<13:
    if flag>=1:
        flag=0
        step+=1
    #Пересчитываю количество строк (то есть длину столбцов)
    bar_len=bar**step
    #заполняю матрицу (можно изменить цифру)
    n,matrix=make_matrix_2(bar_len,string_len)
    #print(matrix)
    print(step,end=' ')
    #считаю время поиска бинарным
    start_time = time.time()
    for i in range(1000):
        binar=['число',n,find_matrix(matrix,bar_len,string_len-1,n)]
    print((time.time()-start_time)/1000,end=' ')
    #print(binar)
    #считаю время поиска лесенкой
    start_time = time.time()
    for i in range(1000):
        linear=['число',n,find_lest(matrix,bar_len,string_len,n)]
    print((time.time()-start_time)/1000,end=' ')
    #print(linear)
    #считаю время поиска эксп. лесенкой
    start_time = time.time()
    for i in range(1000):
        exp=['число',n,exp_matrix_s(matrix,bar_len-1,string_len-1,n)]
    print((time.time()-start_time)/1000)
    #print(exp,'\n')
    #увеличиваю степень 2, а значит и размер таблицы
    flag+=1   

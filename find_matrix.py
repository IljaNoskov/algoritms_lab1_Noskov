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

def exp_serch(arr,start,end,num,exp=1):
    s_end=min(start+2**exp,end)
    if arr[s_end]==num:
        return [1,s_end]
    elif arr[s_end]>num or s_end==end:
        return bins(arr,start,s_end,num)
    else:
        return exp_serch(arr,s_end,end,num,exp+1)
    
def bins_bar(matrix,bar_ind,start,end,num):
    mid=(start+end)//2
    #print(mid)
    if start>end:
        return([-1,start])
    if num==matrix[mid][bar_ind]:
        return([1,mid])
    elif num<matrix[mid][bar_ind]:
        #print('ищу выше',num,matrix[mid][bar_ind])
        return(bins_bar(matrix,bar_ind,start,mid-1,num))
    else:
        #print('ищу ниже')
        return(bins_bar(matrix,bar_ind,mid+1,end,num))
    
def exp_search_bar(matrix,bar_ind,start,end,num,exp=0):
    s_end=min(start+2**exp,end)
    if matrix[s_end][bar_ind]==num:
        return ([1,s_end])
    if matrix[s_end][bar_ind]>num or s_end==end:
        return bins_bar(matrix,bar_ind,start,s_end,num)
    else:
        return exp_search_bar(matrix,bar_ind,s_end,end,num,exp+1)

def exp_s_matrix(matrix,bar_len,string_len,num):
    rez=exp_search_bar(matrix,0,0,bar_len,num)
    #print(rez)
    if rez[0]==1:
        return 'Элемент найден',rez[1],0
    for i in range(min(rez[1],bar_len),-1,-1):
        #print(i)
        if matrix[i][-1]<num:
            #print(num,matrix[i][-1])
            return -1
        rez=exp_serch(matrix[i],0,string_len,num,)
        #print(rez)
        if rez[0]==1:
            return 1,i,rez[1]


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
        exp=['число',n,exp_s_matrix(matrix,bar_len-1,string_len-1,n)]
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
        exp=['число',n,exp_s_matrix(matrix,bar_len-1,string_len-1,n)]
    print((time.time()-start_time)/1000)
    #print(exp,'\n')
    #увеличиваю степень 2, а значит и размер таблицы
    flag+=1   

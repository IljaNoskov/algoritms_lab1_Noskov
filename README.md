# algoritms_lab1_Noskov
Все графики и таблицы, помимо скринов, будут доступны по ссылке https://docs.google.com/spreadsheets/d/1O7C6GYKZfmwLcnTAWSsHm-Yq3RG5AUnM2H3ZAyKF3UM/edit?usp=sharing
Также один из файлов является копией этой таблицы.
Код запускал в IDLE, python 3.7.8.
### Коды алгоритмов
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
            matrix[i].append((max_bar_len/string*i+k)*2)
    return 2*(max_bar_len)+1,matrix
```
Генерация второй матрицы:
A[i][k]=(N/M*i*k)*2;
target=16*N+1.
```python
def make_matrix_2(bar,string):
    matrix=[]
    for i in range(bar):
        matrix.append([])
    for i in range(bar):
        for k in range(string):
            matrix[i].append(((max_bar_len)/string*i*k)*2)
    return 16*(max_bar_len)+1,matrix
```

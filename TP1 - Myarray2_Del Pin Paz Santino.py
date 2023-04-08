class Myarray2():
    def __init__(self, lista, r, c, by_row = True):
        ''' Inicializador de la clase, que toma los siguientes argumentos:
            Inputs:
                1 - "lista" es una matriz almacenada en forma de lista (puede estar ordenada
                por filas o por columnas).
                2 - "r" es la cantidad de filas de la matriz.
                3 - "c" es la cantidad de columnas de la matriz.
                4 - "by_row" es un booleano (default = True), que sirve para indicar si la matriz
                se recorre según filas (by_row = True) o según columnas (by_row = False).
        '''
        self.elems = lista
        self.r = r
        self.c = c
        self.by_row = by_row

    def get_pos(self, j, k):
            ''' Calculo de la posición que una coordenada (j, k) tiene en la lista elems.
            Inputs:
                1 - "j" elemento de la coordenada que indica la fila.
                2 - "k" elemento de la coordenada que indica la columna.
                En esta función, la lista elems no se altera, pero cambia la forma en que se visibiliza la matriz, pero
                aún así esta se lee como se lee en la lista.
            Outputs:
                1 - "position" es el índice de un elemento de la matriz almacenada, en este caso, como lista de listas.
                    El mismo se devuelve en un entero de tipo (int).
            '''
            if (j < 0 or j >= self.r) or (k < 0 or k >= self.r):
                raise ValueError('El índice está fuera de los límites de la matriz')
            if self.by_row == True:
                position = j * self.c + k
            else:
                position = k * self.r + j
            return position

    def get_coords(self, m):
        ''' Dado el índice "m" de un elemento que tiene en la matriz almacenada como lista de listas, calcula
            las coordenadas que este elemento tiene en la matriz
            Inputs:
                1 - "m" es la posición de una coordenada (j, k) en la lista "elems". Notar
                que "m" NO es un elemento propio de la matriz sino la posición del mismo.  
            Outputs:
                1 - Esta función devuelve una tupla "(j, k)" según el orden de lectura de la matriz, indicando
                    las coordenadas que tiene un índice "m" en la matriz.
        '''
        lista = self.elems.copy()
        if m < 0 or m >= (len(lista)*len(lista[0])):
            raise ValueError('El índice "m" que está tratando de utilizar se encuentra fuera de los límites de la matriz')
        if self.by_row == True:
            j =  m // self.c
            k =  m % self.c
        else:
            j = m // self.r
            k = m % self.r
        return (j, k)

    def switch(self):
        ''' Esta función no recibe argumentos, y cambia la lista "elems" (o el nombre asignado a la lista en la que se
            almacena la matriz) y el valor de verdad de "by_row". Por ejemplo, si la lista en la que se almacena la matriz
            es elems = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], con by_row = True, al aplicar la función "switch()", debería
            devolver elems = [[1, 4, 7], [2, 5, 8], [3, 6, 9]] con by_row = False.
            Outputs:
                1 - Devuelve un nuevo objeto de la clase con la misma matriz, alterando la lista elems, y cambiando el valor de by_row.
        '''
        aux = self.elems.copy()
        if self.by_row:
            switched_elems = [[] for x in range(self.c)]
            for j in range(self.r):
                for k in range(self.c):
                    switched_elems[k].append(aux[j][k])
        else:
            switched_elems = [[] for x in range(self.c)]
            for j in range(self.r):
                for k in range(self.c):
                    switched_elems[k].append(aux[j][k])
        new_by_row = not self.by_row
        return self.__class__(switched_elems, self.c, self.r, new_by_row)

    def get_row(self, j):
        ''' Devuelve el contenido de la fila j (sus elementos) en forma de una lista. En el caso que by_row = False,
            esta función utiliza otro método ya creado, get_pos(j, k), ya que este devuelve el índice de un par de
            coordenadas en la matriz, lo que se utiliza para agregar el elemento deseado a la lista row.
            Inputs:
                1 - "j" es un entero (int) >= 0 que indica la fila que se quiere mostrar al finalizar la 
                    ejecución de la función.
            Outputs:
                1 - "row" es una lista que contiene los elementos de la fila "j" que se tomó como parámetro.
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            row = aux[j]
        else:
            row = [i[j] for i in aux]
        return row

    def get_col(self, k):
        ''' Devuelve el contenido de la columna k (sus elementos) en forma de una lista. En el caso que by_row = True,
            esta función utiliza otro método ya creado, get_pos(j, k), ya que este devuelve el índice de un par de 
            coordenadas en la matriz, lo que nos es útil para agregar el elemento deseado a la lista column.
            Inputs:
                1 - "k" es un entero (int) >= 0 que indica la columna que se quiere mostrar al finalizar la ejecución.
            Outputs:
                1 - "column" es una lista que contiene los elementos de la columna "k" que se tomó como parámetro.
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            column = [i[k] for i in aux]
        else:
            column = aux[k]
        return column

    def get_elem(self, j, k):
        ''' Esta función, dada una coordena "j,k", busca el elemento de la matriz que se encuentra en tal coordenada.
            Como la matriz está almacenada en una lista de listas, se utiliza el método get_row(), definido anteriormente
            para así tomar la sublista de la fila "j", y luego se la indexa según "k" para obtener el elemento de la matriz.
            Inputs:
                1 - "j" es un entero (int) >= 0 que indica el número de la fila de la matriz.
                2 - "k" es un entero (int) >= 0 que indica el número de la columna de la matriz.
            Outputs:
                1 - "elem" es un entero (int) perteneciente a la matriz. Es el elemento que, dada las coordenadas
                    j,k como argumento, se pretendía buscar.
        '''
        aux = self.elems.copy()
        elem = self.get_row(j)[k]
        return elem
    
    def del_row(self, j):
        ''' Esta función elimina una fila de la matriz, para luego devolver un objeto de la misma matriz sin tal fila.
            Inputs:
                1 - "j" es un enterio (int) correspondiente a la fila que se busca eliminar de la matriz.
            Outputs:
                1 - Devuelve un nuevo objeto de la clase con la matriz modificada, ya que no contará con la fila "j" que
                se eliminó.
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            aux.pop(j)
        else:
            # [sublist.pop(j) for sublist in aux]
            for sublist in aux:
                sublist.pop(j)
        return self.__class__(aux, self.r-1, self.c, self.by_row)
    
    def del_col(self, k):
        ''' Esta función elimina una columna de la matriz, para luego devolver un objeto de la misma matriz sin tal columna.
            Inputs:
                1 - "k" es un entero (int) correspondiente a la columna que se busca eliminar de la matriz.
            Outputs:
                1 - Devuelve un nuevo objeto de la clase con la matriz modificada, ya que no contará con la columna "k" que
                se eliminó.
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            [sublist.pop(k) for sublist in aux]
        else:
            aux.pop(k)
        return self.__class__(aux, self.r, self.c-1, self.by_row)
    
    def swap_rows(self, j, k):
        ''' Esta función intercambia una fila "j" de la matriz por una fila "k". Luego devuelve un objeto de la misma
            matriz con las filas "j" y "k" intercambiadas.
            Inputs:
                1 - "j" es un entero (int) que indica el número de fila que se quiere intercambiar por la fila "k".
                2 - "k" es un entero (int) que indica el número de fila que se quiere intercambiar por la fila "j".
            Outputs:
                1 - Devuelve un nuevo objeto de la clase con la matriz modificada, al intercambiar la fila "j" con
                la fila "k".
        '''     
        aux = self.elems.copy()
        if self.by_row == True:
            aux[j], aux[k] = aux[k], aux[j]
        else:
            for sublist in aux:
                sublist[j], sublist[k] = sublist[k], sublist[j]
        return self.__class__(aux, self.r, self.c, self.by_row)
    
    def swap_cols(self, l, m):
        ''' Esta función intercambia una columna "l" de la matriz por una columna "m". Luego devuelve un objeto de la misma
            matriz con las columnas "l" y "m" intercambiadas.
            Inputs:
                1 - "l" es un entero (int) que indica el número de fila que se quiere intercambiar por la fila "m".
                2 - "m" es un entero (int) que indica el número de fila que se quiere intercambiar por la fila "l".
            Outputs:
                1 - Devuelve un nuevo objeto de la clase con la matriz modificada, al intercambiar la fila "l" con
                la fila "m".
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            for sublist in aux:
                sublist[l], sublist[m] = sublist[m], sublist[l]
        else:
            aux[l], aux[m] = aux[m], aux[l]
        return self.__class__(aux, self.r, self.c, self.by_row)

    def scale_row(self, j, x):
        ''' Esta función toma una fila "j" de la matriz y la multiplica por un escalar "x", devolviendo un objeto de la 
            misma clase con la matriz multiplicada, donde se alteró la fila al multiplicarla por el escalar.
            Inputs:
                1 - "j" es un entero (int) que indica el número de la fila que se busca multiplicar.
                2 - "x" es un escalar (puede ser de cualquier tipo) que multiplicará a la fila "j".
            Outputs:
                1 - La función devuelve un nuevo objeto de la clase con la fila "j" modificada, ya que esta se multiplicó
                por el escalar "x".
        '''
        aux = self.elems.copy()
        if not isinstance(x, (int, float, complex)): #Instancia de validación
            raise ValueError('El escalar debe ser un número.')
        if self.by_row == True:
            for i in range(self.c):
                aux[j][i] = (aux[j][i]) * x
        else:
            for i in range(len(aux)):
                aux[i][j] = (aux[i][j]) * x
        return self.__class__(aux, self.r, self.c, self.by_row)
    
    def scale_col(self, k, y):
        ''' Esta función toma una columna "k" de la matriz y la multiplica por un escalar "y", devolviendo un objeto de la 
            misma clase con la matriz multiplicada, donde se alteró la columna al multiplicarla por el escalar.
            Inputs:
                1 - "k" es un entero (int) que indica el número de la columna que se busca multiplicar.
                2 - "y" es un escalar (puede ser de cualquier tipo) que multiplicará a la columna "k".
            Outputs:
                1 - La función devuelve un nuevo objeto de la clase con la columna "k" modificada, ya que esta se multiplicó
                por el escalar "y".
        '''
        aux = self.elems.copy()
        if not isinstance(y, (int, float, complex)): #Instancia de validación
            raise ValueError('El escalar debe ser un número.')
        if self.by_row == True:
            for i in range(len(aux)):
                aux[i][k] = (aux[i][k]) * y
        else:
            for i in range(self.c):
                aux[k][i] = (aux[k][i]) * y
        return self.__class__(aux, self.r, self.c, self.by_row)

    def transpose(self):
        ''' Función que devuelve un objeto transpuesto, lo que significa que la matriz está
            traspuesta. Esta función cambia la matriz original, pero no altera ni la lista de
            elementos en la que se almacena la matriz, ni tampoco cambia el valor de verdad
            de by_row.
        '''
        aux = self.elems.copy()
        self.by_row = not self.by_row
        return self.__class__(aux, self.c, self.r, self.by_row)
    
    def flip_cols(self):
        ''' Funcion que devuelve una copia del objeto con sus columnas reflejadas de manera especular. Esto
            supone que la primera columna se intercambia con la última, la segunda con la penúltima y así hasta
            terminar. Esta función no toma argumentos.
            Outputs:
                1 - Devuelve una copia del elemento de la clase, con sus columnas reflejadas de manera especular.
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            for row in aux:
                for i in range(self.c//2):
                    row[i], row[-i-1] = row[-i-1], row[i]
        else:
            aux = aux[::-1]
            # for i in range(self.r//2):
            #     aux[i], aux[self.r-1-i] = aux[self.r-1-i], aux[i]
        return self.__class__(aux, self.r, self.c, self.by_row)
    
    def flip_rows(self):
        ''' Funcion que devuelve una copia del objeto con sus filas reflejadas de manera especular. Esto
            supone que la primera filas se intercambia con la última, la segunda con la penúltima y así hasta
            terminar. Esta función no toma argumentos.
            Outputs:
                1 - Devuelve una copia del elemento de la clase, con sus filas reflejadas de manera especular.
        '''
        aux = self.elems.copy()
        if self.by_row == True:
            aux = aux[::-1]
            # for i in range(self.r//2):
            #     aux[i], aux[self.r-1-i] = aux[self.r-1-i], aux[i]
        else:
            for row in aux:
                for i in range(self.c//2):
                    row[i], row[-i-1] = row[-i-1], row[i]
        return self.__class__(aux, self.r, self.c, self.by_row)

    def myprint(self):
        ''' Función que sirve para imprimir la matriz '''
        #Imprime la matriz para chequear los demás métodos construidos
        print('\n')
        if self.by_row == True:
            for i in range(0,self.r):
                print(self.get_row(i))
        else:
            for i in range(0, self.c):
                print(self.get_row(i))
        print('\n')
        return None

#________________________________________________________________
#Prueba de la clase y sus funciones
matriz = [[1, 2, 1], [3, 5, 4], [7, 4, 10]]
matriz1 = [[1, 2, 1], [3, 5, 4], [2, 4, 1], [10, 11, 0]]
matriz2 = [[1, 2, 5, 1], [3, 5, 4, 3], [7, 4, 10, 1]]

m = Myarray2(matriz, 3, 3, False)
print(m.elems)
# m.myprint()

a = Myarray2(matriz1, 4, 3, False)
print(a.elems)
# a.myprint()

b = Myarray2(matriz2, 3, 4, False)
print(b.elems)
# b.myprint()

# get_pos() 
# position = m.get_pos(1,2)
# print(f'La posicion del elemento en la lista es: {position}')

# get_coords()
# coords = m.get_coords(5)
# print(f'Las coordenadas del elemento en la matriz son: {coords}')

# switch()
# switched = m.switch().elems
# print(f'La lista de la matriz aplicada la función switch() es: {switched}')

# # get_row()
# row = m.get_row(2)
# print(f'Los elementos de la fila dada son: {row}')

# get_column()
# column = m.get_col(2)
# print(f'Los elementos de la columna dada son: {column}')

# get_elem()
# elem = m.get_elem(3, 1)
# print(f'El elemento es: {elem}')

# del_row()
# del_row = m.del_row(2).elems
# print(f'La nueva matriz es: {del_row}')

# del_col()
# del_col = m.del_col(1).elems
# print(f'La nueva matriz es: {del_col}')

# swap_rows()
# swapped_rows = m.swap_rows(0,2).elems
# print(f'La nueva matriz es: {swapped_rows}')

# swap_cols()
# swapped_cols = m.swap_cols(0,1).elems
# print(f'La nueva matriz es: {swapped_cols}')
    
# scale_row(). También modifica el objeto. Comentar entre ''' ''' para probar el resto de la clase.
# x = 2
# scaled_r = m.scale_row(1, x).elems
# print(f'La nueva matriz es: {scaled_r}')

# scale_col(). También modifica el objeto. Comentar entre ''' ''' para probar el resto de la clase.
# y = -0.5
# scaled_c = m.scale_col(1, y).elems
# print(f'La nueva matriz es: {scaled_c}')

# transpose()
# m.transpose()
# m.myprint()

#flip_cols(). También modifica el objeto. Comentar entre ''' ''' para probar el resto de la clase.
# flipped_c = m.flip_cols().elems
# print(f'La nueva matriz es: {flipped_c}')
# m.myprint()

#flip_rows(). También modifica el objeto. Comentar entre ''' ''' para probar el resto de la clase.
# flipped_r = m.flip_rows().elems
# print(f'La nueva matriz es: {flipped_r}')
# m.myprint()
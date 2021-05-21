''' Author: Didier Stevenson Calvache Grajales
     Date: May 2021
     <didiermaxilo3@gmail.com>

    /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/= Third Higher /=/=/=/=/=/=/=/=/=/==/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
    Dado un array de enteros, retornar el tercer entero más grande del mismo. Si el tercero más grande no existe,
    retornar el número mayor.

    Ejemplo 1:
    Input: nums = [3,2,1]
    Output: 1

    Ejemplo 2:
    Input: nums = [1,2]
    Output: 2
    Detalle: El tercero mas grande no existe, entonces el máximo (2) es devuelto.

    Ejemplo 3:
    Input: nums = [2,2,3,1]
    Output: 1
    Detalle: Notese que el tercero mas grande acá significa el tercero mas grande distinto. Ambos números 2 son
    considerados como el segundo más grande.

    Condiciones:
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
'''

def thirdHigher(array):
    array.sort()
    array = list(set(array))
    if(len(array) <3):
        return array[-1]
    return array[-3]

array1 = [1,2,3,4,5,6]
array2 = [3,2,1]
array3 = [1,2]
array4 = [2,2,3,1]

array1 = thirdHigher(array1)
array2 = thirdHigher(array2)
array3 = thirdHigher(array3)
array4 = thirdHigher(array4)

print(f"\t\t/=/=/= Highers of =/=/=/\nArray1: {array1}\nArray2: {array2}\nArray3: {array3}\nArray4: {array4}")



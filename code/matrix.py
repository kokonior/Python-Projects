#FIRMANSYAH HELMI KURNIAWAN
#TEKNIK MULTIMEDIA DAN JARINGAN
#ALGORITMA DAN PEMROGRAMAN
#2007421030

##31 Python Tutorial for Beginners | Working with Matrix in Python

from numpy import *

arr1 = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr2 = arr1.flatten()
arr3 = arr1.reshape(3,4)
arr4 = arr1.reshape(3,2,2)
print("mengubah bentuk menjadi rata\n", arr2, "\n")
print("mengubah bentuk 3 baris 4 kolom\n", arr3, "\n")
print("mengubah bentuk 3 bagian 2 baris 2 kolom\n", arr4, "\n")

matrix1 = matrix('1 2 3; 6 4 5; 1 6 7')
diagonal = diagonal(matrix1)
print("matrix normal\n", matrix1, "\n")
print("matrix diagonal\n", diagonal, "\n")
print("matrix minimal\n", matrix1.min(), "\n")
print("matrix maksimal\n", matrix1.max(), "\n")

matrix2 = matrix('1 2 3; 7 7 7; 1 6 7')
matrix_kali = matrix1 * matrix2
matrix_tambah = matrix1 + matrix2
print("matrix kali\n", matrix_kali, "\n")    
print("matrix tambah\n", matrix_tambah, "\n")    

# Function to take an input of string and new line character and return the (2nd) column and row of choice
# An example is given. Note the function only work if there is the same number of elements in each row

class Matrix:
    def __init__(self, matrix_string):
        newList = matrix_string.split('\n')
        self.rowList = []
        self.columnList = []      
        for row in range(len(newList)):
            self.rowList.append([int(number) for number in newList[row].split()])     
        for column in range(len(self.rowList[0])):
            testList =[]
            for row in range(len(self.rowList)):
                testList.append(self.rowList[row][column])
            self.columnList.append(testList)
            
    def row(self, index):
        return self.rowList[index-1]
    
    def column(self, index):
        return self.columnList[index-1]

#Example
matrix = Matrix("89 1903 3 4\n18 3 1 5\n9 4 800 5")

print(matrix.column(2)) 
print(matrix.row(2))

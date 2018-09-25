

# sheemo's evil question

def find_determinant( matrix ):
      # define matrix of array of n arrays containing n elements
      n = len(matrix)

      if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]4
      elif n == 1:
            return matrix[0]
      elif n == 0:
            return 'u suck find out what a matrix is.'
      else:
            total = 0
            count = 1
            for i in range(n):
                  mat = []
                  for x in range(1,n):
                        mat.append(matrix[x][0:i]+matrix[x][i+1:])
                  # obtained new matrix
                  
                  mat_value = matrix[0][i] * find_determinant( mat )
                  if count % 2 == 0:
                        total -= mat_value
                  else:
                        total += mat_value
                  count += 1
            return total

import numpy as np
np.set_printoptions(formatter={'float': lambda  x: "{0:0.2f}".format(x)})

# matrix = np.array([[1.0,3.0,2.0,-4.0,3.0],
#                    [-2.0,-1.0,2.0,6.0,4.0],
#                    [0.0,-1.0,3.0,-5.0,1.0],
#                    [3.0,-4.0,2.0,5.0,-7.0],
#                    [1.0,2.0,-8.0,6.0,1.0]])

# res = np.array([[-3.0,19.0,-2.0,-11.0,4.0]])
# res = np.transpose(res)
# mtrx = np.concatenate([matrix, res], axis=1)
# n = 5

matrix=np.array([[3.0,-2.0,0.0,0.0,0.0,0.0],
                 [-2.0,3.0,-2.0,0.0,0.0,0.0],
                 [0.0,-2.0,2/3,-2.0,0.0,0.0],
                 [0.0,0.0,0.0,-2.0,3.0,-2.0],
                 [0.0,0.0,-2.0,3.0,-2.0,0.0],
                 [0.0,0.0,0.0,0.0,-2.0,3.0]])
res = np.array([[-1.0,-1.0,-10/3,-1.0,-1.0,1.0]])
res = np.transpose(res)
mtrx = np.concatenate([matrix, res], axis=1)
n = 6

print(mtrx)
print()
# to place a pivot for first column
if mtrx[0][0] == 0:
    for i in range(1,n):
        if mtrx[i][0] != 0 :
            mtrx[[0 , i]] = mtrx[[i , 0]]
            break
    print(mtrx)
#row reduction 
for j in range(0 , n) : 
    for i in range(j+1,n):
        if mtrx[i][j] != 0 :
            for x in range(j, i) :
                if mtrx[x][j] != 0 :
                    coef= mtrx[i][j] / mtrx[x][j]
                    mtrx[i] -= coef * mtrx[x]
                    print()
                    print(mtrx)
                    break

#transform to diameter matrix
for j in range(n-1 , 0,-1) : #n-1 to 0 
    for i in range(0,j):
        if mtrx[i][j] != 0 :
            coef= mtrx[i][j] / mtrx[j][j]
            mtrx[i] -= coef * mtrx[j]

x=[n]            
for i in range(n) : 
   mtrx[i]= mtrx[i]/mtrx[i][i]
   
print(mtrx)

for i in range(n):
    x.append(mtrx[i][n])
result = np.array(x)

print("result matrix is : ",result )






                


def gauss(matrix,m,n):
    p=0
    for i in range(m):
        if all(matrix[i][j]==0 for j in range(n-1)) and matrix[i][n-1]!=0:
            print("vo nghiem")
            break
        if matrix[i][p]==0:
            check=0
            for j in range (i,m): #Kiem tra tung cot de swap neu can thiet
                if matrix[j][p]!=0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    check=1
                    break
            if check == 0: #neu cot bang vector 0 thi doi sang cot ke tiep
                p+=1
                if p>n-1:
                    p-=1
        if matrix[i][p]!=0:
            temp = matrix[i][p]+0.0
            for j in range (n):
                if matrix[i][j]!=0:
                    matrix[i][j]/=temp
            for k in range (i+1,m,1): #kiem dong` khac 0 tinh tu cot pivot
                if matrix[k][p]!=0:
                    multi= matrix[k][p]+0.0 # gia tri can` nhan^ len 
                    for j in range (p,n,1):
                        matrix[k][j]-=(multi*matrix[i][j])+0.0 #mat[i][j] la dong` cua? pivot
                        
            p+=1
    return matrix
def InfiniteSol(matrix,m,n):
    check = False
    dem =0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]!=0:
                dem+=1
                break
    if dem<len(matrix[1]):
        check=True
    return check
def InfiniteSolSubtitution(a,m,n):
    x=['none']*(n-1)
    for i in range(m-1,-1,-1):
        for j in range(n):
            if a[i][j]!=0:
                temp=a[i][n-1]
                for k in range (j+1,n-1):
                    temp = str(temp)
                    if x[k]=='none':
                        x[k]='a'+str(k)
                        temp=temp+'-'+str(a[i][k])+str(x[k])
                    else: temp=temp+'-'+str(a[i][k])+'x'+str(x[k])
                if isinstance(temp,str):
                    temp='('+temp+')'
                else: temp='('+temp+')'
                x[j]=temp
                x[j]=x[j].replace('--','+')
                break
    return x
def subtitution(a,m,n):
    x=[0]*(n-1)
    for i in range(m-1,-1,-1):
        for j in range(n):
            if a[i][j]!=0:
                temp=a[i][n-1]
                for k in range(j+1,n-1):
                    temp-=a[i][k]*x[k]
                temp/=a[i][j]
                x[i]=temp
                
                break
    return x
matrix=[[1,-2,3,-3],[2,2,0,0],[0,-3,4,1],[1,0,1,-1]]
matrix1=[[0,0,-2,0,7,12],[2,4,-10,6,12,28],[2,4,-5,6,-5,-1]]
matrix2=[[2,-4,6,8],[1,-1,1,-1],[1,-3,4,0]]
matrix3=[[4,-2,-4,2,1],[6,-3,0,-5,3],[8,-4,28,-44,11],[-8,4,-4,12,-5]]
matrix4=[[1,2,-2,3],[3,-1,1,1],[-1,5,-5,5]]
m =len(matrix4)
n=len(matrix4[1])
gauss(matrix4,m,n)
print(*matrix4,sep='\n')
if(InfiniteSol(matrix4,m,n)==True): x=InfiniteSolSubtitution(matrix4,m,n)
else: x=subtitution(matrix4,m,n)
print(x)
# x=subtitution(matrix,m,n)
# print(x)

# x=subtitution(matrix,m,n)
# print(*matrix,sep='\n')
# print(x)

    

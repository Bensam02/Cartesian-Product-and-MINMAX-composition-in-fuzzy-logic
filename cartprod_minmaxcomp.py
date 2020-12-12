def cartesian():    
    n = int(input("\nEnter number of elements in first set (A): "))
    A = []
    B = []
    print("Enter elements for A:") 
    for i in range(0, n): 
        ele = float(input()) 
        A.append(ele)
    m = int(input("\nEnter number of elements in second set (B): "))
    print("Enter elements for B:") 
    for i in range(0, m): 
        ele = float(input()) 
        B.append(ele)
    print("A = {"+str(A)[1:-1]+"}")
    print("B = {"+str(B)[1:-1]+"}")
    cart_prod = []
    cart_prod = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            cart_prod[i][j] = min(A[i],B[j])
    print("A x B = ")
    for i in range(n):
        for j in range(m):
            print(cart_prod[i][j],end="  ")
        print("\n")
    return


def minmax():
    r1 = int(input("Enter number of rows of first relation (R1): "))
    c1 = int(input("Enter number of columns of first relation (R1): "))
    rel1=[[0 for i in range(c1)]for j in range(r1)]
    print("Enter the elments for R:")
    for i in range(r1):
        for j in range(c1):
            rel1[i][j]=float(input())
    
    r2 = int(input("Enter number of rows of second relation (R2): "))
    c2 = int(input("Enter number of columns of second relation (R2): "))
    rel2=[[0 for i in range(c2)]for j in range(r2)]
    print("Enter the elments for R:")
    for i in range(r2):
        for j in range(c2):
            rel2[i][j]=float(input())
    
    print("\nR1 = ")
    for i in range(r1):
        for j in range(c1):
            print(rel1[i][j],end=" ")
        print("\n")
    print("\nR2 = ")
    for i in range(r2):
        for j in range(c2):
            print(rel2[i][j],end=" ")
        print("\n")
    
    
    col=0
    comp=[]
    for i in range(r1):
        comp.append([])
        for j in range(c2):
            l=[]
            for k in range(r2):
                l.append(min(rel1[i][k],rel2[k][j]))
            comp[i].append(max(l))  
    
    print("\nR1 composition R2 =")
    for i in range(r1):
        for j in range(c2):
            print(comp[i][j],end=" ")
        print("\n")
    return

ch=1
while ch==1:
    print("MENU:\n----\n1->Cartesian Product\n2->Minmax Composition\n3->Exit")
    op=int(input("Enter Your Choice: "))
    if op==1:
        cartesian()
    elif op==2:
        minmax()
    elif op==3:
        break
    else:
        print("Wrong Choice!")
    ch=int(input("Do you wish to continue (1-Yes | 0-No): "))
    print("\n")


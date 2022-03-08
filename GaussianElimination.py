"""
By Aaron D'Cunha
Code gives each steps to solve 3 systems using Gaussian Elimination
"""


def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm


def add(row1,row2):
    
    r1 = row1.copy()
    r2 = row2.copy()
    
    for i in range(len(r1)):
        r2[i] += r1[i]
    
    return r2

def multiplyrow(row,val):
    
    r = row.copy()
    for  i in range(len(r)):
        r[i] *= val
        
    return r

def printMatrix(r1,r2,r3):
    print(r1)
    print(r2)
    print(r3)

def solveMatrix(row1,row2,row3):
    
    try:
    
        r1 = row1.copy()
        r2 = row2.copy()
        r3 = row3.copy()
        
        print("Given Matrix")
        printMatrix(r1,r2,r3)
        print("")
        
        #STEP 1
        if(r3[0] != 0):
        
            
            if(compute_lcm(r1[0],r3[0]) < compute_lcm(r2[0],r3[0])):
                
                lcm = compute_lcm(r1[0],r3[0])
                r3mul =  lcm/r3[0] 
                r1mul =  lcm/r1[0] 
                
                if( (r1[0] * r1mul ) / (r3[0] * r3mul) == 1 ):
                    r3mul *= -1
                    
                tempR1=multiplyrow(r1, r1mul)
                tempR3=multiplyrow(r3,r3mul)
                r3 = add(tempR1,tempR3)
                
                print("{0} R1 + {1} R3 => R3".format(r1mul,r3mul))
                
            else:
                
                lcm = compute_lcm(r2[0],r3[0])
                r3mul =  lcm / r3[0]
                r2mul =  lcm /r2[0] 
                
                if( (r2[0] * r2mul ) / (r3[0] * r3mul) == 1 ):
                    r3mul *= -1
                    
                tempR2=multiplyrow(r2, r2mul)
                tempR3=multiplyrow(r3,r3mul)
                r3 = add(tempR2,tempR3)
                
                print("{0} R2 + {1} R3 => R3".format(r2mul,r3mul))
                
            printMatrix(r1,r2,r3)
        
        print("")
        
        #STEP 2
        if(r2[0] != 0):
          
            lcm = compute_lcm(r1[0],r2[0])
            r2mul =  lcm/r2[0] 
            r1mul =  lcm/r1[0] 
            
            if( (r1[0] * r1mul ) / (r2[0] * r2mul) == 1 ):
                r2mul *= -1
                
            tempR1=multiplyrow(r1, r1mul)
            tempR2=multiplyrow(r2,r2mul)
            r2 = add(tempR1,tempR2)
            
            print("{0} R1 + {1} R2 => R2".format(r1mul,r2mul))
                
            
                
            printMatrix(r1,r2,r3)
            
        print("")
        
        #STEP 2.5
        if(r2[1]==0):
            r3copy = r3.copy()
            r2copy = r2.copy()
            r2 = r3copy;
            r3 = r2copy;
            
            print("INVERT R2 and R3")
            
            printMatrix(r1,r2,r3)
            
       
		 
        
        #STEP 3
        if(r3[1] != 0):
          
            lcm = compute_lcm(r2[1],r3[1])
            r2mul =  lcm/r2[1] 
            r3mul =  lcm/r3[1] 
            
            if( (r3[1] * r3mul ) / (r2[1] * r2mul) == 1 ):
                r2mul *= -1
                
            tempR3=multiplyrow(r3, r3mul)
            tempR2=multiplyrow(r2,r2mul)
            r3 = add(tempR3,tempR2)
            
            print("{0} R2 + {1} R3 => R3".format(r2mul,r3mul))
                
            
                
            printMatrix(r1,r2,r3)
            
        print("")
        
        #STEP 4
        if(r3[2] != 1):
            print("1/{0} R3 => R3".format(r3[2]))
            r3 = multiplyrow(r3,1/r3[2])
            printMatrix(r1,r2,r3)
        
        print("")    
        
        #STEP 5
        if(r2[2] != 0):
            tempr3 = multiplyrow(r3,-r2[2])
            print("{0} R3 + {1} R2 => R2".format(-r2[2],1))
            r2 = add(r2,tempr3)
            printMatrix(r1,r2,r3)
            
        print("")
        
        #STEP 6
        if(r2[1] != 1):
            print("1/{0} R2 => R2".format(r2[1]))
            r2 = multiplyrow(r2,1/r2[1])
            printMatrix(r1,r2,r3)
            
        print("")
        
        #STEP 7
        if(r1[1] != 0):
            tempr2 = multiplyrow(r2,-r1[1])
            print("{0} R2 + {1} R1 => R1".format(-r1[1],1))
            r1 = add(r1,tempr2)
            printMatrix(r1,r2,r3)
        
        print("")
        
        #STEP 8
        if(r1[2] != 0):
            tempr3 = multiplyrow(r3,-r1[2])
            print("{0} R3 + {1} R1 => R1".format(-r1[2],1))
            r1 = add(r1,tempr3)
            printMatrix(r1,r2,r3)
            
        print("")
        
        #STEP 9
        if(r1[0] != 1):
            print("1/{0} R1 => R1".format(r1[0]))
            r1 = multiplyrow(r1,1/r1[0])
            printMatrix(r1,r2,r3)
        
        print("Solution : ({0},{1},{2})".format(r1[3],r2[3],r3[3]))
    
    except:
        print("No solution possible from given matrix")
    

        
print("Insert each row in the form [a, b, c, d]") 
rowone = eval(input("Insert row1: "))
rowtwo = eval(input("Insert row2: "))
rowthree = eval(input("Insert row3: "))

solveMatrix(rowone,rowtwo,rowthree)
    
    
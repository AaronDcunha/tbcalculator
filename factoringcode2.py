"""
Factoring code mdae by Aaron
This is V2. In this version I would just use the quadratic formula and from there reshape it to get the factors
"""

import cmath

def getSign(cmplx):
    if(cmplx.real / abs(cmplx.real) == -1):
        return "-"
    else:
        return "+"
    
def hcf(_1,_2):
    prevNum = 1
    if _1<=_2:
        for i in range(1,int(_1+1)):
            if( _1 % i == 0 and _2 % i == 0 ) :
                prevNum = i
    else:
        for i in range(1,int(_2+1)):
            if( _1 % i == 0 and _2 % i == 0 ) :
                prevNum = i
                
    return prevNum

def factorise(a,b,c):
    if(a == 0):
        
        print("Coefficient 'a' cannot be 0 (Invalid Input)")
        return 
    
    elif(a !=0 and b!=0 and c!=0):
        
        _sum = b
        _product = a*c
        
        factor1 = ( _sum + cmath.sqrt(_sum**2 - ( 4 * _product ) ) ) / 2
        factor2 = _sum - factor1
        
        print("")
        print("Factors : {0} and {1}".format(factor1,factor2))
        
        if(a == 1) :
        
            print("")
            print("Can be written as: (x {0} {1}) (x {2} {3})".format(getSign(factor1),abs(factor1),getSign(factor2),abs(factor2)))
            return
        
        common1 = hcf(abs(a),abs(factor1))
        common2 = hcf(abs(c),abs(factor2))
        
        cofA = a/common1
        cofB = factor1/common1
        cofC = factor2/common2
        cofD = c/common2
        
        if( (cofA + cofB) / (cofC+cofD) == -1):
            common2 *= -1
        
        print("")
        print("Can be written as: ({0}x {1} {2}) ({3}x {4} {5})".format(cofA,getSign(cofB),abs(cofB),common1,getSign(common2),abs(common2)))
        
    elif(a!=0 and b!=0 and c==0):
        
        common = hcf(abs(a),abs(b))
        
        print("")
        print("Factors : {0}".format(common))
        print("")
        
        if(common == 1):     
            print("Can be written as: x({0}x {1} {2})".format(a,getSign(b),b))
        else:
            print("Can be written as: {0}x({1}x {2} {3})".format(common,a/common,getSign(b),b/common))
            
    elif(a!=0 and b==0 and c!=0):
        
        print("")
        
        if(getSign(a) == "+" and getSign(c) =="-"):           
            print("Can be written as: ({0}x + {1}) ({0}x - {1})".format(cmath.sqrt(a).real,cmath.sqrt(abs(c)).real))
        elif(getSign(a) == "-" and getSign(c) =="+"):
            print("Can be written as: ({0}x + {1}) ({0}x - {1})".format(cmath.sqrt(abs(a)).real,cmath.sqrt(c).real))
        else:
            common = hcf(abs(a),abs(c))
            print("Can be written as: {0}({1}x {2} {3})".format(common,a/common,getSign(c),abs(c/common)))
           
    else:
        print("")
        print("Unable to compute, possible problems => Invalid Input (or) Cannot be factored ")
 

print("Insert coefficients ax^2 +bx +c = 0")
print("Note there are some drawbacks using this calculator and would likely be fixed soon. Use this only to double check your answer")
_a = int(input("Coefficient a: "))
_b = int(input("Coefficient b: "))
_c = int(input("Coefficient c: "))


factorise(_a,_b,_c)

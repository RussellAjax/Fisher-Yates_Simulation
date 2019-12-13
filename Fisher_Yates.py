import random
import sys

sys.setrecursionlimit(10000)

#variable declaration
#for this function, a = 1, b = 2, c = 3, d = 4
abcd = 0 #the permutation of abcd will be [1,2,3,4] when comparing the conditionals
abdc = 0
acbd = 0
acdb = 0
adbc = 0
adcb = 0
bacd = 0
badc = 0
bcad = 0
bcda = 0
bdac = 0
bdca = 0
cabd = 0
cadb = 0
cbad = 0
cbda = 0
cdab = 0
cdba = 0
dabc = 0
dacb = 0
dbac = 0
dbca = 0
dcab = 0
dcba = 0

def randomize(arr_Parameter, n_Parameter, recursiveCount_Parameter):
    #assigning global variables to the function
    global abcd
    global abdc
    global acbd
    global acdb
    global adbc
    global adcb
    global bacd
    global badc
    global bcad
    global bcda
    global bdac
    global bdca
    global cabd
    global cadb
    global cbad
    global cbda
    global cdab
    global cdba
    global dabc
    global dacb
    global dbac
    global dbca
    global dcab 
    global dcba

    if recursiveCount_Parameter == 5000:
       return """ABCD: {0}
        ABDC: {1}
        ACBD: {2}
        ACDB: {3}
        ADBC: {4}
        ADCB: {5}
        BACD: {6}
        BADC: {7}
        BCAD: {8}
        BCDA: {9}
        BDAC: {10}
        BDCA: {11}
        CABD: {12}
        CADB: {13}
        CBAD: {14}
        CBDA: {15}
        CDAB: {16}
        CDBA: {17}
        DABC: {18}
        DACB: {19}
        DBAC: {20}
        DBCA: {21}
        DCAB: {22}
        DCBA: {23}
        """.format(str(abcd), str(abdc), str(acbd) ,str(acdb), str(adbc), str(adcb), str(bacd), str(badc), str(bcad), str(bcda), str(bdac), str(bdca), str(cabd), str(cadb), str(cbad), str(cbda), str(cdab), str(cdba), str(dabc), str(dacb), str(dbac), str(dbca), str(dcab), str(dcba))
    else:
        for i in range(n_Parameter-1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
    
        result = arr

        if result == [1, 2, 3,4]:
            abcd += 1
        elif result == [1, 2, 4, 3]:
            abdc += 1
        elif result == [1,3, 2, 4]:
            acbd += 1
        elif result == [1, 3, 4, 2]:
            acdb += 1
        elif result == [1, 4, 2, 3]:
            adbc += 1
        elif result == [1, 4, 3, 2]:
            adcb += 1
        elif result == [2, 1, 3, 4]:
            bacd += 1
        elif result == [2, 1, 4, 3]:
            badc += 1
        elif result == [2, 3, 1, 4]:
            bcad += 1
        elif result == [2, 3, 4, 1]:
            bcda += 1
        elif result == [2, 4, 1, 3]:
            bdac += 1
        elif result == [2, 4, 3, 1]:
            bdca += 1
        elif result == [3, 1, 2, 4]:
            cabd += 1
        elif result == [3, 1, 4, 2]:
            cadb += 1
        elif result == [3, 2, 1, 4]:
            cbad += 1
        elif result == [3, 2, 4, 1]:
            cbda += 1
        elif result == [3, 4, 1, 2]:
            cdab += 1
        elif result == [3, 4, 2, 1]:
            cdba += 1
        elif result == [4, 1, 2, 3]:
            dabc += 1
        elif result == [4, 1, 3, 2]:
            dacb += 1
        elif result == [4, 2, 1, 3]:
            dbac += 1
        elif result == [4, 2, 3, 1]:
            dbca += 1
        elif result == [4, 3, 2, 1]:
            dcba += 1
        elif result == [4, 3, 1, 2]:
            dcab += 1

        recursiveCount_Parameter = recursiveCount_Parameter + 1
        return randomize(arr_Parameter, n_Parameter, recursiveCount_Parameter)
#END OF FUNCTION

arr = [1,2,3,4]
n = len(arr)
recursiveGlobalCount = 1

print(randomize(arr, n, recursiveGlobalCount))
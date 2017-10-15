Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def isPrimerNumber(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        isPrimeNum = True;
        for i in range(2, num):
            if num % i == 0:
                isPrimeNum = False;
                break
        
        if isPrimeNum == True:
            return True
        else:
            return  False

        
>>> x = 1
>>> count = 0
>>> List = []
>>> while count <= 1000:
	    x+=1 
	    if (isPrimerNumber(x) == True):
		List.append(x) 
		count+=1

print(List)

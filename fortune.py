def fortune(a,b,c,d,e,f):
    result  = set([a,b,c,d,e,f])
    A = list(result) 
    sum = int(A[0])+int(A[1])+int(A[2])+int(A[3])+int(A[4])+int(A[5])
    if sum >= 12:
        return "0"
    else:
        return "1"

B = input("주민번호를 입력하세요:")
C = [int(digit)for digit in B]
if len(B)==6:
    result = fortune(*C)
    print (result)
else:    
    print(" 6자리로 입력해주세요 ")

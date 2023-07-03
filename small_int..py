
def getSmallInt(A):
    A.sort()
    n = len(A)-1
    if A[0]<=0 or A[n]<=0:
        return 1
    if A[0]<=0 and A[n]<=0:
        return 1

    i=0
    while i <n:
        j = A[i]
        next = A[i+1]
        first_step = next- j
        if first_step==1:
            i+=1
        elif first_step==0:
            i+=2
        if first_step >1:
            print(j+1)
            return j+1
    print(A[n]+1)
    return A[n]+1

if __name__ == "__main__":
    A = []
    num_times = int(input('How many times: '))
    i = 0
    while i<num_times:
        num = int(input(str(i) + ' Enter number : '))
        A.append(num)
        i+=1
    getSmallInt(A)
def get_fibo(n:int):
    if n <= 0:
        return {"error" : "n must be a positive Number"}
    sequence = []
    n1 = 0
    n2 = 1
    sequence.append(n1)
    sequence.append(n2)
    n = int(input("enter the  number :"))
    for i in range(n-2):
        n3 = n1+n2
        sequence.append(n3)
        n1=n2
        n2=n3

    return sequence

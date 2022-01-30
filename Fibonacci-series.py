def fibo_seriesfibo_to_n(n):
    fibo=[1,1]
    while fibo[-1] < (n):
        k=fibo[-1]+fibo[-2]
        fibo.append(k)
    print(fibo)
fibo_seriesfibo_to_n(50)
#Code by Samson c. Mathews

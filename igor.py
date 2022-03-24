import random
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
start = 1   # inclusive
end = 61    # exclusive
n = 6      # size
i=0
j=0
k=0 # numero de acertos
count = 1
a = []
count2=0
while k<=6:
    count = count + 1 
    x = random.sample(range(start, end), n)
    igr = random.sample(range(start, end), n)
    x.sort();
    igr.sort();
    i=0
    while i<=5:
        aux = x[i]
        j=0
        while j<=5:
            if aux==igr[j]:
                k=k+1
                a.append(aux)
            j=j+1
        i=i+1
    t = (1/count)*100    
    t = truncate(t,8)
    #k>=5 = vai printar todos os sorteios que acertar 5 ou + 
    if k>=5:    
        print("\n-----------------------------------------")
        print("iteração     :",count)
        print("sorteio      :",x)
        print("igor         :",igr)
        print("acertos      :",k)
        print("numeros      :",a)
        print("probabilidade:",t,"%\n")
        count=0
        if k==6:
            print("ALERTA DE NÚMERO IGOR\n ALERTA DE NÚMERO IGOR\n ALERTA DE NÚMERO IGOR\n ALERTA DE NÚMERO IGOR\n")
    a = []
    k = 0
    i = 0


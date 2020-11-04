#lab 3

alfa = float(input())
beta = ( alfa - int(alfa/30)*30)*(360/30)
if '.0' in str(beta) and not('.00' in str(beta)):
    print(str(int(beta)))
else:
    print(beta)

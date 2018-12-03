#!/usr/bin/python

ile = input()
dodatnie = []
ujemne = []
wynik = []
    
for i in xrange(ile):
    wartosci = [int(x) for x in raw_input().split()]
    
    for j in range(1,len(wartosci)):
        if j%2==0:
            dodatnie.append(wartosci[j])
    
    for k in range(1,len(wartosci)):
        if k%2!=0:
            ujemne.append(wartosci[k])

    wynik.extend(dodatnie)
    wynik.extend(ujemne)

    for l in xrange(len(wynik)):
        print wynik[l],

    dodatnie = []
    ujemne = []
    wynik = []
    
    print '\n'

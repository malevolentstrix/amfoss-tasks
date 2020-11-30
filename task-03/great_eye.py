n=int(input())
dct={}
for i in range(0,n):
    k=int(input())
    tst=input()
    values=tst.split(' ')
    dct[k]=values
prm=list(dct.keys())
for j in prm:
    count=0
    if j<=len(dct[j])-1:
        word=dct[j][j]
        for k in word:
            count+=ord(k)
        print(count)
    else:
        count=-1
        print(count)

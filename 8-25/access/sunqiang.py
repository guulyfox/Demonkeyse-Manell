before=0
f2=open('tmp.txt','a+')
with open('access_log') as f1:
    while 1:
        f=f1.readline()
        if f == '':
            exit(0)

        k=f.split()[3][1:15].replace('/','')
        if before == k:
            f2.write(f)

        else:
            f2.close()
            f2=open('access.log-{}'.format(k),'a+')
            f2.write(f)

        before=f.split()[3][1:15].replace('/','')

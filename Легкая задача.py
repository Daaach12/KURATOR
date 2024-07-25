# №1
f=open('24_7094.txt').readline().strip()
cnt=0
alf = sorted(set(f))
for i in alf:
    s=f
    for j in alf:
        if j!=i:
            s=s.replace(j,"*")
    cnt+=s.count(f'*{i*5}*')
print(cnt)
# №3
f=open('24_7094.txt').readline().strip()
cnt=0
alf = sorted(set(f))
symbols={i:0 for i in alf}

for i in range (len(f)-6):
    if f[i]!=f[i+1] \
            and f[i+1]==f[i+2]==f[i+3]==f[i+4]==f[i+5] \
            and f[i]==f[i+6]:
        symbols[f[i]]+=1
print(f'{max(symbols)}{symbols[max(symbols)]}')
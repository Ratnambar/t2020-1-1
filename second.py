a = int(input())
res = []
count = 0

i=0
while(count<a):
    if i%2!=0:
        res.append(i)
        count+=1
    i+=1
print(res)
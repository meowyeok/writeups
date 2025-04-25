# pico : Bbbbloat

```cpp
input="A:4@r%uL4Ff0f9b03=_cf0cc7fc2e_N"
res=[]

for i in input:
  if ( (ord(i)>32) and (i != 127)):
    x = ord(i)+47

    if(x<=126):
      res.append(x)
    else:
      res.append(ord(i)-47)
      
for i in res:
  print(chr(i),end="")
```
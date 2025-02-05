encode=input()
decode=''
i=0
while i<len(encode):
    if encode[i].isdigit():
        decode+=encode[i+1]*int(encode[i])
        i=i+2
print(decode)

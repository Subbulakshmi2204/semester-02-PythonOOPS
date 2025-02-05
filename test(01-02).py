try:
    st=input("Enter an string:")
    a=len(st)
    if st[0]==st[a-1]:
        print(st[0])
        b=st[0]
        print(ord(b))
    else:
        raise ValueError ("No alphabet found..")
except ValueError as e:
    print(e)

    

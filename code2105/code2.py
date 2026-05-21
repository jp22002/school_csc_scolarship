def run_length_encode(data):
    dicti = {}
    for i in data:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    final = ()
    for i in dicti:
        final += ((i, dicti[i]),)
    return(final)

data = [10,20,30,30,30,20]
print(run_length_encode(data))
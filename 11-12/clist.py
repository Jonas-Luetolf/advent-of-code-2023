def cindex(arr,c):
    return arr[int(c.imag)][int(c.real)]

def crange(c0,c1,):
    for a in range(int(c0.imag),int(c1.imag)):
        for b in range(int(c0.real),int(c1.real)):
            yield complex(a,b)

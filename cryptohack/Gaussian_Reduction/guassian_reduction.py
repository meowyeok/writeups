v = (846835985, 9834798552); u = (87502093, 123094980)
v, u = map(ZZ^2, [v, u])

def gaussian_reduction(v1, v2):
    while 1:
        if v2*v2 < v1*v1: # ∥v2∥ < ∥v1∥ <=> ∥v2∥² < ∥v1∥²
            v1, v2 = v2, v1
    
        m = floor((v1*v2) / (v1*v1))
        if m == 0:
            return v1, v2
    
        v2 -= m*v1

a, b = gaussian_reduction(v, u)
print(a*b)
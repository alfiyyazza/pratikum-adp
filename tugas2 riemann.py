n = int(input("masukkan sebuah nilai n : "))
batas_bawah = 1 
batas_atas = 3 
delta_x = (batas_atas-batas_bawah)/n
luas =  0
for i in range(1, n+1) :
    xi = batas_bawah + i*delta_x 
    f_xi = xi**2 + 2*xi #f(x)=x**2 + 2*x
    luas += f_xi * delta_x
    
print(f"Luas daerah dari fungsi x**2 + 2*x dengan batas daerah {batas_bawah} dan {batas_atas} dan jumlah partisi n = {n} adalah {luas}")

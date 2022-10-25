from xdrlib import ConversionError

 
a11 = input ('Vnesi broj na pozicija a11: ')
a12 = input ('Vnesi broj na pozicija a12: ')
a13 = input ('Vnesi broj na pozicija a13: ')
a21 = input ('Vnesi broj na pozicija a21: ')
a22 = input ('Vnesi broj na pozicija a22: ')
a23 = input ('Vnesi broj na pozicija a23: ')
a31 = input ('Vnesi broj na pozicija a31: ')
a32 = input ('Vnesi broj na pozicija a32: ')
a33 = input ('Vnesi broj na pozicija a33: ')

Determinant = int(a11)*int(a22)*int(a33) + int(a12)* int(a23)*int(a31) + int(a13) *int(a21)*int(a32) - int(a12)*int(a21)*int(a33) - int(a11)*int(a23)*int(a32) - int(a13)*int(a22)*int(a31)


kraj = input(f'Determinantata e {Determinant}. Pritisnete enter za da zavrsite')
    

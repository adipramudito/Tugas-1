#Menghitung luas lingkaran
phi=22/7
r=input("Jari-jari lingkaran: ")
jari=float(r)
luas1=phi*jari**2
luas2="{:.2f}".format(luas1)
txt="Luas lingkaran dengan jari-jari "+str(r)+" cm adalah "+str(luas2)+" cm"+"\u00b2"
print(txt)
import passlib.hash as pl

ll = pl.md5_crypt.encrypt('12344321')
print(ll)

if pl.md5_crypt.verify('12344321','$1$dWje1fjH$009oUGCdC.lLaMGP7IVTe1'):
 print('Ok!')

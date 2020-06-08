import os
os.system('clear')
print ('\t<<<<< Matematika >>>>>')
print ('\tDont Rename Ny Script!')
print ('\tScript By ZkickYT')
print ('\tRename Die?')
print ('\tBreak Rules? Dye')
print
print '1.Penjumlahan'
print '2.Perkurangan'
print '3.Perkalian'
print '4.Pembagian'
print '5.Sisa Bagi'
print '6.Pemangkatan'
print
pilih = input('Silahkan Pilih Angka : ')

if pilih == 1:
	print
	angka_1 = input ('Angka Pertama : ')
	angka_2 = input ('Angka Kedua : ')
	total = angka_1 + angka_2
	print
	print'Totalnya : ', (total)
	
if pilih == 2:
	print
	angka_1 = input ('Angka Pertama : ')
	angka_2 = input ('Angka Kedua : ')
	total = angka_1 - angka_2
	print
	print'Totalnya : ', (total)
	
if pilih == 3:
	print
	angka_1 = input ('Angka Pertama : ')
	angka_2 = input ('Angka Kedua : ')
	total = angka_1 * angka_2
	print
	print'Totalnya : ', (total)
	
if pilih == 4:
	print
	angka_1 = input ('Angka Pertama : ')
	angka_2 = input ('Angka Kedua : ')
	total = angka_1 / angka_2
	print
	print'Totalnya : ', (total)
	
if pilih == 5:
	print
	angka_1 = input ('Angka Pertama : ')
	angka_2 = input ('Angka Kedua : ')
	total = angka_1 % angka_2
	print
	print'Totalnya : ', (total)

if pilih == 6:
	print
	angka_1 = input ('Angka Pertama : ')
	angka_2 = input ('Angka Kedua : ')
	total = angka_1 ** angka_2
	print
	print'Totalnya : ', (total)
	
else:
	print
	print 'Menu Tidak Ada!'
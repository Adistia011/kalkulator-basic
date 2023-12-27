def tambah(a, b):
  return a + b

def kurang(a, b):
  return a - b

def kali(a, b):
  return a * b

def bagi(a, b):
  if b != 0:
      return a / b
  else:
      return "Error: Pembagian pake angka nol gak bisa."

angka1 = float(input("Masukin angka: "))
operasi = input("Masukin input nya (+, -, *, /): ")
angka2 = float(input("Masukin angka: "))

if operasi == '+':
  hasil = tambah(angka1, angka2)
  print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operasi == '-':
  hasil = kurang(angka1, angka2)
  print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operasi == '*':
  hasil = kali(angka1, angka2)
  print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operasi == '/':
  hasil = bagi(angka1, angka2)
  print(f"Hasil: {angka1} / {angka2} = {hasil}")
else:
  print("Error: Penghitungan gak bisa. Coba Pakai +, -, *, atau /.")
ilksayi=input("ilk sayi girin:")
ikincisayi=input("ikinci sayi girin:")
secim=input("+,-,,/ :")

if secim =='+':
 print(float(ilksayi)+float(ikincisayi))
 
if secim =='-':
  print(float(ilksayi)-float(ikincisayi))

if secim =='/':
  print(float(ilksayi)/float(ikincisayi))

if secim =='':
  print(float(ilksayi)*float(ikincisayi)) 

print("iyi bok yedin")
'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if(n==0 or n==1):
    return False
  for d in range(2, n//2):
    if(n%d==0):
      return False
    return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  p=1
  for el in lst:
    p=p*el
  return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  z=0
  while y!=0:
    z=x%y
    x=y
    y=z
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  z=y
  if x<y:
    z=x
  if z==0:
    if x>y:
      return x
    return y
  for i in range(z,1,-1):
    if x%i==0 and y%i==0:
      return i
  
def main():
  # interfata de tip consola aici
  n=int(input("n="))
  if is_prime(n):
    print("nr prim")
  else:
      print("nr neprim")

  a=[]
  n=int(input("n="))
  for i in range(0,n):
    a.append(int(input()))
  print(get_product(a))

  x=int(input("x="))
  y=y=int(input("y="))
  print(get_cmmdc_v1(x,y))
  print(get_cmmdc_v2(x,y))

if __name__ == '__main__':
  main()

N=int(input("Enter the N values Numbers:"))
sum=0
for i in range(N):
  x=float(input("Enter number:"))
  sum+=x
  Avg=sum/N
  print("Print the avg number=%0.2f"%Avg)

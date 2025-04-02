import time
print("welcome to ATM")
print("="*30)
print("pls insert ATM card")
time.sleep(2)
print("pls wait for 3 sec")
time.sleep(3)
print("="*30)
print("1.Deposit \n2.Withdraw \n3.exit")
try:
   inp=int(input("pls enter your option="))
except ValueError:
   print("input must be 1 or 2 or 3 try again")
   time.sleep(3)
   exit()
try:
   oldbal=int(input("pls enter your old balance="))
   amount=int(input("pls enter the (W/D) amount="))
except ValueError:
   print(" amount should be in in numbers only")
match inp:
   case 1:
      if amount>=50000:
         panin=input("for depo above 50000 you need pan\ndo you have pan (y/n)=")
         if panin in "Yy":
            print("garte!.........")
            print("current balence=",oldbal+amount)
         else:
            print("sorry with out pan we cant prossed!........")
   case 2:
      if oldbal<amount:
         print("insuffecient funds!")
      elif oldbal==amount:
         print("sorry min bal should be maintained")
      else:
         currentbal=oldbal-amount
         print("current bal=",currentbal)
   case 3:
      exit()

   

            

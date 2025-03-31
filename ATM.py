oBal=int(input("Enter old Bal Amount:"))
ttype = int("Enter w for withdraw and d for deposit")
tamnt= int(input("Enter transaction amount:")
           if ttype=="w" or ttype=="W":
             if tamnt>old:
                 print("insufficient funds")
           elif tamnt==obal:
                 print("Pls maintain Min bal")
         else:
             cbal=obal-tamnt
             print("your current bal=",cbal)
elif ttype=="d" or ttype=="d":
      if tamnt>=50000:
         print("required pan")
      pan=input("do you have pan type y for yes=")
      if pan=="y" or pan=="y":
         cbal=obal+tamnt
      print("current bal=",cbal)
     else:
      print("invalid input")
     else:
        cbal=obal+tant
      print("current balance=",cbal)
      
  

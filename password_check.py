password=input("Enter password\n")
#password should have a lowercase, upper case and digit
lower=0
extra=0
upper=0
digit=0
for i in range(len(password)):
      if password[i].islower():
          lower=lower+1
      elif password[i].isupper():
          upper+=1
      elif password[i].isdigit():
          digit+=1
      else:
          extra+=1

if lower>=1 and upper>=1 and digit>=1 and extra>=1 and len(password)>=8:
     print("Password requirement matched")
else:
     print("Password condition is not matched")






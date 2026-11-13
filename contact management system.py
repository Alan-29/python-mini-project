contacts={}
while True:
  print("1.add contacts")
  print("2.search contacts")
  print("3.update contacts")
  print("4.delete contacts")
  print("5.display contacts")
  print("6.exit")
  choice=int(input("Enter the choice"))
  if choice==1:
      name=input("enter the name:")
      phone=int(input("Enter phone number:"))
      email=input("Enter the email:")
      contacts[name]=[phone,email]
      print("contact added")
  elif choice==2:
      name=input("Enter the name:")
      if name in contacts:
          print(contacts[name])
      else:
          print("contact not found")
  elif choice==3:
      name=input("Enter the name:")
      if name in contacts:
          phone=int(input("Enter the newphonenumber:"))
          email=input("Enter the newemail:")
          contacts[name]=[phone ,email]
          print("contact updated")
      else:
          print("contact not found")
  elif choice==4:
      name=input("Enter the name:")
      if name in contacts:
          del contacts[name]
          print("contacts deleted")
      else:
          print("contact not found")
  elif choice==5:
      for name in sorted(contacts):
          print(name,contacts[name])
  elif choice==6:
      break
  else:
      print("invalid choice")
                

      
    

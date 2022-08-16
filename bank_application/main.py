from customer import Customer
while True:
  print("""
  1.Create User.
  2.Deposite.
  3.Withdraw.
  4.Transfer.
  5.Transfer History Details.
  6.Exit.
  """)
  number=int(input("Enter the above detail-> "))
  match number:
    case 1:
      Customer.getInputFromUser()
    case 2:
      Customer.deposite()
    case 3:
      Customer.withdrawl()
    case 4:
      Customer.transfer()
    case 5:
      Customer.getTransactionalHistory()
    case 6:
      break


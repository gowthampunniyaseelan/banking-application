filename="bank_application/bank_db.txt"
class Customer:
  """
  This function is used to write the new user in the file
  """
  def __init__(self,customerId,name,balance,password,accountId):
    self.customerId = customerId
    self.name = name
    self.balance = balance
    self.password = password
    self.accountId = accountId

    """
    This is to write new user in the file
    """
    with open(filename,"r+") as f:
      data = self.customerId +" "+ self.accountId + " " + self.name + " " + self.balance + " " + self.password+"\n"
      f.seek(0,2)
      f.write(data)
    """
    Create new file for every user to track their bank transaction and their history of details about bank balance.
    """
    with open(f"bank_application/{self.customerId}.txt","w") as  write_new_file:
      pass
    """
    Write that user details of transaction in their file
    """
    with open(f"bank_application/{self.customerId}.txt","r+") as  new_file:
      history_id = 1
      history_data = str(history_id) +" "+ "opening" + " " + self.balance + " " + self.balance + "\n"
      new_file.seek(0,2)
      new_file.write(history_data)
    """
    Get the input from the user for to open the account
    """
  @classmethod
  def getInputFromUser(cls):
    """
    Read the existing file from the bank_db.txt
    """
    with open(filename,"r") as f:
      data=f.readlines()
    """
    Loop through the file
    """
    for i in range(len(data)):
      """
      Split the last user in the file and get the data like customerId,accountId and then increase the accountId and customerId to add another user
      """
      result=data[i].split()
      customerId=int(result[0])
      accountId = int(result[1])
      customerId+=1
      accountId+=1
    name=input("Enter your name: ")
    balance=int(input("Enter the initial amount must be thousand: "))
    password=input("Enter your password: ")
    repassword=input("Enter your password again: ")
    """
    Hashing the password like if the user enter 1 then the hashing password is 2 and if it is 9 means 0.z means a , Z means A
    """
    if password==repassword:
      ascii_value = [ord(i) for i in password]
      for j in range(len(ascii_value)):
        if ascii_value[j] == 90:
          ascii_value[j] = 64
        if ascii_value[j] == 122:
          ascii_value[j] = 96
        if ascii_value[j] == 57:
          ascii_value[j] = 47
      new_value = [k+1 for k in ascii_value]
      final_password=[chr(k) for k in new_value]
      password="".join(final_password)
      """
      After getting the user details we are going to give that to the constructor.    
      """
      Customer(str(customerId),name,str(balance),password,str(accountId))
    else:
      print("Enter the password again.")
  @classmethod
  def deposite(cls):
    customerId=input("Enter the customer ID: ")
    accountId = input("Enter the account ID: ")
    amount=int(input("Enter the amount that you want to deposite: "))
    """
    Reading the file to add the amount
    """
    with open("bank_application/bank_db.txt","r+") as readfile:
      data=readfile.readlines()
      for i in range(len(data)):
        result=data[i].split()
        cId = result[0]
        aId = result[1]
        """
        Using customerId and accountId to find the user
        """
        if cId == customerId and aId == accountId:
          """
          Adding that amount to the user
          """
          result[3]=str(int(result[3])+amount)
          dummy_result=" ".join(result)
          data[(int(cId)-1)]=dummy_result+"\n"
      original_result="".join(data)
      """
      Add the amount to the file
      """
    with open(filename,"w") as writefile:
      writefile.write(original_result)
      """
      Find the seperate user file and add the deposite details
      """
    with open(f"bank_application/{customerId}.txt","r+") as transaction_history:
      data=transaction_history.readlines()[-1]
      data = data.split()
      result = int(data[3])
      tId=int(data[0])
      data[0]=str(tId+1)
      data[1]="deposite"
      data[2] =str(amount)
      final_result =str(result + amount)
      data[3]=final_result+"\n"
      end=" ".join(data)
      transaction_history.write(end)
  @classmethod
  def withdrawl(cls):
    """
    Same as comments in the deposite function but it will substract the money instead of adding it.
    """
    customerId=input("Enter the customer ID: ")
    accountId = input("Enter the account ID: ")
    amount=int(input("Enter the amount that you want to withdraw: "))
    with open(filename,"r+") as readfile:
      data=readfile.readlines()
      for i in range(len(data)):
        result=data[i].split()
        cId = result[0]
        aId = result[1]
        if cId == customerId and aId == accountId:
          result[3]=str(int(result[3])-amount)
          if int(result[3])<1000:
            print("You don't have sufficient balance.")
          else:
            print(f"You withdraw {amount}")
            dummy_result=" ".join(result)
            data[(int(cId)-1)]=dummy_result+"\n"
            original_result="".join(data)
            with open(filename,"w") as writefile:
              writefile.write(original_result)
            with open(f"bank_application/{customerId}.txt","r+") as transaction_history:
              data=transaction_history.readlines()[-1]
              data = data.split()
              trans_result = int(data[3])
              tId=int(data[0])
              data[0]=str(tId+1)
              data[1]="withdraw"
              data[2] =str(amount)
              final_result =str(abs(trans_result - amount))
              data[3]=final_result+"\n"
              end=" ".join(data)
              transaction_history.write(end)
  @classmethod
  def transfer(cls):
    """
    Same as deposite function and withdraw function 
    but we are going to find the user using the same
    method in deposite and withdraw function.
    And then withdraw the amount from the user who are
    going to transact the amount and then getting
    the customerId and accountId to transact that amount to
    the other user and then adding the amount
    to the user.In this all the operation we are going to keep
    track of the user individual file and write the transaction details. 
    """
    print("Enter your details")
    customerId=input("Enter the customer ID: ")
    accountId = input("Enter the account ID: ")
    amount=int(input("Enter the amount that you want to withdraw: "))
    with open(filename,"r+") as readfile:
      data=readfile.readlines()
      for i in range(len(data)):
        first_result=data[i].split()
        cId = first_result[0]
        aId = first_result[1]
        if cId == customerId and aId == accountId:
          first_result[3]=str(int(first_result[3])-amount)
          if int(first_result[3])<1000:
            print("You don't have sufficient balance.")
          else:
            print(f"You withdraw {amount}")
            dummy_result=" ".join(first_result)
            data[(int(cId)-1)]=dummy_result+"\n"
            original_result="".join(data)
            with open(filename,"w") as writefile:
              writefile.write(original_result)
    with open(f"bank_application/{customerId}.txt","r+") as transaction_history:
      data=transaction_history.readlines()[-1]
      data = data.split()
      trans_result = int(data[3])
      tId=int(data[0])
      data[0]=str(tId+1)
      data[1]="transfered"
      data[2] =str(amount)
      final_result =str(trans_result - amount)
      data[3]=final_result+"\n"
      end=" ".join(data)
      transaction_history.write(end)
    print("Enter another person details to transfer the money.")
    customerId=input("Enter the customer ID: ")
    accountId = input("Enter the account ID: ")
    with open(filename,"r+") as readfile:
      data=readfile.readlines()
      for i in range(len(data)):
        result=data[i].split()
        cId = result[0]
        aId = result[1]
        if cId == customerId and aId == accountId:
          result[3]=str(int(result[3])+amount)
          dummy_result=" ".join(result)
          data[(int(cId)-1)]=dummy_result+"\n"
      original_result="".join(data)
    with open(filename,"w") as writefile:
      writefile.write(original_result)
    with open(f"bank_application/{customerId}.txt","r+") as transaction_history:
      data=transaction_history.readlines()[-1]
      data = data.split()
      result = int(data[3])
      tId=int(data[0])
      data[0]=str(tId+1)
      data[1]="transfered"
      data[2] =str(amount)
      final_result =str(result + amount)
      data[3]=final_result+"\n"
      end=" ".join(data)
      transaction_history.write(end)
  @classmethod
  def getTransactionalHistory(cls):
    """
    Get the individual user details like CustomerId to get their
    transaction details from their own file
    """
    customerId=input("Enter the customer ID: ")
    password=input("Enter your password: ")
    ascii_value = [ord(i) for i in password]
    for j in range(len(ascii_value)):
      if ascii_value[j] == 90:
        ascii_value[j] = 64
      if ascii_value[j] == 122:
        ascii_value[j] = 96
      if ascii_value[j] == 57:
        ascii_value[j] = 47
    new_value = [k+1 for k in ascii_value]
    final_password=[chr(k) for k in new_value]
    password="".join(final_password)
    with open(filename,"r") as readingHistory:
      data=readingHistory.readlines()
      for i in range(len(data)):
        result=data[i].split()
        cId=result[0]
        cPassword=result[4]
        if cId == customerId and cPassword == password:
          with open(f"bank_application/{customerId}.txt","r") as readthefile:
            read=readthefile.readlines()
            for i in range(len(read)):
              print(read[i])



loopFlag = 1
def tax():
  numTaxBrackets = int(input("How many tax brackets are there? "))
  
  nameCounter = 0
  
  taxBrackets = {}
  taxRates = {}
  taxableIncome = {}
  print("If a maximun is infinity. Just put inf")
  for i in range(numTaxBrackets):
    nameCounter+=1 #helps user keep track of which tax bracket and tax rate they are typing for
    strNameCounter = str(nameCounter)
    taxBrackets[strNameCounter] = float(input("The maximum value of tax bracket #" + strNameCounter + ": ")) 
    taxRates[strNameCounter] =  float(input("Tax Rate " + strNameCounter + ": ")) 
  
  Income = float(input("Annual Income:"))

  for i in taxRates:
    taxRates[i]= taxRates[i]/100
  
  
  for i in taxBrackets:
    formerItem = int(i) - 1
    strFormerItem = str(formerItem)
    if Income >= taxBrackets[i]: 
      if i != '1': 
          taxableIncome[i] = (taxBrackets[i] - taxBrackets[strFormerItem]) * taxRates[i] 
      elif i == '1': 
        taxableIncome[i] = (taxBrackets[i]) * taxRates[i]
      else: 
        print("Problem with index")
    if Income <= taxBrackets[i]: 
      if i == '1': 
        taxableIncome[i] = (taxBrackets[i]) * taxRates[i]
      elif i != 1:
        taxableIncome[i] = (Income - taxBrackets[strFormerItem]) * taxRates[i] 
      break
  
  
  taxedIncome = sum(taxableIncome.values())
  
  print("The amount you will pay in tax is $", taxedIncome)
  return
  




while loopFlag == 1: 
  Question = input("Do You Want To Calculate How Much You Will Pay In Taxes: 1 For Yes; 0 For No " )
  if Question.lower() == "1":
    tax()
    continue 
  if Question.lower() == "0":
    print("Thank You For Using The Tax Calculator")
    break 
  else: 
    print("Did Not Understand Response. Please Follow Instructions.")
    continue
 

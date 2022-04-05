# Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.
# Employee should have the following attributes:
# StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand,
# For Example:
# jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
# Create a method computePayment in class Employee which takes HoursWorked and date as input, and returns a payment information dictionary as follows: (if jg is an Employee object for worker Joe Green)
# We will assume a standard rate of 20% and a higher rate of 40%, and that PRSI at 4% is not subject to allowances. (we will ignore USC etc.)
# >>>jg.computePayment(42 '31/10/2021')
# {'name': 'Joe Green', 'Date':'31/10/2021', 'Regular Hours Worked':37,'Overtime Hours Worked':5,'Regular Rate':16,'Overtime Rate':24, 'Regular Pay':592,'Overtime Pay':120,'Gross Pay':712, 'Standard Rate Pay':710,'Higher Rate Pay':2, 'Standard Tax':142,'Higher Tax':0.8,'Total Tax':142.8,'Tax Credit':72, 'Net Tax':70.8, 'PRSI': 28.48,'Net Deductions':99.28, 'Net Pay': 612.72}
# Test your class and method thoroughly, and at a minimum include test cases testing the following:
# Net pay cannot exceed gross pay 
# #TestMethod
# def testNetLessEqualGross(self):
#   e=Employee(#Joe Green's Information)
#   pi=e.computePayment(1,'31/10/2021')
#   self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])
# Overtime pay or overtime hours cannot be negative.
# Regular Hours Worked cannot exceed hours worked
# Higher Tax cannot be negative.
# Net Pay cannot be negative.

class Employee:
  def __init__(self,StaffID,LastName,FirstName,RegHours,HourlyRate,OTMultiple,TaxCredit,StandardBand):
    self.StaffID=StaffID
    self.LastName=LastName
    self.FirstName=FirstName
    self.RegHours=RegHours
    self.HourlyRate=HourlyRate
    self.OTMultiple=OTMultiple
    self.TaxCredit=TaxCredit
    self.StandardBand=StandardBand

  def computePayment(self,HoursWorked,date):
    tax=0
    higherTax=0
    otHours=0
    hourOTpayment=0
    slrylessthnslab=0
    finopt={}
    otHours=HoursWorked-self.RegHours
    hourOTpayment=self.HourlyRate*self.OTMultiple
    fullName=(self.FirstName+' '+self.LastName)
    

    # print(hourOTpayment)  #extra pay for overtime
    if otHours>0:
      totalOTpayment=otHours*hourOTpayment
      # print(totalOTpayment)  #total ot payment
    else:
      print('notvalid')

    totalSalary=(self.RegHours*self.HourlyRate)+totalOTpayment
    # print(totalSalary)

 
    slrylessthnslab=totalSalary-self.StandardBand
    # print(slrylessthnslab)
    if slrylessthnslab>0:
      higherIncome=totalSalary-self.StandardBand
      stndrdTax=self.StandardBand*0.2
      higherTax=higherIncome*0.4
      tax=stndrdTax+higherTax
    else:
      stndrdTax=totalSalary*0.2
      higherTax=0
      tax=totalSalary*0.2

    netTax=tax-self.TaxCredit  ##add negative expection handling
    prsiSum=totalSalary*0.04
    netDeduction=netTax+prsiSum
    netPay=totalSalary-netDeduction

 
   

    
    finopt['name']=fullName
    finopt['Date']=date
    finopt['Regular Hours Worked']=self.RegHours
    finopt['Overtime Hours Worked']=otHours
    finopt['Regular Rate']=self.HourlyRate
    finopt['Overtime Rate']=hourOTpayment
    finopt['Regular Pay']=(self.RegHours*self.HourlyRate)
    finopt['Overtime Pay']=totalOTpayment
    finopt['Gross Pay']=totalSalary
    finopt['Standard Rate Pay']=self.StandardBand
    finopt['Higher Rate Pay']=higherIncome  
    finopt['Total Tax']=tax
    finopt['Tax Credit']=self.TaxCredit
    finopt['Net Tax']=netTax
    finopt['PRSI']=prsiSum
    finopt['Net Deductions']=netDeduction
    finopt['Net Pay']=netPay

    # print(finopt)

    
    return finopt

 
    
    
# abc= Employee(12345,'Green','Joe',37,16,1.5,72,710)
abc= Employee(12345,'Green','Joe',37,14,1.5,72,500)
print(abc.computePayment(42,'07/01/2022'))

# {'name': 'Joe Green',
#date--  'Date':'31/10/2021',
#RegHours--  'Regular Hours Worked':37,
#otHours-- 'Overtime Hours Worked':5,
#HourlyRate-- 'Regular Rate':16,
#hourOTpayment-- 'Overtime Rate':24,
#(self.RegHours*self.HourlyRate)--  'Regular Pay':592,
#totalOTpayment-- 'Overtime Pay':120,
#totalSalary-- 'Gross Pay':712,
#StandardBand--  'Standard Rate Pay':710,
#higherTax-- 'Higher Rate Pay':2, ++
# stndrdTax--'Standard Tax':142, ++
#higherTax-- 'Higher Tax':0.8, ++
#tax 'Total Tax':142.8,
#TaxCredit-- 'Tax Credit':72, 
#netTax-- 'Net Tax':70.8, 
#prsiSum-- 'PRSI': 28.48,
#netDeduction-- 'Net Deductions':99.28,
#netPay--  'Net Pay': 612.72}
# Test your class and method thoroughly, and at a minimum include test cases testing the following:
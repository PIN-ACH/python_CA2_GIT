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


import unittest

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
    higherTax=0
    higherIncome=0
    finopt={}
    otHours=HoursWorked-self.RegHours
    hourOTpayment=self.HourlyRate*self.OTMultiple
    fullName=(self.FirstName+' '+self.LastName)

    
    # print(hourOTpayment)  #extra pay for overtime
    #overtime pay less thn normal pay
    # if self.OTMultiple<=1:
    #   try: 
    #       raise ValueError('Overtime pay can\'t be less than regular pay.')
    #   except ValueError as e:
    #     return e


    #overtime less than normal time
    #if there is overtime and if there is no overtime
    if otHours>0:
      totalOTpayment=otHours*hourOTpayment
      totalSalary=(self.RegHours*self.HourlyRate)+totalOTpayment
    # print(totalOTpayment)  #total ot payment
    elif otHours<0:
      totalSalary=(self.RegHours+otHours)*self.HourlyRate
      totalOTpayment=0              #changing overtime payment to 0 as there was no overtime
      otHours=0                   #changing overtime hour to 0 as there was no overtime
      self.RegHours=HoursWorked  #change regular hours to hours worked. less work ws done

      # print(totalSalary)
    
    slrylessthnslab=totalSalary-self.StandardBand
    
    if slrylessthnslab>0:
      higherIncome=totalSalary-self.StandardBand
      stndrdTax=self.StandardBand*0.2
      higherTax=higherIncome*0.4
      tax=stndrdTax+higherTax
    else:
      stndrdTax=totalSalary*0.2
      tax=totalSalary*0.2
    
    if self.TaxCredit>tax:
      self.TaxCredit=tax
      netTax=tax-self.TaxCredit 
    else:
      netTax=tax-self.TaxCredit 

    #credit high than tax
    
    # if not netTax>0:
    #   try: 
    #       raise ValueError('Tax Credit higher than tax to be paid')
    #   except ValueError as e:
    #     return e

    prsiSum=totalSalary*0.04
    netDeduction=netTax+prsiSum
    netPay=totalSalary-netDeduction

    finopt['name']=fullName
    finopt['Date']=date
    finopt['Regular Hours Worked']=self.RegHours
    finopt['Overtime Hours Worked']="{:.2f}".format(otHours)
    finopt['Regular Rate']=self.HourlyRate
    finopt['Overtime Rate']="{:.2f}".format(hourOTpayment)
    finopt['Regular Pay']="{:.2f}".format(self.RegHours*self.HourlyRate)
    finopt['Overtime Pay']="{:.2f}".format(totalOTpayment)
    finopt['Gross Pay']="{:.2f}".format(totalSalary)
    finopt['Standard Rate Pay']=self.StandardBand
    finopt['Higher Rate Pay']="{:.2f}".format(higherIncome)
    finopt['Standard Tax']="{:.2f}".format(stndrdTax)
    finopt['Higher Tax']="{:.2f}".format(higherTax)
    finopt['Total Tax']="{:.2f}".format(tax)
    finopt['Tax Credit']=self.TaxCredit
    finopt['Net Tax']="{:.2f}".format(netTax)
    finopt['PRSI']="{:.2f}".format(prsiSum)
    finopt['Net Deductions']="{:.2f}".format(netDeduction)
    finopt['Net Pay']="{:.2f}".format(netPay)
    
    return finopt

 
    
    
  # abc= Employee(12345,'Green','Joe',37,16,1.5,72,710)
  # print(abc.computePayment(35,'07/01/2022'))
abc= Employee(12345,'Green','Joe',32,16,1,-10,710)
print(abc.computePayment(3,'07/01/2022'))





##test all cases
# Net pay cannot exceed gross pay 
class testEmployee(unittest.TestCase):
  def testNetLessEqualGross(self):
    e=Employee(12345,'Green','Joe',37,16,1.5,72,710)
    testit=e.computePayment(1,'31/10/2021')
    self.assertLessEqual(testit['Net Pay'],testit['Gross Pay'])

    # Overtime pay or overtime hours cannot be negative.
  def testGreaterEqualOT(self):
    e=Employee(12345,'Green','Joe',32,16,-1,72,300)
    testit=e.computePayment(9,'31/10/2021')
    self.assertGreaterEqual(testit['Overtime Hours Worked'],testit['Overtime Pay'],'0') #check athe cond#check otpay is converting from - to postv

# Regular Hours Worked cannot exceed hours worked
  # def testGreaterEqualOT(self):
  #   e=Employee(12345,'Green','Joe',32,16,-1,72,300)
  #   testit=e.computePayment(9,'31/10/2021')
  #   self.assertGreaterEqual(testit['Overtime Hours Worked'],testit['Overtime Pay'],'0')

# Higher Tax cannot be negative.
  def testHtaxcantbenagative(self):
    e=Employee(12345,'Green','Joe',37,16,1.5,72,710)
    testit=e.computePayment(10,'31/10/2021')
    self.assertGreaterEqual(testit['Higher Tax'],'0')

# Net Pay cannot be negative.
  def testnetpaycantbenagative(self):
      e=Employee(12345,'Green','Joe',37,16,1.5,10,710)
      testit=e.computePayment(1,'31/10/2021')
      self.assertGreaterEqual(testit['Net Pay'],'0')
      

unittest.main(argv=['ignored'],exit=False)
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
#higherTax-- 'Higher Rate Pay':2, 
# stndrdTax--'Standard Tax':142, 
#higherTax-- 'Higher Tax':0.8, 
#tax 'Total Tax':142.8,
#TaxCredit-- 'Tax Credit':72, 
#netTax-- 'Net Tax':70.8, 
#prsiSum-- 'PRSI': 28.48,
#netDeduction-- 'Net Deductions':99.28,
#netPay--  'Net Pay': 612.72}
# Test your class and method thoroughly, and at a minimum include test cases testing the following:
#  abc= Employee(12345,'Green','Joe',37,10,1.1,7,100)
# abc= Employee(12345,'Green','Joe',100,-1,-1,-100,800)
#credit high than tax
#overtime less than normal time
#overtime pay less thn normal pay
#param missing in employee
#param extra in employee
#pamarm in compute  payment
# regtime and hour worked

#pay cant be negav

# print(abc.computePayment(38,'07/01/2022'))
# print(abc.computePayment(37,'07/01/2022'))
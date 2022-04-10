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
    finalOutput={}
    otHours=HoursWorked-self.RegHours                #difference between  regular hour and actual hours worked 
    hourOTpayment=self.HourlyRate*self.OTMultiple     #overtime payment  per hour
    fullName=(self.FirstName+' '+self.LastName)         #Name concatination

    

    if self.TaxCredit<0 or self.StandardBand<0 or self.RegHours<0 or self.OTMultiple<0 or self.HourlyRate<0:  #values entered can't be negative.
      try: 
          raise ValueError('Class entered Values can\'t be negative.')
      except ValueError as e:
        return e
        
    if HoursWorked>168 or self.RegHours>168:
     try: 
      raise ValueError('A week can\'t have have hours more than 168')
     except ValueError as e:
      return e


    #if there is overtime and if there is under hours
    if otHours>=0: #for overtime
      totalOTpayment=otHours*hourOTpayment                           #overtime hrs worked into per hour overtime payment
      totalSalary=(self.RegHours*self.HourlyRate)+totalOTpayment     #gross income with OT
    elif otHours<0:   #for under hours worked
      totalSalary=(self.RegHours+otHours)*self.HourlyRate
      totalOTpayment=0                                                #changing overtime payment to 0 as there was no overtime
      otHours=0                                                       #changing overtime hour to 0 as there was no overtime
      self.RegHours=HoursWorked                                       #change regular hours to hours worked. less work was done

    
    slrylessthnslab=totalSalary-self.StandardBand                      #gross salary and the band difference
    
    if slrylessthnslab>0:                                               #if the difference is positive
      higherIncome=totalSalary-self.StandardBand                        #calculate higher income
      stndrdTax=self.StandardBand*0.2                                   #Calculate total amount of tax on standard income
      higherTax=higherIncome*0.4                                        #Calculate total amount of tax on higher income
      tax=stndrdTax+higherTax                                           #sum the taxes for tot tax deduction
    else:                                                               #if the difference is negative
      stndrdTax=totalSalary*0.2                                         #calculate standard tax
      tax=totalSalary*0.2                                               #calculate tot tax which is same as standard tax in this case
    
    if self.TaxCredit>tax:                                              #if tax credit is greater than tax 
      self.TaxCredit=tax                                                #tax and credit will be same 
      netTax=tax-self.TaxCredit                                         #tax will be 0, remaing credit will be deducted from next pay
    else:                                                               #if tax is greater than credit
      netTax=tax-self.TaxCredit                                         #deduct tax from credit


    prsiSum=totalSalary*0.04                                            #calculate prsi on gross salary
    netDeduction=netTax+prsiSum                                         #deduct prsi from gross incomee
    netPay=totalSalary-netDeduction                                     #net payment 
 


    finalOutput['name']=fullName
    finalOutput['Date']=date
    finalOutput['Regular Hours Worked']=self.RegHours
    finalOutput['Overtime Hours Worked']="{:.2f}".format(otHours)
    finalOutput['Regular Rate']=self.HourlyRate
    finalOutput['Overtime Rate']="{:.2f}".format(hourOTpayment)
    finalOutput['Regular Pay']="{:.2f}".format(self.RegHours*self.HourlyRate)
    finalOutput['Overtime Pay']="{:.2f}".format(totalOTpayment)
    finalOutput['Gross Pay']="{:.2f}".format(totalSalary)
    finalOutput['Standard Rate Pay']=self.StandardBand
    finalOutput['Higher Rate Pay']="{:.2f}".format(higherIncome)
    finalOutput['Standard Tax']="{:.2f}".format(stndrdTax)
    finalOutput['Higher Tax']="{:.2f}".format(higherTax)
    finalOutput['Total Tax']="{:.2f}".format(tax)
    finalOutput['Tax Credit']="{:.2f}".format(self.TaxCredit)
    finalOutput['Net Tax']="{:.2f}".format(netTax)
    finalOutput['PRSI']="{:.2f}".format(prsiSum)
    finalOutput['Net Deductions']="{:.2f}".format(netDeduction)
    finalOutput['Net Pay']="{:.2f}".format(netPay)
    return finalOutput
    

 
    
    
 #obj for employee1 
emp1= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
print(emp1.computePayment(42,'07/01/2022'))

#obj for employee2
emp2= Employee(5,'Howland','Tom',35,16,1.1,10,500)
print(emp2.computePayment(33,'07/01/2022'))





##test all cases
# Net pay cannot exceed gross pay 
class testEmployee(unittest.TestCase):
  def testNetLessEqualGross(self):
    e=Employee(1,'David','Mark',37,16,1.5,72,710)
    testit=e.computePayment(1,'31/10/2021')
    self.assertLessEqual(testit['Net Pay'],testit['Gross Pay'])


    # Overtime pay or overtime hours cannot be negative.
  def testGreaterEqualOT(self):
    e=Employee(2,'cuff','Jack',32,16,1,72,300)   #####fix
    testit=e.computePayment(50,'31/10/2021')
    self.assertGreaterEqual(testit['Overtime Hours Worked'],'0') 
    self.assertGreaterEqual(testit['Overtime Pay'],'0')
    
# Regular Hours Worked cannot exceed hours worked
  def testhrslessthnhrswork(self):
    e=Employee(3,'Marilynn','eden',32,16,2,72,300)
    testit=e.computePayment(12,'31/10/2021')
    self.assertLessEqual(testit['Regular Hours Worked'],12) 

# Higher Tax cannot be negative.
  def testHtaxcantbenagative(self):
    e=Employee(4,'Willard','Gael',37,16,1.5,72,100)
    testit=e.computePayment(56,'31/10/2021')
    self.assertGreaterEqual(testit['Higher Tax'],'0')

# Net Pay cannot be negative.
  def testnetpaycantbenagative(self):
      e=Employee(5,'Cornelius','Sabrina',37,16,1.5,10,710)
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
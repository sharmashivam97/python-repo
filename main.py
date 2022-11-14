accountNo = int(input("Enter account number"))
monthNo = int(input("Enter month number"))
elecPlan = input("Enter Elec. Plan")
elecUsed = int(input("Enter electricity used"))
gasPlan = input("Enter the gas plan")
gasUsed = int(input("Enter gas used"))
province = input("Enter province")
elecBill = 0.0
gasBill = 0.0
provinceList= ["AB","BC","MB","NT","NU","QC","SK","YT"]

tax = 0.0
if(elecPlan == "EFIR"):
    if(elecUsed > 1000):
        elecBill = elecUsed*0.0941
    else:
        elecBill = elecUsed*0.0836
else:
    elecBill = 0.0911 * elecUsed
if(gasPlan == "GFIR"):
    if(gasUsed>950):
        gasBill = gasUsed * 0.0589
    else:
        gasBill = gasUsed * 0.0456
else:
    gasBill =gasUsed * 0.0393
totalBill = 120.62 + gasBill + elecBill + 1.32
if(province in provinceList):
    totalBill = 1.05 * totalBill
elif(province == "ON"):
    totalBill = totalBill * 1.13
else:
    totalBill = totalBill * 1.15
print("Thank you! Your total amount due now is: $"+ str(round(totalBill,2)))
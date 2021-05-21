"""
empData={}
empData1={}
def detailss():
    empname=input("Enter the emp name")
    empAge=input("Enter the emp age")
    empAdd=input("Enter the emp address")

    empData1["empname"]=empname
    empData1["empAge"]=empAge
    empData1["empAdd"]=empAdd
    empData["empDetails"]= empData1
    for details in empData.items():
       print(details)
detailss()
for number in range(0,5):
    deci=input("Do you want to insert more")
    if deci == "yes":
       detailss()
    else:
        break
"""
mydict = {}
bnn=1
bn=mydict.get(bnn)
print(bn)

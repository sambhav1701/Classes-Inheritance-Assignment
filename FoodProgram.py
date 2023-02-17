import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}
order_total = 0

customer1 = fc.Customer("570", "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False)
customer2 = fc.Customer("569", "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True)


#transaction1 = fc.Transaction(dict['trans1'][0], dict['trans1'][1], dict['trans1'][2], dict['trans1'][3])
#transaction2 = fc.Transaction(dict['trans2'][0], dict['trans2'][1], dict['trans2'][2], dict['trans2'][3])
#transaction3 = fc.Transaction(dict['trans3'][0], dict['trans3'][1], dict['trans3'][2], dict['trans3'][3])
#transaction4 = fc.Transaction(dict['trans4'][0], dict['trans4'][1], dict['trans4'][2], dict['trans4'][3])


print("Customer Name: ",customer1.get_name())
print("Phone: ",customer1.get_phone())
cost = 0
for key, value in dict.items():
    if str(value[3]) == customer1.get_customerid():
        if customer1.is_member:
            discountprice = value[2] * 0.8
            print("Order Item:" , value[1] , "Price =" , value[2])
        else:
            print("Order Item:" , value[1] , "Price =" , value[2])
        cost += value[2] 
print("Total Cost:", cost)


print("Customer Name: ",customer2.get_name())
print("Phone: ",customer2.get_phone())
cost = 0
for key, value in dict.items():
    if str(value[3]) == customer2.get_customerid():
        if customer2.is_member:
            discountprice = value[2] * 0.8
            print("Order Item:" , value[1] , "Price =" , value[2])
        else:
            print("Order Item:" , value[1] , "Price =" , value[2])
        cost += value[2] 
print("Total Cost:", cost)
print("Member Discount: ", cost * 0.8)
print("Total Cost after discount:", cost - (cost * 0.8))
                   
        



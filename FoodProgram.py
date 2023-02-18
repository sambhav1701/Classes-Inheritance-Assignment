import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}


customer1 = fc.Customer("570", "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False)
customer2 = fc.Customer("569", "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True)



#transaction1 = fc.Transaction(dict['trans1'][0], dict['trans1'][1], dict['trans1'][2], dict['trans1'][3])
#transaction2 = fc.Transaction(dict['trans2'][0], dict['trans2'][1], dict['trans2'][2], dict['trans2'][3])
#transaction3 = fc.Transaction(dict['trans3'][0], dict['trans3'][1], dict['trans3'][2], dict['trans3'][3])
#transaction4 = fc.Transaction(dict['trans4'][0], dict['trans4'][1], dict['trans4'][2], dict['trans4'][3])

transaction_instance = []
for key, value in dict.items():
    transaction = fc.Transaction(value[0], value[1], value[2], value[3])
    transaction_instance.append(transaction)
    #print(transaction_instance)

for customer in [customer1, customer2]:
    order_total = 0

    print("Customer Name: ",customer.get_name())
    print("Phone: ",customer.get_phone())

    for transaction in transaction_instance:
        if int(transaction.get_customerid()) == int(customer.get_customerid()):
            order_total += transaction.get_cost()
            print("Order Item:" , transaction.get_itemname() , "Price =" , transaction.get_cost())
            

    if customer.is_member():
        discount = order_total * 0.2
        print("Total Cost:", order_total)
        print("Member Discount: ", discount)
        print("Total Cost after discount:", order_total - discount)
    else:
        print("Total Cost:", order_total)

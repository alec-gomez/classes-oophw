import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }

order_total = 0


# first customer id
customer1 = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712",
                        "dsellyarft@gmpg.org", "254-555-9362", "false")

# return first customer info (name and phone num)
print(f"Customer Name: {customer1.get_name()}")
print(f"Customer Phone: {customer1.get_phone()}")

# item of customer 1
print(
    f"Order Item: {dict['trans3'][1]} Price: $ {format(dict['trans3'][2], ',.2f')}")
print(
    f"Order Item: {dict['trans4'][1]} Price: $ {format(dict['trans4'][2], ',.2f')}")

# cost customer 1
if customer1.get_mem_status() == 'False':
    order_total = dict["trants3"][2] + dict["trans4"][2]
    print(f"Total Cost: ${format(order_total, ',.2f')}")
    print()
elif customer1.get_mem_status() == 'True':
    order_total = dict["trans3"][2] + dict["trans4"][2]
    discount = order_total * 0.20
    discount_total = order_total - discount
    print(f"Total Cost: ${format(order_total, ',.2f')}")
    print(f"Member Discount: ${format(discount, ',.2f')}")
    print(f"Total Cost After Discount: ${format(discount_total, ',.2f')}")
    print()
else:
    print("Not Valid Member Status")

# second customer id
customer2 = fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710",
                        "ahimsworthfs@list-,anage.com", "254-555-2273", "true")

# return second customer info (name and phone num)
print(f"Customer Name: {customer2.get_name()}")
print(f"Customer Phone: {customer2.get_phone()}")

# item of customer 2
print(
    f"Order Item: {dict['trans1'][1]} Price: ${format(dict['trans1'][2], ',.2f')}")
print(
    f"Order Item: {dict['trans2'][1]} Price: ${format(dict['trans2'][2], ',.2f')}")

# cost of customer 2
if customer2.get_mem_status() == 'False':
    order_total = dict['trans1'][2] + dict["trans2"][2]
    print(f"Total Cost: {format(order_total, ',.2f')}")
    print()
elif customer2.get_mem_status() == 'True':
    order_total = dict["trans1"][2] + dict["trans2"][2]
    discount = order_total * 0.20
    discount_total = order_total - discount
    print(f"Total Cost: ${format(order_total, ',.2f')}")
    print(f"Member Discount: $ {format(discount, ',.2f')}")
    print(f"Total Cost After Discount: ${format(discount_total, ',.2f')}")
    print()
else:
    print("Not Valid Member Status")

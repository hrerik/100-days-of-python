import random

friends = ["Ana","Bob,","Carl","Denis","Edward","Felix","Gabriel","Helga","Ivan"]

list_size = len(friends)
id_bill = random.randint(0,list_size-1) # "-1" for no index out of range

print(f"{friends[id_bill]} will pay the bill today!!")

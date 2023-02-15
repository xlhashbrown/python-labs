# Program 7: using list indexing
regions = ["North", "South", "East", "West"]
sales = [70000, 40000, 120000, 55000]
employees = ["Alex", "Gertrude", "Hughie", "Zack"]

print("Region:",regions[1],"\tSales:",sales[0]) # you can quickly reference a value in a list with "list[position]"
print("Region:",regions[-1],"\tSales:",sales[-1]) # a negative value rolls over to the end of the list

employees[2] = "Reginald"

for employee in employees:
    print(employee)
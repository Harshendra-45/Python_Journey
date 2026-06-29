def gen_bill():
    pid = int(input("Enter patient id"))
    cons_charge = int(input("Enter consultation fees"))
    med_cost =int(input("Enter medicine cost"))
    test_cost =int(input("Enter test cost"))

    Total = cons_charge+med_cost+test_cost
    print("Bill for ", pid)
    print(Total)
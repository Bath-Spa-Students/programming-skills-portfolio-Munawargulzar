sandwich_orders = ['beef sandwich', 'chicken sandwich', 'meat sandwich' , 'salad sandwich']
finished_sandwiches =[] 

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"I  made your {current_sandwiches}.")
    finished_sandwiches.append (current_sandwiches)

    print("\nSandwiches that were made:")
    for sandwich in finished_sandwiches:
        print(sandwich)






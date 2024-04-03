sandwich_orders =['pastrami','Egg sandwich', 'Pastrami','  Chicken sandwich' , 'Meatball sandwich', 'Pastrami' , 'Olive sandwich']
finhished_sandwiches= []

print("The deli has run out of pastrami.")

while'pastrami' in sandwich_orders:
      sandwich_orders.remove('pastrami')

while sandwich_orders:
      current_sandwich = sandwich_orders.pop()
      print(f"I made your {current_sandwich}.")   
      finhished_sandwiches.append(current_sandwich) 

      print("\nSandwiches that were made;")
      for sandwiches in finhished_sandwiches:
          print(sandwiches)
     



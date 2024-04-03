prompt= "how old are you?"
prompt+= "\nEnter 'quit' when ypu are finishrd."

while True: 
    age = input(prompt)
    if age == 'quit':
        break
    age= int (age)

    if age < 5:
        print("your ticket is $20.")
    else:
        print(" your tickrt os $25.")
        
        
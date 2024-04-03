# Initial list of guests
guests = ['inez', 'g', 'elsa', 'aiza']

# Print a message indicating only two guests can be invited
print("Sorry, the dinner table won't arrive in time, so we can only invite two guests for dinner.\n")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I'm unable to invite you to dinner.")

# Print messages to the remaining two guests, letting them know they're still invited
for remaining_guest in guests:
    print(f"{ remaining_guest }, you're still invited to dinner.")

# Use del to remove the last two names from the list
del guests[:]
print("\nThe guest list is now empty:", guests )
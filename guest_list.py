guest_list = ['Bernie', 'Obama', 'Reich'] 

del guest_list[0]
guest_list.append('Fran')
print(f"{guest_list[0]}! Please come to dinner!")
print(f"{guest_list[1]}! Please come to dinner!")
print(f"{guest_list[2]}! Please come to dinner!")

guest_list.insert(0, 'Boy')
print(guest_list)

guest_list.pop(2)
print(f"So sorry you can't come {guest_list.pop(2)}")

guest_list.pop(1)
print(f"So sorry you can't come {guest_list.pop(0)}")

# Guest list is now empty
print(f"The number of guests invited is {len(guest_list)}")
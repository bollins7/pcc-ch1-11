guest_list = ['Bernie', 'Obama', 'Reich']
print(f"{guest_list[0]}! Please come to dinner!")
print(f"{guest_list[1]}! Please come to dinner!")
print(f"{guest_list[2]}! Please come to dinner!")

del guest_list[0]
guest_list.append('Fran')
print(f"{guest_list[0]}! Please come to dinner!")
print(f"{guest_list[1]}! Please come to dinner!")
print(f"{guest_list[2]}! Please come to dinner!")
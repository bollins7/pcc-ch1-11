# for every magician in the list of magicians, print the magician
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

    print(f"{magician.title()}, that was a great trick!")

    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    # doing something after a for loop, but not in the loop
print("Thank you, everyone. That was a great magic show!")
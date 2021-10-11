#Do not compleate solution in this area! See private sections for coding space

OPTIONS = [
    "Hugo's Solution", "Murdoch's Solution", "Adam's Solution",
    "Saim's Solution"
]
possible_choice = ['1', '2', '3', '4']

print("Which solutions would you like to run: ")

for num in range(len(OPTIONS)):
    print(str(num + 1) + '.', OPTIONS[num])

user_choice = input("Enter your selection: ")
while user_choice not in possible_choice:
    user_choice = input("INVALID option. Enter your selection: ")

if user_choice == '1':
    import hugoSolution

elif user_choice == '2':
    import murdochSolution
    murdochSolution.solution()

elif user_choice == '3':
    import adamSolution
    adamSolution.solution()

elif user_choice == '4':
    import saimSolution
    saimSolution.solution()

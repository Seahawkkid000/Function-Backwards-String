#Program to write a string backwords
string=input("Enter a string")
print("1. Reverse your string")
print("2. Create a new string")
print("3. Exit")
while True:
    choice=int(input("Enter your choice"))
    if(choice==1):
        reverse_string=string[-1:-len(string)-1:-1]
        def string_reverse(string):
            print("Here is how your string looks reversed:", reverse_string)
            while True:
                choice2=input("Are you sure you want to reverse it permanantly?")
                choice2=choice2.lower()
                if(choice2=='yes'):
                    reverse_string=string
                    print("Your string is", string)
                    break
                elif(choice=='no'):
                    break
                else:
                    print("Invalid Input")

        string_reverse(string)
    elif(choice==2):
        string=input("Enter a string")
        print("1. Reverse your string")
        print("2. Create a new string")
        print("3. Exit")
        reverse_string=string[-1:-len(string)-1:-1]
    elif(choice==3):
        break
    else:
        print("Invalid Input")

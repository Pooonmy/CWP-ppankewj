import sys

if len(sys.argv) != 2:
    print("none")
else:
    secret_word = sys.argv[1]
    
    user_input = input("What was the parameter? ")
    
    if user_input == secret_word:
        print("Good job!")
    else:
        print("Nope, sorry...")

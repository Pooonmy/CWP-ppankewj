import sys

parameters = sys.argv[1:]

if not parameters:
    print("none")
else:
    print(f"parameters: {len(parameters)}")
    
    for param in parameters:
        print(f"{param} {len(param)}")

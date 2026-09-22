import sys

if len(sys.argv) != 2:
    print("none")
else:
    text_string = sys.argv[1]
    
    z_count = text_string.count("z")
    
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)

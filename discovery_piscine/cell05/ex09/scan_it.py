import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text_string = sys.argv[2]
    
    count = text_string.count(keyword)
    
    if count == 0:
        print("none")
    else:
        print(count)

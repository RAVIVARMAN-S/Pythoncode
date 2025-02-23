def shuffle_string(string,indexes_list):
    for i in indexes_list:
    
        b=string[int(i)]
        print(b,end="")


string = input()
indexes_list = input().split()
shuffle_string(string, indexes_list)

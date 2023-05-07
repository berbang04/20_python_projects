def binary_search(list,element):
    start=0
    middle=0
    end=len(list)
    steps=0

    while(start<=end):
        print("steps: ",steps, ":", str(list[start:end+1]))
        steps=steps +1

        middle=(start+end)//2
        if list[middle]==element:
            return middle
        elif list[middle] <element:
            start=middle+1

        else :
            end=middle-1
    return -1        
my_list=[1,2,3,4,5,6,7,8,9]
target=1
binary_search(my_list,target)
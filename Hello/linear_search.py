target = 5;
list = [1,2,3,4,5,6,7,8,9,0];
print(list)
def linear_search(list, target):
    # Returns the index position of the target if found, else return none
    for i in range(0,len(list)):
        if list[i] ==target:
            print(i);
            return i
    print('None');        
    return None;


def verify(index):
    if index is not None:
        print("Target found at index",index)
    else:
        print("Target not found in list");

linear_search(list,target)
target = 90;
list = [0,1,2,3,4,5,6,7,8,9];
def binary_search(target,list):
    first = 0;
    last = len(list) -1;

    while first <= last:
        midpoint =(first+last)//2;

        if list[midpoint] == target:
            print(midpoint);
            return midpoint;
        elif list[midpoint] < target:
            first = midpoint + 1;
        else:
            last = midpoint -1;
    print("value does'nt exist in list")
    return None;

binary_search(target,list);
 
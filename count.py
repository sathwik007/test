num_to_find = int(input("Enter the number to be found :-\n"))

a=[2,20,30]

def occur1(a,num_to_find):
    j = i = 0
    while j==0:
        if a[len(a)-1] > num_to_find:
            if num_to_find < a[i]:
                j=1
                return i
                break
            else:
                i = i + 1
        else:
            return "The entered number is greater than the numbers in the list"
            j=1

print(occur1(a,num_to_find)) 

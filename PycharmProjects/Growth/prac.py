
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            print(arr[left], arr[right])
            break
        elif total < target:
            left +=1
        else:
            right -=1
    return [-1, +1]


arr = [2, 3, 4, 5, 8 ]
print(two_sum(arr,10))
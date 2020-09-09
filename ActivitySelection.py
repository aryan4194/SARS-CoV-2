'''ACTIVITY SELECTION PROBLEM'''
'''GREEDY ALGORITHM'''

n = int(input())
start = list(map(int, input().split()))
finish = list(map(int, input().split()))
arr = list()
arr1 = list()
arr = sorted(finish)
count = 0
print(arr)
for i in range(n):
    ind = finish.index(arr[i])
    arr1.append(start[ind])
    finish.pop(ind)
    finish.insert(ind, -1)
print(arr1)
k = 0
for j in range(n):
    if j == 0:
        count = 1
        continue
    else:
        if arr1[j] >= arr[k]:
            count += 1
            k = j
print(count)
nums = [1,2,4,7,4,9]

for i in nums:
    if i in nums:
        nums.remove(i)
        if i in nums:
            duplicate = i
        else:
            continue
    else:
        continue

print(duplicate)

nums = [3,2,4]
target = 6

nums.sort()
numsDic=dict(zip(range(len(nums)),nums))

for index1 in range(len(nums)) :
    if nums[len(nums)-1-index1] > target :
        continue
    else:
        resi = target - nums[len(nums)-1-index1]
        for k, v in numsDic.items():
            if v == nums[len(nums)-1-index1]:
                output1 = k
        for index2 in range(len(nums)-index1-1):
            if nums[index2] > resi:
                break
            else:
                if nums[index2] == resi:
                    print(nums[len(nums)-1-index1],nums[index2])
                    for k, v in numsDic.items():
                        if v == nums[index2]:
                            output2 = k
                            
                

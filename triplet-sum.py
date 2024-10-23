def trip(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        first, last = i + 1, len(nums) - 1
        while first < last:
            total = nums[i] + nums[first] + nums[last]
            if total < 0:
                first += 1
            elif total > 0:
                last -= 1
            else:
                triplets.append([nums[i], nums[first], nums[last]])
                while first < last and nums[first] == nums[first + 1]:
                    first += 1
                while first < last and nums[last] == nums[last - 1]:
                    last -= 1
                first += 1
                last -= 1
    return triplets

ui = input()
nums = list(map(int, ui.split()))
result = trip(nums)
print(result)

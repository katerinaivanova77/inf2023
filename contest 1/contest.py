nums = list(map(int, input().split()))
def maxik(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    prev_max = nums[0]
    curr_max = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        temp = curr_max
        curr_max = max(prev_max + nums[i], curr_max)
        prev_max = temp

    return curr_max
result = maxik(nums)
print(result)

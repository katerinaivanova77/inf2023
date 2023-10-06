nums = list(map(int, input().split()))
def largestNumber(nums):
    nums = [str(num) for num in nums]

    def compare(x, y):
        return int(y + x) - int(x + y)
    def key_
    nums.sort(key=compare)

    largest_num = ''.join(nums)

    return largest_num
result = largestNumber(nums)
print(result)

nums = input("Enter  numbers separated by space: ")
nums = list(map(int, nums.split(" ")))

avg = sum(nums) / len(nums)

print("Average:", avg)

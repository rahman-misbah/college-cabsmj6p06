nums = input("Enter 3 number separated by spaces: ")
nums = list(map(int, nums.split(" ")))

prod = 1

for i in nums: prod *= i

print(f"Sum: {sum(nums)}")
print(f"Product: {prod}")
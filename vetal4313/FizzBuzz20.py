numbers = []
with open('numbers.txt', 'r') as f:
    items = f.read().split('\n')

    for i in items:
        numbers.append([int(n) for n in i.split(',')])
    for nums in numbers:
        for num in range(1, nums[2], 1):

            if num % nums[0] == 0:
                print("F", end="")

            elif num % nums[1] == 0:
                print("B", end="")

            elif num % (nums[1] + nums[2]) == 0:
                print("FB", end="")

            else:
                print(num, end="")
            f.close()
        print(num)
save_res = open('text.txt', 'w')
for index in nums:
    save_res.write(str(index) + "\t")
save_res.close()


f.close()

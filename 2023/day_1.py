
with open('input.txt', 'r') as file:
    total_sum = 0
    nums = ['one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    line = file.readline()

    while line:
        l = 0
        r = len(line) - 2

        while l < len(line) - 2:
            if line[l].isdigit():
                l = line[l]
                break

            if line[l:l+3] in nums:
                l = str(nums.index(line[l:l+3]) + 1)
                break

            if line[l:l+4] in nums:
                l = str(nums.index(line[l:l+4]) + 1)
                break

            if line[l:l+5] in nums:
                l = str(nums.index(line[l:l+5]) + 1)
                break

            l += 1

        while r > 0:
            if line[r].isdigit():
                r = line[r]
                break

            if line[r-2:r+1] in nums:
                r = str(nums.index(line[r-2:r+1]) + 1)
                break

            if line[r-3:r+1] in nums:
                r = str(nums.index(line[r-3:r+1]) + 1)
                break

            if line[r-4:r+1] in nums:
                r = str(nums.index(line[r-4:r+1]) + 1)
                break

            r -= 1

        print(r)
        total_sum += int(l + r)
        line = file.readline()

    print(total_sum)

# n = 123456
# sn = str(n)
# p = 1
# s = 0
# for d in sn:
#     p *= int(d)
#     s += int(d)

# print(p-s)

# pattern = "0"
# s = "y"

# patlen = len(pattern)
# slen = len(s)
# limit = slen - patlen
# matchcnt = 0
# for i in range(0, limit + 1):
#     sSub = s[i:(i + patlen)]
#     patmatch = []
#     for j in range(0, patlen):
#         if sSub[j].lower() in ('a', 'e', 'i', 'o', 'u') and pattern[j] == "0":
#             patmatch.append("T")
#         elif sSub[j].lower() not in ('a', 'e', 'i', 'o', 'u') and pattern[j] == "1":
#             patmatch.append("T")
#         else:
#             patmatch.append("F")
#     if "F" not in patmatch:
#         matchcnt += 1

# print(matchcnt)


def twoSum(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in nums[i+1:len(nums)]:
            print(nums[i+1:len(nums)].index(target - nums[i]))


print(twoSum([3, 3], 6))

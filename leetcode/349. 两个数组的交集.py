def solution(nums_1,nums_2):
    n1 = set(nums_1)
    n2 = set(nums_2)
    res = []
    for i in n1:
        if i in n2:
            res.append(i)

    return res



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
solution(nums1,nums2)

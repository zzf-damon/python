def first(nums):
    stack = []
    length = len(nums)
    res = [-1] * length
    for pre in range(length):
        while stack and nums[stack[-1]] < nums[pre]:
            tem = stack.pop()
            res[tem] = pre - tem
        stack.append(pre)
    return res


a = [4, 9, 2, 6, 8, 1, 7]
print(first(a))


def second(nums):
    nums = sorted(nums)
    length = len(nums)
    res = [0] * length
    pre, pro = length // 2, length // 2 + 1
    point = length - 2
    while pre > 0 and pro < length:
        res[pre] = nums[point]
        res[pro] = nums[point + 1]
        point -= 2
        pre -= 1
        pro += 1
        if point == -1:
            res[pre] = nums[point + 1]

    res.append(res[0])
    count = 0
    for i in range(length):
        count = max(count, abs(res[i] - res[i + 1]))

    return count


b = [2, 4, 7, 8, 10, 12, 15]
print(second(b))


def third(n, nums):
    nodesCount = 10000
    parent = list(range(nodesCount + 1))

    def find(index: int) -> int:
        if parent[index] != index:
            parent[index] = find(parent[index])
        return parent[index]

    def union(index1: int, index2: int):
        parent[find(index1)] = find(index2)

    res = []

    for i, x, y in nums:
        if i == 1:
            if find(x) != find(y):
                union(x, y)
        else:
            res.append([i, x, y])
    count = 0
    for i, x, y in res:
        if find(x) == find(y):
            count += 1

    return count


n = 4
nums = [[1, 1, 2], [2, 1, 3], [2, 1, 4], [1, 2, 3]]
print(nums)
print(third(n, nums))
n = 2
nums = [[1, 1, 2], [1, 2, 3]]
print(nums)
print(third(n, nums))


def fourth(nums):
    maxs = []
    lists = []
    k = 1
    length = len(nums)
    for i in range(length):
        max_h = 1
        tem = i
        if i == length - 1:
            order = [nums[tem]]
            maxs.append(max_h)
            lists.append(order)
        else:
            for index in range(i + 1, length):
                max_h = 1
                tem = i
                order = [nums[tem]]
                for j in range(index, length):
                    if check(nums[tem], nums[j]):
                        max_h += 1
                        tem = j
                        order.append(nums[j])
                maxs.append(max_h)
                lists.append(order)
                k += 1
    max_h = 0
    recoder_index = 0
    for i in range(len(maxs)):
        if maxs[i] > max_h:
            max_h = maxs[i]
            recoder_index = i
    print(max_h)
    print(lists[recoder_index])


def check(s1, s2):
    if abs(len(s1) - len(s2)) > 1: return False
    flat = len(s1) - len(s2)
    minlength = len(s2) if len(s1) > len(s2) else len(s1)
    for i in range(minlength):
        if s1[i] == s2[i]:
            continue
        if flat == 0:
            return s1[i + 1:] == s2[i + 1:]
        elif flat == 1:
            return s1[i + 1:] == s2[i:]
        else:
            return s1[i:] == s2[i + 1:]
    return True


a = ["cat", "dig", "dog", "fig", "fin", "fine", "fog", "log", "wine"]

fourth(a)

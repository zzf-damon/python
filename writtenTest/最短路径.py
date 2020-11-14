input = [["start", "A", 10],
         ["start", "B", 2],
         ["start", "C", 5],
         ["A", "B", 6],
         ["A", "C", 4],
         ["B", "C", 2],
         ]


def strut_path(S_list):
    res = []
    dict1 = {}
    for i in input:
        for j in i:
            m = min(j[2],dict1.get(j[0]))
            dict1[j[0]] = m




strut_path(input)

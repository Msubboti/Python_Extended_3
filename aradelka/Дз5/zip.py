def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))


s = [1, 2, 4, 5]
t = ('f', 'f', 'f')
d = ('a', 'a')
g = list((s[i], t[i], d[i]) for i in shortest_sequence_range(s, t, d))

# for item in g:
#     print(item)
print(g)

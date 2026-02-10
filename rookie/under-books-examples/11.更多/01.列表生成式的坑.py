# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

""" 坑点,意思一样改简洁  """
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[0] * len(courses)] * len(names)
# # scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)

a = [None] * 2
print([id(i) for i in a])	# [140708600660288, 140708600660288]
a[0] = 1
print(a)					# [1, None]

b = [[None] * 2] * 3
print([id(i) for i in b])	# [2388733524288, 2388733524288, 2388733524288]
b[0] = [1, 1]
print(b)					# [[1, 1], [None, None], [None, None]]

c = [[None] * 2] * 3
print([id(i) for i in c])	# [2388733524544, 2388733524544, 2388733524544]
c[0][0] = 1					# [[1, None], [1, None], [1, None]]
print(c)

d = [[None] * 2 for _ in range(3)]	# [2388733523648, 2388733519488, 2388732361024]
print([id(i) for i in d])			# [[1, None], [None, None], [None, None]]
d[0][0] = 1
print(d)

# def add_end(L=[]):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
# def add_end2(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
# if __name__ == '__main__':
#     print(add_end())
#     print(add_end())
#     print(add_end())
#     print(add_end2())
#     print(add_end2())
#     print(add_end2())


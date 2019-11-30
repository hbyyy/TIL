# # Strategy:  Iterate over a copy
# # users = {
# #     'hby': 'inactive',
# #     'hbb': 'active',
# #     'kbs': 'inactive',
# #     'asd': 'inactive',
# #     'ewq': 'active',
# #     'uyt': 'inactive'
# # }
# #
# users1 = ['1','2','3','4','5','6','7','8','9','0']
# users2 = users1.copy()
# # print(users2)
# # print(users1)
# #
# #
# # print(users2)
# # print(users1)
# for idx, user in enumerate(users1.copy()):
#     print((idx, user))
#     print(users1)
#     if idx% 2 == 0:
#         users1.remove(user)

nationWidth = {
	'korea': 220877,
	'Rusia': 17098242,
	'China': 9596961,
	'France': 543965,
	'Japan': 377915,
	'England' : 242900,
}

w = nationWidth['korea']
nationWidth.pop('korea')
l = list(nationWidth.items())
gap = max(nationWidth.values())
item = 0

for i in l:
    if gap > abs(i[1] - w):
        gap = abs(i[1] - w)
        item = i
print(item[0],item[1]-220877)

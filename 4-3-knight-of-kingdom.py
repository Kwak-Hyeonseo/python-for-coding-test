N = input()
row_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = (row_list.index(N[0]))
col = int(N[1])-1
case = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
cnt = 0
for i in case:
  if 0 <= row + i[0] < 8 and 0 <= col + i[1] < 8:
    cnt += 1 
print(cnt)

# The matrix problem


n, m = list(map(int,input().split(' ')))


matrix = [input()]
for _ in range(n):
    matrix=matrix.append(_)

#matrix = [input() for _ in range(n)]
string = ''.join([''.join(i) for i in zip(*matrix)])
print(re.sub(r'(?<=\w)[^\w]+(?=\w)',' ',string))


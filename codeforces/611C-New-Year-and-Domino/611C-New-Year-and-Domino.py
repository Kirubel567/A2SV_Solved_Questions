#build the horizontal counter
h_counter = [[0]*(w+1) for _ in range(h+1)]
v_counter = [[0]*(w+1) for _ in range(h+1)]

for i in range(len(mat)): 
    for j in range(len(mat[0])-1):
        if mat[i][j] == "." and mat[i][j+1] == ".": 
            h_counter[i+1][j+1] = 1

for i in range(len(mat)-1): 
    for j in range(len(mat[0])):
        if mat[i][j] == "." and mat[i+1][j] == ".": 
            v_counter[i+1][j+1] = 1

#pref_sum building
for i in range(1, h+1): 
    for j in range(1, w+1): 
        h_counter[i][j] += h_counter[i-1][j] + h_counter[i][j-1] - h_counter[i-1][j-1]
        v_counter[i][j] += v_counter[i-1][j] + v_counter[i][j-1] - v_counter[i-1][j-1]

def query(P, r1, c1, r2, c2): 
    if r1>r2 or c1>c2: 
        return 0
    return P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1]

q = int(input())
for _ in range(q): 
    r1, c1, r2, c2 = map(int, input().split())

    horizontal = query(h_counter, r1, c1, r2, c2-1)
    vertical = query(v_counter, r1, c1, r2-1, c2)

    print(horizontal+vertical)
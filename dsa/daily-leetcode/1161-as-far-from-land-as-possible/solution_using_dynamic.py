def maxDist(mat):
    rows = len(mat)
    cols = len(mat[0])
    max_dist = len(mat) + len(mat[0]) + 1
    dist = [[max_dist for _ in range(len(mat[0]))] for _ in range(len(mat))]

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                dist[i][j] = 0
            else:
                curr_min_dist = min((dist[i-1][j] + 1 if i>0 else max_dist), (dist[i][j-1] + 1 if j > 0 else max_dist))
                dist[i][j] = min(dist[i][j], curr_min_dist)

    # second pass
    ans = float('-inf')
    for i in range(rows -1, -1, -1):
        for j in range(cols -1, -1, -1):
            curr_min_dist = min((dist[i+1][j] + 1 if i < rows - 1 else max_dist), (dist[i][j+1] + 1 if j < cols-1 else max_dist))
            dist[i][j] = min(dist[i][j], curr_min_dist)

            ans = max(ans, dist[i][j])

    return ans if ans != 0 or ans != max_dist else -1


if __name__ == "__main__":
    mat = [[0,1,0,1],
           [0,0,1,0],
           [0,1,1,1],
           [0,0,0,0]]
    print(maxDist(mat))

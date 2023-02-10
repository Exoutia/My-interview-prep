from collections import deque
def min_distance(mat: list):
    dis = -1
    vis = mat.copy()
    dq = deque((i, j) for i in range(len(vis)) for j in range(len(vis)) if vis[i][j]==1)

    while dq:
        curr_size = len(dq)
        while curr_size:
            org_x_cor, org_y_cor = dq.popleft()
            for i, j in ((0,-1), (0, 1), (-1, 0), (1, 0)):
                x_cor = org_x_cor + i
                y_cor = org_y_cor + j
                if x_cor < len(vis) and y_cor < len(vis) and x_cor >= 0 and y_cor >= 0 and vis[x_cor][y_cor] == 0:
                    vis[x_cor][y_cor] = 1
                    dq.append((x_cor, y_cor))
            curr_size -= 1
        dis += 1
    return dis



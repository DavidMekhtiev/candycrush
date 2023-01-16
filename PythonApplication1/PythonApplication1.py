def candyCrush(N,M,k):
    changed = True
    while changed:
        changed = False
        for i in range(N):
            for j in range(N - 2):
                if M[i][j] == M[i][j + 1] == M[i][j + 2] != 0:
                    M[i][j] = M[i][j + 1] = M[i][j + 2] = -M[i][j]
                    changed = True
        for i in range(N - 2):
            for j in range(N):
                if M[i][j] == M[i + 1][j] == M[i + 2][j] != 0:
                    M[i][j] = M[i + 1][j] = M[i + 2][j] = -M[i][j]
                    changed = True
        for i in range(N):
            c = N - 1
            for j in reversed(range(N)):
                if M[j][i] > 0:
                    M[c][i] = M[j][i]
                    c -= 1
            for j in reversed(range(c + 1)):
                M[j][i] = 0

    return M


if __name__ == "__main__":
    N = 6
    M = [[1, 2, 3, 4, 5, 1],
         [5, 1, 1, 2, 1, 3],
         [3, 2, 4, 3, 4, 2],
         [2, 4, 4, 1, 4, 2],
         [1, 3, 1, 1, 1, 4],
         [2, 2, 4, 5, 2, 2]]
    k = 3

    print(candyCrush(N, M, k))
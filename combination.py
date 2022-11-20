def comb(L):
    for p in range(3):
        for q in range(3):
            for r in range(3):
                if (p!=q and q!=r and p!=r):
                    print(L[p], L[q], L[r])
comb([10, 13, 15])



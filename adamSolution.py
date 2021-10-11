#Please code your solution within this function
def solution():
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
    triangles = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
    alan = 0
    brian = 16
    colin = 48
    solutions = []
    while colin <= 100:
        brian = 16
        while brian <= 84:
            alan = 0
            while alan <= 68:
                if colin in fibonacci and brian in squares and alan in triangles:
                    if colin > brian and brian > alan and (alan + 16) <= brian and (brian + 32) <= colin:

                        print(str(colin) + " " + str(brian) + " " + str(alan))
                        solutions.append([colin, brian, alan])

                if colin in fibonacci and brian in triangles and alan in squares:
                    if colin > brian and brian > alan and (
                            alan + 16) <= brian and (brian + 32) <= colin:

                        print(str(colin) + " " + str(brian) + " " + str(alan))
                        solutions.append([colin, brian, alan])
                if colin in squares and brian in fibonacci and alan in triangles:
                    if colin > brian and brian > alan and (
                            alan + 16) <= brian and (brian + 32) <= colin:
                        print(str(colin) + " " + str(brian) + " " + str(alan))
                        solutions.append([colin, brian, alan])
                if colin in squares and brian in triangles and alan in fibonacci:
                    if colin > brian and brian > alan and (
                            alan + 16) <= brian and (brian + 32) <= colin:
                        print(str(colin) + " " + str(brian) + " " + str(alan))
                        solutions.append([colin, brian, alan])
                if colin in triangles and brian in fibonacci and alan in squares:
                    if colin > brian and brian > alan and (
                            alan + 16) <= brian and (brian + 32) <= colin:
                        print(str(colin) + " " + str(brian) + " " + str(alan))
                        solutions.append([colin, brian, alan])
                if colin in triangles and brian in squares and alan in fibonacci:
                    if colin > brian and brian > alan and (
                            alan + 16) <= brian and (brian + 32) <= colin:
                        print(str(colin) + " " + str(brian) + " " + str(alan))
                        solutions.append([colin, brian, alan])
                alan += 1
            brian += 1
        colin += 1
    print(solutions)
    for sol in solutions:
        for solcheck in solutions:
            if sol[0] == solcheck[0] - 9 and sol[1] == solcheck[1] - 9 and sol[
                    2] == solcheck[2] - 9:
                print("\n--" + str(sol))
                print("  " + str(solcheck))
                print("")

## File contains code for finite projective geometry of order 2
## PG(2,2). This is also known as the Fano Plane. Wanted
## to find the collineation group for PG(2,2)

## Define the points and lines for the geometry
Points = [0,1,2,3,4,5,6]
Lines = ['012','234','045','036','256','146','135']

def LineTransform(line, collineatoin):

    line = ''.join(sorted(line))
    check = CollinearCheck(line)

    if check == False:
        return "Input not a valid line"

    newLine = ''

    for point in line:
        newPoint = Collineation[int(point)]
        newLine = newLine + str(newPoint)

    newLine = ''.join(sorted(newLine))
    check = CollinearCheck(newLine)

    if check == True:
        return newLine
    else:
        return "Output not a valid line"
## Checks if input line is defined in PG(2,2).
def CollinearCheck(line):

    lines = ['012','234','045','036','256','146','135']

    if line in lines:
        return True
    else:
        return False

    ## Input is a set s with n elements. Return all permutations on the set.
    ## This is the Symmetric group of n elements.

    def SymmetricGroup(s):
        if len(s) == 0:
            return [[]]

        sGroup = [s[0:1] + x for x in SymmetricGroup(s[1:])]

        for i in range(1, len(s)):
            if s[i] == s[0]:
                continue
            s[0], s[i] = s[i], s[0]
            sGroup += [s[0:1] + x for x in SymmetricGroup(s[1:])]

        return sGroup

    ## Takes the symmetric group and for each permutation performs
    ## a line transformation on the defined lines of PG(2,2).
    ## Returns all permutation that are collineations

    def CollineationSet(lines, symmetricGroup):

        C = []
        i = 0
        ## iterating over the size of the Symmetric Group
        while i < len(symmetricGroup):

            ## The number of valid transformed lines by permutation
            j = 0

            ## iterating over the defined lines in PG(2,2)
            for line in lines:

                ## check if given permutation returns valid line
                check = LineTransform(line, symmetricGroup[i])
                j = j + 1

                ## breaks if output is not valid
                if check == "Output not a valid line":
                    break

            ## adds to collineation if all lines are transformed
            if j == 7:
                C.append(symmetricGroup[i])
            i = i + 1
        return C

    ## Repeat composition of collineation until it return to the input.
    ## Collects new collineations until returns the input.
    ## The length of the collected list is the order of the collineation.
    def CyclePerm(Perm1):

        cycle = [Perm1]
        newPerm = CompositionPerm(Perm1, Perm1)

        while newPerm != Perm1:
            cycle.append(newPerm)
            newPerm = CompositionPerm(Perm1, newPerm)

        return cycle

    ## (Perm2 o Perm1)(x) Perm2(Perm1(x))
    def CompositionPerm(Perm1, Perm2):

        composition = []

        for i in Perm1:
            composition.append(Perm2[i])
        return composition

    ## Return the order a Collineation
    def Order(perm):

        cycleSet = CyclePerm(perm)

        return len(cycleSet)

    ## Returns a list of the order of all collineations of PG(2,2)
    def TotalOrder(perm):

        c = []

        for i in perm:
            n = Order(i)

            c.append(n)
        return c

## For a given collineation the position represents the Domain
## the element occupying the position is the image
## example [3,5,1,0,2,4,6] represent,
## f(0) = 3
## f(1) = 5
## f(2) = 1
## f(3) = 0
## f(4) = 2
## f(5) = 4
## f(6) = 6





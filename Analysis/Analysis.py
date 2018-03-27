

def ProblemAnalysis( SolveStatus ):
    res = {}
    for _ in SolveStatus:
        for __ in _:
            if __ != 'Teamname':
                problemindex = __
                status = _[__][0]
                times = _[__][1]
                if problemindex not in res:
                    res[problemindex] = [ 0 , 0 ]
                res[problemindex][0] += times
                if status == 'correct':
                    res[problemindex][1] += 1
    ListSummary = []
    for _ in res:
        ListSummary.append([_, res[_][0], res[_][1]])
    ListSummary.sort()
    return ListSummary

# to do
def ProblemSolverAnalysis( SolveStatus ):
    pass
    #FastestSolve , 

if __name__ == '__main__':
    pass
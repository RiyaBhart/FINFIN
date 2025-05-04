from ortools.sat.python import cp_model

def n_queens(N):
    model = cp_model.CpModel()

    queens = [model.NewIntVar(0, N - 1, f'queen_{i}') for i in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            model.Add(queens[i] != queens[j])  
            model.AddAbsEquality(queens[i] - queens[j], j - i) 

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = [solver.Value(queens[i]) for i in range(N)]
        print(solution)
    else:
        print("No solution found")

n_queens(4)

from ortools.sat.python import cp_model

def sudoku_solver():
    model = cp_model.CpModel()

    grid = [[model.NewIntVar(1, 4, f'cell_{r}_{c}') for c in range(4)] for r in range(4)]

    for r in range(4):
        model.AddAllDifferent(grid[r])  

    for c in range(4):
        model.AddAllDifferent([grid[r][c] for r in range(4)])  

    for r in range(0, 4, 2):
        for c in range(0, 4, 2):
            model.AddAllDifferent([grid[r + dr][c + dc] for dr in range(2) for dc in range(2)])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for r in range(4):
            print([solver.Value(grid[r][c]) for c in range(4)])
    else:
        print("No solution found")

sudoku_solver()

from ortools.sat.python import cp_model

def map_coloring():
    model = cp_model.CpModel()

    colors = ['Red', 'Green', 'Blue']
    regions = ['A', 'B', 'C', 'D']
    color_vars = {region: model.NewIntVar(0, len(colors) - 1, region) for region in regions}

    adjacencies = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }

    for region, neighbors in adjacencies.items():
        for neighbor in neighbors:
            model.Add(color_vars[region] != color_vars[neighbor])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = {region: colors[solver.Value(color_vars[region])] for region in regions}
        print(solution)
    else:
        print("No solution found")

map_coloring()

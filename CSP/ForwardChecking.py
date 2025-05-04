from ortools.sat.python import cp_model

def forward_checking():
    model = cp_model.CpModel()
    
    domains = {'X':[1,2,3],'Y':[1,2,3],'Z':[1,2,3]}
    variables = {var: model.NewIntVar(min(domains[var]),max(domains[var]),var)for var in domains}
    
    model.Add(variables['X'] != variables['Y'])
    model.Add(variables['Y'] != variables['Z'])
    model.Add(variables['X'] != variables['Z'])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = {var: solver.Value(variables[var]) for var in variables}
        print(solution)
    else:
        print("No solution found")
forward_checking() 
from ortools.sat.python import cp_model

def job_scheduling():
    model = cp_model.CpModel()

    jobs = ['J1', 'J2', 'J3', 'J4']
    machines = ['M1', 'M2']
    
   
    job_vars = {}
    for job in jobs:
        for machine in machines:
            job_vars[(job, machine)] = model.NewBoolVar(f'{job}_{machine}')
    
    for job in jobs:
        model.Add(sum(job_vars[(job, machine)] for machine in machines) == 1)
    
    model.Add(job_vars[('J1', 'M1')] + job_vars[('J1', 'M2')] == 1) 
    model.Add(job_vars[('J2', 'M1')] + job_vars[('J2', 'M2')] == 1)  
    
    model.Add(job_vars[('J1', 'M1')] + job_vars[('J2', 'M1')] <= 1) 
    model.Add(job_vars[('J1', 'M2')] + job_vars[('J2', 'M2')] <= 1)  
    model.Add(job_vars[('J3', 'M1')] <= job_vars[('J4', 'M2')])
    
    model.Add(sum(job_vars[(job, 'M1')] for job in jobs) <= 2)
    
    model.Add(sum(job_vars[(job, 'M2')] for job in jobs) <= 2)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = {}
        for job in jobs:
            for machine in machines:
                if solver.Value(job_vars[(job, machine)]) == 1:
                    solution[job] = machine
        print("Solution:", solution)
    else:
        print("No solution found")

job_scheduling()

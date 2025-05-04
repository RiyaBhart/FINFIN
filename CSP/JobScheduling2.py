from ortools.sat.python import cp_model

def job_scheduling():
    model = cp_model.CpModel()
    
    durations={
        'J1':2, 'J2':3, 'J3':4, 'J4':2
    }
    
    horizon = 10
    starts = {
        job: model.NewIntVar(0, horizon - durations[job], f"{job}_start")
        for job in durations
    }

    model.Add(starts['J1'] + durations['J1'] < starts['J3'])
    
    j2_endsbeforej4 = model.NewBoolVar('j2_before_j4')
    j4_endsbeforej2 = model.NewBoolVar('j4_before_j2')
    
    model.Add(starts['J2'] + durations['J2'] < starts['J4']).OnlyEnforceIf(j2_endsbeforej4)
    model.Add(starts['J4'] + durations['J4'] < starts['J2']).OnlyEnforceIf(j4_endsbeforej2)
    
    model.AddBoolOr([j2_endsbeforej4,j4_endsbeforej2])
    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    if status in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
        print("Feasible Schedule is : ")
        for job in ['J1','J2','J3','J4']:
            start = solver.Value(starts[job])
            end = start +durations[job]
            print(job," ", start," - ",end)
    else:
        print("no feasible solution")
        
job_scheduling()

from ortools.sat.python import cp_model

def timetable_scheduling():
    model = cp_model.CpModel()

    teachers = ['T1', 'T2']
    subjects = ['S1', 'S2', 'S3']
    time_slots = ['9am', '10am', '11am']


    assignments = {}
    for subject in subjects:
        for teacher in teachers:
            for time in time_slots:
                var_name = f'{subject}_{teacher}_{time}'
                assignments[(subject, teacher, time)] = model.NewBoolVar(var_name)


    for subject in subjects:
        model.Add(sum(assignments[(subject, teacher, time)] 
                      for teacher in teachers for time in time_slots) == 1)


    for teacher in teachers:
        for time in time_slots:
            model.Add(sum(assignments[(subject, teacher, time)] 
                          for subject in subjects) <= 1)

    model.Add(sum(assignments[(subject, 'T1', time)] 
                  for subject in subjects for time in time_slots) == 2)
    model.Add(sum(assignments[(subject, 'T2', time)] 
                  for subject in subjects for time in time_slots) == 1)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = {}
        for (subject, teacher, time), var in assignments.items():
            if solver.Value(var) == 1:
                solution[subject] = (teacher, time)
        print("Solution:", solution)
    else:
        print("No solution found")

timetable_scheduling()

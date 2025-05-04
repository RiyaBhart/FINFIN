from ortools.sat.python import cp_model

products = [
    {"id": 0, "frequency": 15, "volume": 2},
    {"id": 1, "frequency": 8, "volume": 1},
    {"id": 2, "frequency": 20, "volume": 3}
]

slots = [
    {"id": 0, "distance": 1},
    {"id": 1, "distance": 2},
    {"id": 2, "distance": 3}
]

model = cp_model.CpModel()
numproducts = len(products)
numslots = len(slots)

assignments = [model.NewIntVar(0,numslots-1,f'assign_p{i}') for i in range(numproducts)]

model.AddAllDifferent(assignments)

total_cost = model.NewIntVar(0,1000,'total_cost')

cost_terms = []

for i in range(numproducts):
    for j in range(numslots):
        is_assigned = model.NewBoolVar(f'prod{i}_slot{j}')
        model.Add(assignments[i]==j).OnlyEnforceIf(is_assigned)
        model.Add(assignments[i]!=j).OnlyEnforceIf(is_assigned.Not())
        
        cost = products[i]['frequency'] * slots[j]['distance']
        cost_terms.append(is_assigned * cost)
model.Add(total_cost == sum(cost_terms))
model.Minimize(total_cost)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"Total Cost = {solver.Value(total_cost)}")
    for i in range(numproducts):
        assigned_slot = solver.Value(assignments[i])
        print(f"Product {i + 1} assigned to Slot {assigned_slot + 1} (Distance = {slots[assigned_slot]['distance']})")
else:
    print("No solution found.")
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define model structure
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Define CPDs
cpd_intelligence = TabularCPD('Intelligence', 2, [[0.7], [0.3]], state_names={'Intelligence': ['High', 'Low']})
cpd_studyhours = TabularCPD('StudyHours', 2, [[0.6], [0.4]], state_names={'StudyHours': ['Sufficient', 'Insufficient']})
cpd_difficulty = TabularCPD('Difficulty', 2, [[0.4], [0.6]], state_names={'Difficulty': ['Hard', 'Easy']})

# Grade has 3 outcomes: A, B, C → index: 0=A, 1=B, 2=C
cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        # A
        [0.8, 0.6, 0.4, 0.7, 0.3, 0.2, 0.2, 0.1],
        # B
        [0.15, 0.3, 0.4, 0.2, 0.4, 0.3, 0.3, 0.2],
        # C
        [0.05, 0.1, 0.2, 0.1, 0.3, 0.5, 0.5, 0.7],
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={
        'Grade': ['A', 'B', 'C'],
        'Intelligence': ['High', 'Low'],
        'StudyHours': ['Sufficient', 'Insufficient'],
        'Difficulty': ['Hard', 'Easy']
    }
)

cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95, 0.80, 0.50],  # Pass = Yes
        [0.05, 0.20, 0.50]   # Pass = No
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={
        'Pass': ['Yes', 'No'],
        'Grade': ['A', 'B', 'C']
    }
)

# Add CPDs
model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)

# Validate model
assert model.check_model()

# Inference
inference = VariableElimination(model)

# Query 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)
result1 = inference.query(
    variables=['Pass'],
    evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)
print("P(Pass | StudyHours=Sufficient, Difficulty=Hard):")
print(result1)

# Query 2: P(Intelligence | Pass=Yes)
result2 = inference.query(
    variables=['Intelligence'],
    evidence={'Pass': 'Yes'}
)
print("\nP(Intelligence | Pass=Yes):")
print(result2)

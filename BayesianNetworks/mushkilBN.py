from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Intelligence','Grade'),('Difficulty','Grade'),('Grade','Letter'),('Intelligence','SAT')])

cpd_intelligence = TabularCPD(variable='Intelligence',variable_card=2,values=[[0.7],[0.3]],state_names={'Intelligence':['High','Low']})

cpd_difficulty = TabularCPD(variable = 'Difficulty',variable_card=2,values =[[0.6],[0.4]],state_names={'Difficulty':['Easy','Hard']})

cpd_grade = TabularCPD(variable = 'Grade',variable_card=3,values=[[0.3,0.5,0.1,0.2],[0.4,0.3,0.3,0.4],[0.3,0.2,0.6,0.4]],evidence=['Intelligence','Difficulty'],evidence_card=[2,2], state_names={'Grade':['A','B','C'],'Intelligence':['High','Low'],'Difficulty':['Easy','Hard']})

cpd_letter = TabularCPD(variable='Letter',variable_card=2,values=[[0.9,0.6,0.3],[0.1,0.4,0.7]],evidence=['Grade'],evidence_card=[3],state_names={'Letter':['Strong','Weak'],'Grade':['A','B','C']})

cpd_sat = TabularCPD(variable = 'SAT',variable_card=2,values=[[0.95,0.2],[0.05,0.8]],evidence=['Intelligence'],evidence_card=[2],state_names={'SAT':['High','Low'],'Intelligence':['High','Low']})

model.add_cpds(cpd_intelligence,cpd_difficulty,cpd_grade,cpd_letter,cpd_sat)

assert model.check_model()

infer = VariableElimination(model)

query_result = infer.query(variables=['Letter'],evidence={'SAT':'High'})
print(query_result)

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Spam','ContainsFree'),('Spam','ContainsWinner'),('Spam','ContainsLink'),('SenderReputation','Spam')])

cpd_senderreputation =TabularCPD(variable='SenderReputation',variable_card=2,values=[[0.85],[0.15]],state_names={'SenderReputation':['Good','Bad']})

cpd_spam = TabularCPD(variable='Spam',variable_card=2,values=[[0.2,0.9],[0.8,0.1]],evidence=['SenderReputation'],evidence_card=[2],state_names={'Spam':['Yes','No'],'SenderReputation':['Good','Bad']})

cpd_containsfree = TabularCPD(variable='ContainsFree',variable_card=2,values=[[0.7,0.1],[0.3,0.9]],evidence=['Spam'],evidence_card=[2],state_names={'Spam':['Yes','No'],'ContainsFree':['Yes','No']})

cpd_containswinner = TabularCPD(variable='ContainsWinner',variable_card=2,values=[[0.6,0.05],[0.4,0.95]],evidence=['Spam'],evidence_card=[2],state_names={'Spam':['Yes','No'],'ContainsWinner':['Yes','No']})

cpd_containslink = TabularCPD(variable='ContainsLink',variable_card=2,values=[[0.8,0.3],[0.2,0.7]],evidence=['Spam'],evidence_card=[2],state_names={'Spam':['Yes','No'],'ContainsLink':['Yes','No']})

model.add_cpds(cpd_senderreputation,cpd_spam,cpd_containsfree,cpd_containslink,cpd_containswinner)

assert model.check_model()

infer = VariableElimination(model)

print("\ntask 1 : P(Spam| ContainsFree=Yes,ContainsLink=Yes , SenderReputation = Yes) ")
task1 = infer.query(variables=['Spam'],evidence={'ContainsFree':'Yes','ContainsLink':'Yes','SenderReputation':'Bad'})
print(task1)

print("\n Task2 : P(Spam=No | containsFree = No, ContainsWinner = no, ContainsLink = no, SenderReputation = Good)")
task2 = infer.query(variables=['Spam'],evidence={'ContainsFree':'No','ContainsLink':'No','SenderReputation':'Good'})
print(task2)

model.add_edge('Spam','ContainsUrgent')
cpd_urgent = TabularCPD(variable='ContainsUrgent', variable_card=2,
                        values=[[0.5, 0.9],  # P(Yes | Spam=Yes), P(Yes | Spam=No)
                                [0.5, 0.1]],
                        evidence=['Spam'], evidence_card=[2],state_names={'ContainsUrgent':['Yes','No'],'Spam':['Yes','No']})

model.add_cpds(cpd_urgent)

model.check_model()

infer_updated = VariableElimination(model)

print("\nTask3: P(Spam | ContainsUrgent = Yes)")
task3 = infer_updated.query(variable=['Spam'],evidence={'ContainsUrgent':'Yes'})
print(task3)
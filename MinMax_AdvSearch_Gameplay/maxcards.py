class Agent:
    def __init__(self,name,strategy):
        self.name =name
        self.strategy = strategy
        self.score =0
        
    def pick(self,cards):
        return self.strategy(cards)
    

def max_strategy(cards):
    if cards[0]>=cards[-1]:
        return cards.pop(0)
    else:
        return cards.pop(-1)

def min_strategy(cards):
    if cards[0]<=cards[-1]:
        return cards.pop(0)
    else:
        return cards.pop(-1)
    
def run_agent(cards):
    max_agent = Agent("max",max_strategy)
    min_agent = Agent("min",min_strategy)
    
    agents = [max_agent,min_agent]
    turn = 0
    print("initial cards ",cards)
    while (cards):
        agent = agents[turn%2]
        pick = agent.pick(cards)
        agent.score +=pick
        print(f"{agent.name} picks {pick}, remaining cards: {cards}")
        turn+=1
        
    print("finals scores : max = ",max_agent.score," min = ",min_agent.score)
    if max_agent.score> min_agent.score:
        print("winner : max agent")
    if max_agent.score<min_agent.score:
        print("winner : min agent")
    else:
        print("draw")
        
cards = [4, 10, 6, 2, 9, 5] 
run_agent(cards)
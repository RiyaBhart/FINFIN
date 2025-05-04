import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None

class MinmaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "goal reached" if node.minmax_value is not None else "searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == 'goal reached':
            return f"minmax value for root node : {node.minmax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):
        self.computed_nodes.append(node.value)

        if depth == 0 or not node.children:
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.alpha_beta_search(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    print("Pruned node:", child.value)
                    break
            node.minmax_value = value
            return value
        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.alpha_beta_search(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    print("Pruned node:", child.value)
                    break
            node.minmax_value = value
            return value

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)

# Build the tree
root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

# Define depth and run agent
depth = 3
agent = MinmaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)

# Output results
print("\nComputed Nodes:", environment.computed_nodes)
print("Minimax values:")
print(f"A: {root.minmax_value}")
print(f"B: {n1.minmax_value}")
print(f"C: {n2.minmax_value}")
print(f"D: {n3.minmax_value}")
print(f"E: {n4.minmax_value}")
print(f"F: {n5.minmax_value}")
print(f"G: {n6.minmax_value}")

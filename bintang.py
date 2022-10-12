from collections import  deque

class PriorityQueue:
   def __init__(self):
       self.fn={}
       self.nodes={}
   def append(self,node):
        problem=Problem('Arad','Bucharest')
        if node.state not in self.fn.keys():
           self.fn[node.state]=int(problem.h(node.state))+node.path_cost
           self.nodes[node.state]=node
          
   def pop(self):
       # Find state with minmum f-value  
       state= min(self.fn, key=self.fn.get)
       del self.fn[state]
       node=self.nodes[state]
       del self.nodes[state]
       return node
      
   def replace(self,child):
       problem=Problem('Arad','Bucharest')
       if self.contains(child) and self.fn[child.state]>int(problem.h(child.state))+child.path_cost:
          self.fn[child.state]=int(problem.h(child.state))+child.path_cost
          self.nodes[child.state]=child

   def IsEmpty(self):
       return not self.fn

   def Clear(self):
       self.fn={}
       self.nodes={}
      
   def contains(self,node):
       return node.state in self.fn.keys()

   def __str__(self):
        str1 = ' '.join(str(e) for e in self.fn.keys())
        return  str1
# ______________________________________________________________________________

class Problem(object):
    def __init__(self, init_state, goal_state):
        self.initial_state = init_state;
        self.goal_state = goal_state;
        self.state_space = {};
        self.state_space['Arad'] = {'GoZerind': 'Zerind', 'GoSibiu' : 'Sibiu', 'GoTimisoara': 'Timisoara'};
        self.state_space['Zerind'] = {'GoOradea': 'Oradea', 'GoArad' : 'Arad' };
        self.state_space['Oradea'] = {'GoSibiu': 'Sibiu', 'GoZerind': 'Zerind'};
        self.state_space['Timisoara'] = {'GoLugoj' : 'Lugoj', 'GoArad' : 'Arad'};
        self.state_space['Lugoj'] = {'GoTimisoara' : 'Timisoara', 'GoMehandia' : 'Mehandia'};
        self.state_space['Drobeta'] = {'GoMehandia' : 'Mehandia', 'GoCraiova' : 'Craiova'};
        self.state_space['Craiova'] = {'GoDrobeta' : 'Drobeta', 'GoRimnicu' : 'Rimnicu Vilcea', 'GoPitesti' : 'Pitesti'};
        self.state_space['Rimnicu Vilcea'] = {'GoSibiu' : 'Sibiu', 'GoPitesti' : 'Pitesti', 'GoCraoova' : 'Craiova'};
        self.state_space['Sibiu'] = {'GoArad' : 'Arad', 'GoFagaras' : 'Fagaras', 'GoOradea' : 'Oradea', 'GoRimnicu' : 

'Rimnicu Vilcea'};
        self.state_space['Fagaras'] = {'GoSibiu' : 'Sibiu', 'GoBucharest' : 'Bucharest'};
        self.state_space['Pitesti'] = {'GoRimnicu' : 'Rimnicu Vilcea', 'GoCraiova' : 'Craiova', 'GoBucharest' : 

'Bucharest'};
        self.state_space['Bucharest'] = {'GoFagaras' : 'Fagaras', 'GoPitesti' : 'Pitesti', 'GoGiurgiu' : 'Giurgiu', 

'GoUrziceni' : 'Urziceni'};
        self.state_space['Giurgiu'] = {'GoBucharest' : 'Bucharest'};
        self.state_space['Urziceni'] = {'GoBucharest' : 'Bucharest', 'GoValsui' : 'Valsui', 'GoHirsova' : 'Hirsova'};
        self.state_space['Hirsova'] = {'GoEforie' : 'Eforie', 'GoUrziceni' : 'Urziceni'};
        self.state_space['Eforie'] = {'GoHirsova' : 'Hirsova'};
        self.state_space['Valsui'] = {'GoUrziceni' : 'Urziceni', 'GoIasi' : 'Iasi'};
        self.state_space['Iasi'] = {'GoValsui' : 'Valsui', 'GoNeamt' : 'Neamt'};
        self.state_space['Neamt'] = {'GoIasi' : 'Iasi'};
        self.state_space['Mehandia'] = {'GoLugoj' : 'Lugoj','GoDrobeta' : 'Drobeta'};

        self.step_cost = {};
        self.step_cost['Arad'] = {'GoZerind': '75', 'GoSibiu': '140', 'GoTimisoara': '118'};
        self.step_cost['Zerind'] = {'GoOradea': '71', 'GoArad': '75'};
        self.step_cost['Oradea'] = {'GoSibiu': '152', 'GoZerind': '71'};
        self.step_cost['Timisoara'] = {'GoLugoj': '111', 'GoArad': '118'};
        self.step_cost['Lugoj'] = {'GoTimisoara': '111', 'GoMehandia': '70'};
        self.step_cost['Drobeta'] = {'GoMehandia': '75', 'GoCraiova': '120'};
        self.step_cost['Craiova'] = {'GoDrobeta': '120', 'GoRimnicu': '146', 'GoPitesti': '138'};
        self.step_cost['Rimnicu Vilcea'] = {'GoSibiu': '80', 'GoPitesti': '97', 'GoCraoova': '146'};
        self.step_cost['Sibiu'] = {'GoArad': '140', 'GoFagaras': '99', 'GoOradea': '151','GoRimnicu': '80'};
        self.step_cost['Mehandia'] = {'GoLugoj' : '70','GoDrobeta' : '75'};

        self.step_cost['Fagaras'] = {'GoSibiu': '99', 'GoBucharest': '211'};
        self.step_cost['Pitesti'] = {'GoRimnicu': '97', 'GoCraiova': '138', 'GoBucharest': '101'};
        self.step_cost['Bucharest'] = {'GoFagaras': '211', 'GoPitesti': '101', 'GoGiurgiu': '90', 'GoUrziceni': '85'};
        self.step_cost['Giurgiu'] = {'GoBucharest': '90'};
        self.step_cost['Urziceni'] = {'GoBucharest': '85', 'GoValsui': '142', 'GoHirsova': '98'};
        self.step_cost['Hirsova'] = {'GoEforie': '86', 'GoUrziceni': '98'};
        self.step_cost['Eforie'] = {'GoHirsova': '86'};
        self.step_cost['Valsui'] = {'GoUrziceni': '142', 'GoIasi': '92'};
        self.step_cost['Iasi'] = {'GoValsui': '92', 'GoNeamt': '87'};
        self.step_cost['Neamt'] = {'GoIasi': '87'};
        
        self.heuristics = {};
        self.heuristics['Arad'] = 366;
        self.heuristics['Zerind'] = 374;
        self.heuristics['Oradea'] =380;
        self.heuristics['Timisoara'] = 329;
        self.heuristics['Lugoj'] = 244;
        self.heuristics['Drobeta'] = 242;
        self.heuristics['Craiova'] = 160;
        self.heuristics['Rimnicu Vilcea'] = 193;
        self.heuristics['Sibiu'] = 253;
        self.heuristics['Fagaras'] = 176;
        self.heuristics['Pitesti'] = 100;
        self.heuristics['Bucharest'] = 0;
        self.heuristics['Giurgiu'] = 77;
        self.heuristics['Urziceni'] = 80;
        self.heuristics['Hirsova'] = 151;
        self.heuristics['Eforie'] = 161;
        self.heuristics['Valsui'] = 199;
        self.heuristics['Iasi'] = 226;
        self.heuristics['Neamt'] = 234;
        self.heuristics['Mehandia'] = 241;

    def Actions(self, state):
        lst=self.state_space[state].keys()
        return lst
        
    def Result(self, state, action):
        return self.state_space[state][action]

    def Goal_test(self, state):
        return state == self.goal_state

    def Path_cost(self, state, action):
        return self.step_cost[state][action]

    def h(self, state):
        return self.heuristics[state]

# ______________________________________________________________________________


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
       
        
    def __repr__(self):
        return "<Node {} {} >".format(self.state,self.path_cost)

    def __lt__(self, node):
        return self.state < node.state    
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state
#-----------------------------------------------------------------------------
def child_node(problem,parent, action):
        next_state = problem.Result(parent.state, action)
        
        step_cost= problem.Path_cost(parent.state, action)
        next_node = Node(next_state, parent,action, parent.path_cost+int(step_cost))
        return next_node
    
def solution(node):
        path_back =[]
        while node:
            path_back.append(node)
            node = node.parent
        for n in reversed(path_back): 
            print (n)

# ______________________________________________________________________________

def Astar(problem):
    
    node=Node(problem.initial_state)
    frontier = PriorityQueue()
    frontier.append(node)
    explored=[]
    while True:
      if frontier.IsEmpty(): return print('Failure')
      node=frontier.pop()
      #print(node) uncomment to understand working of algorithm
      if problem.Goal_test(node.state): return solution(node)
      explored.append(node.state)
      for action in problem.Actions(node.state):
          child=child_node(problem,node,action)
          if child.state not in explored and not frontier.contains(child):
             frontier.append(child)
          elif frontier.contains(child):
             frontier.replace(child)

# ____________________________________________________________________________
# Program main part
problem=Problem('Arad','Bucharest')
Astar(problem)

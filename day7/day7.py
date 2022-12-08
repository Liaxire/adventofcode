file = open("day7_input.txt")
lines = file.readlines()

class Tree:
    def __init__(self, name):
        self.children = []
        self.size = 0
        self.name = name


def execute_cd(command, current_node, last_nodes):
  if command[1] == "cd":
    if command[2] == "..":
      current_node = last_nodes.pop()
    else:
      last_nodes.append(current_node)
      for i in current_node.children:
        if i.name == command[2]:
          current_node = i
  return current_node  
          

def add_dir(command, current_node):
  for i in current_node.children:
    if command[1] == i.name:
      return
  current_node.children.append(Tree(command[1]))
  return current_node
def parseLine(line, current_node, last_nodes):
  words = line.split()
  if words[0] == "$":
    current_node = execute_cd(words, current_node, last_nodes)
  elif words[0] == "dir":
    current_node = add_dir(words, current_node)
  else:
    current_node.size += int(words[0])
  return current_node

def dfs(node):
  global sum
  for i in node.children:
    dfs(i)
    node.size += i.size
  if node.size <= 100000:
    sum += node.size

sum = 0
last_nodes = []
current_node = Tree("/")
original_node = current_node
for line in lines:
  current_node = parseLine(line, current_node, last_nodes)
dfs(original_node)



lowest = original_node.size - 40000000
current_lowest = None
def dfs2(node, lowest):
  global current_lowest
  for i in node.children:
    # print(i.size)
    if i.size >= lowest and (current_lowest == None or i.size < current_lowest):
      current_lowest = i.size
    dfs2(i, lowest)

print(lowest)
dfs2(original_node,  lowest)
print(current_lowest)

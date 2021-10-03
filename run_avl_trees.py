''' run the avl_tree_complete '''
from avl_tree_complete import Node

root = Node(10)
add = [8, 3, 1, 10, 5, 14, 9, 20, 13, 19]

for i in add:
    root.insert(i)
#delete 
#root.delete(8)
#show_tree
#print_tree
#print(max(add))
#print(min(add))
#root.print_tree()
#root.count_levels()
root.show_tree()

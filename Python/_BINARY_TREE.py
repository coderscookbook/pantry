# from @rob_loves_coding92
# PYTHON BINARY TREE

import matplotlib.pyplot as plt

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left  = None
    self.right = None

def plot_binary_tree(root):
  fig, ax = plt.subplots()
  ax.set_axis_off()
  
  def plot_node(node, x, y, dx):
    if node is None:
      return
    
    ax.annotate(str(node.value),
                (x,y), ha='center',
                va = 'center',
                bbox=dict(facecolor='white',
                edgecolor='black', boxstyle='circle'))
    
    if node.left is not None:
      ax.plot([x, x- dx], [y, y -1, dx /2])
      plot_node(node.left, x -dx, y - 1, dx / 2)
      
    if node.right is not None:
      ax.plot([x, x + dx], [y, y - 1, dx / 2 ])
      plot_node(node.right, x + dx, y - 1, dx / 2)
      
    plot_node(root, 0, 0, 1)
    plt.show()
    
# Create binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Plot binary tree
plot_binary_tree(root)
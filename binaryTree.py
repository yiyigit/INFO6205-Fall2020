
#1. Link List in Binary Tree :
class Solution:
def isSame(self, head, root):
    if not head:return True
    if not root:return False
    if head.val != root.val:
        return False
    return self.isSame(head.next, root.left) or self.isSame(head.next,root.right)

def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
    if not head:return True
    if not root:return False
    if self.isSame(head,root):return True
    return self.isSubPath(head, root.left) or self.isSubPath(head,root.right)

#2. Binary Tree Tilt:
class Solution:
def findTilt(self, root: TreeNode) -> int:
    def dfs(node):
        if not node:
            return 0
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        self.tilt += abs(left_sum-right_sum)
        sum = left_sum + right_sum +node.val
        return sum
    self.tilt = 0
    dfs(root)
    return self.tilt

#3. Merge Two Binary Trees:
class Solution:
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2:return None
    if not t1:return t2
    if not t2:return t1
    root = TreeNode(t1.val+t2.val)
    root.left = self.mergeTrees(t1.left,t2.left)
    root.right = self.mergeTrees(t1.right, t2.right)
    return root
#4. Construct a Binary tree from Inorder and Preorder traversal
class Solution:
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:return None
    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:index+1],inorder[:index])
    root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
    return root
    
#5. Tree Diameter
class Solution:

def treeDiameter(self, edges: List[List[int]]) -> int:
    graph = [set() for i in range(len(edges)+1)]
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)

    diameter = 0

    def dfs(curr, visited):

        nonlocal diameter

        d1, d2 = 0, 0
        distance = 0
        visited[curr] = True

        for neighbor in graph[curr]:
            if not visited[neighbor]:
                distance = 1 + dfs(neighbor, visited)

            if distance > top_1_distance:
                top_1_distance, top_2_distance = distance, top_1_distance
            elif distance > top_2_distance:
                top_2_distance = distance

    diameter = max(diameter, d1 + d2)

    return d1

    visited = [False for i in range(len(graph))]
    dfs(0, visited)

    return diameter

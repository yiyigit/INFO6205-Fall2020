#Q1
#Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
#Note:
#
#The length of both num1 and num2 is < 5100.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]

#/*Q2
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
#Example:
#
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4


class Solution:
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    return dummy.next

#/*Q3
#Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and
#removing them causing the left and the right side of the deleted substring to concatenate together.
#
#We repeatedly make k duplicate removals on s until we no longer can.
#
#Return the final string after all such duplicate removals have been made.
#
#It is guaranteed that the answer is unique.
#
#Example:
#Input: s = "abcd", k = 2
#Output: "abcd"
#Explanation: There's nothing to delete.
#
#Input: s = "deeedbbcccbdaa", k = 3
#Output: "aa"
#Explanation:
#First delete "eee" and "ccc", get "ddbbbdaa"
#Then delete "bbb", get "dddaa"
#Finally delete "ddd", get "aa"
#*/
class Solution:
def removeDuplicates(self, s: str, k: int) -> str:
    def detectDupilcates(string,k):
        detected = False
        new_string = ''
        i = 0
        while i< len(string)-k+1:
            if string[i:i+k] == string[i]*k:
                detected = True
                i+=k
            else:
                new_string += string[i]
                i+=1
        new_string += string[i:]
        if detected:
            return (True,new_string)
        return (False,string)
    
    if_remove,res = detectDupilcates(s,k)
    if not if_remove:return res
    return self.removeDuplicates(res,k)
        

#/*Q4
#Given a 2D board and a word, find if the word exists in the grid.
#
#The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#Example:
#
#board =
#[
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
#
#Given word = "ABCCED", return true.
#Given word = "SEE", return true.
#Given word = "ABCB", return false.
#*/

class Solution:
def exist(self, board: List[List[str]], word: str) -> bool:
    m,n = len(board),len(board[0])
    
    def dfs(i,j,visited,index):
        if index == len(word):
            return True
        if i not in range(m) or j not in range(n) or (i,j) in visited:
            return False
        
        if word[index] != board[i][j]:
            return False
        visited.add((i,j))
        result = dfs(i+1,j,visited,index+1) or dfs(i,j+1,visited,index+1) or dfs(i-1,j,visited,index+1) or dfs(i,j-1,visited,index+1)
        visited.remove((i,j))
        return result
        
    for i in range(m):
        for j in range(n):
            visited = set()
            if dfs(i,j,visited,0):
                return True
    return False
#/*Q5
#Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
#Example 1:
#Given tree s:
#
#     3
#    / \
#   4   5
#  / \
# 1   2
#Given tree t:
#   4
#  / \
# 1   2
#Return true, because t has the same structure and node values with a subtree of s.
#Example 2:
#Given tree s:
#
#     3
#    / \
#   4   5
#  / \
# 1   2
#    /
#   0
#Given tree t:
#   4
#  / \
# 1   2
#Return false.
#*/
class Solution:
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if not s:return False
    if self.isSame(s,t):return True
    return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    
def isSame(self,s,t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val == t.val:
        return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
    return False



#/*Q6
#Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
#Example 1:
#
#Input:
#    5
#   / \
#  3   6
# / \   \
#2   4   7
#
#Target = 9
#
#Output: True
#
#
#Example 2:
#
#Input:
#    5
#   / \
#  3   6
# / \   \
#2   4   7
#
#Target = 28
#
#Output: False
#*/
class Solution(object):
def findTarget(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    if not root:
        return False

    return self._findTarget(root, set(), k)

def _findTarget(self, node, nodes, k):
    if not node:
        return False

    complement = k - node.val
    if complement in nodes:
        return True

    nodes.add(node.val)

    return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)
#/*Q7
#Given an encoded string, return its decoded string.
#
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
#Note that k is guaranteed to be a positive integer.
#
#You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
#Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,k.
#For example, there won't be input like 3a or 2[4].
#
#Example:
#s = "3[a]2[bc]", return "aaabcbc".
#s = "3[a2[c]]", return "accaccacc".
#s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
#*/
class Solution(object):
def decodeString(self, s):
    stack = []; curNum = 0; curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curString += c
    return curString

#/*Q8
#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#Example 1:
#
#Input:
#11110
#11010
#11000
#00000
#
#Output: 1
#Example 2:
#
#Input:
#11000
#11000
#00100
#00011
#
#Output: 3
#*/

class Solution:
def numIslands(self, grid: List[List[str]]) -> int:
    m,n = len(grid),len(grid[0])
    res =0
    def dfs(i,j):
        if i not in range(m) or j not in range(n):
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        return
        
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i,j)
                res +=1
    return res
    
#/*Q9
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
#Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#
#
#Example 1:
#
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take.
#             To take course 1 you should have finished course 0. So it is possible.
#Example 2:
#
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take.
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.
#
#
#Constraints:
#
#The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#You may assume that there are no duplicate edges in the input prerequisites.
#1 <= numCourses <= 10^5
#*/

class Solution:
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    indegree = {}
    condition = {}
    for after,pre in prerequisites:
        indegree[after] = indegree.get(after,0) +1
        condition[pre] = condition.get(pre,[]) + [after]
    
    que = []
    for num in range(numCourses):
        if num not in indegree:
            que.append(num)
    while que:
        course = que.pop(0)
        numCourses -=1
        if course not in condition:
            continue
        for after in condition[course]:
            indegree[after] -=1
            if indegree[after] ==0:
                que.append(after)
                del indegree[after]
    return numCourses==0
            
#/*Q10
#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
#Example 1:
#
#Input: [[0, 30],[5, 10],[15, 20]]
#Output: 2
#Example 2:
#
#Input: [[7,10],[2,4]]
#Output: 1
#*/

import heapq
class Solution:
def rooms(self, array):
    array.sort(key=lambda x:x[0])
    que = []
    num = 0
    for start,end in array:
        if not que:
            num +=1
            heapq.heappush(que,end)
        else:
            time = heapq.heappop(que)
            if time > start:
                num +=1
                heapq.heappush(que,time)
                heapq.heappush(que,end)
            else:
                heapq.heappush(que,end)
    return num
                

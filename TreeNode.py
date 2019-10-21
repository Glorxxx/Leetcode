# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class OperationTree:
    def create(self,List):
        root = TreeNode(List[0])
        lens=len(List)
        if lens>=2:
            root.left=self.create(List[1])
        if lens >=3:
            root.right=self.create(List[2])
        return root
class Solution:
    def rangeSumBST(self, root, L: int, R: int) -> int:
        ans=0
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                if L<= node.val<=R:
                    ans=ans+node.val
                if L<node.val:
                    stack.append(node.left)
                if node.val<R:
                    stack.append(node.right)
        return ans

x=1
y=4
List1=[1,[2,[4,[8],[9]],[5]],[3,[6],[7]]]
op=OperationTree()
tree1=op.create(List1)
root=[10,5,15,3,7,18]
sol = Solution()
c=sol.rangeSumBST(tree1,4,9)

print(c)


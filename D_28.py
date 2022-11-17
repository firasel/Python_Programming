class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBt(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0 or preorder[0] not in inorder:
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        preorder.pop(0)
        root.left = self.createBt(preorder, inorder[0:pos])
        root.right = self.createBt(preorder, inorder[pos+1:])
        return root

    def buildTree(self, preorder, inorder):
        root = self.createBt(preorder, inorder)
        return root


st = Solution()
print(st.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))

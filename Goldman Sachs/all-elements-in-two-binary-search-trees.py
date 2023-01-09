class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        st1,st2,res=[],[],[]
        while root1 or root2 or len(st1) or len(st2):
            while root1:
                st1.append(root1)
                root1=root1.left
            while root2:
                st2.append(root2)
                root2=root2.left
            if not len(st2) or (len(st1) and st1[-1].val<=st2[-1].val):
                root1=st1.pop()
                res.append(root1.val)
                root1=root1.right
            else:
                root2=st2.pop()
                res.append(root2.val)
                root2=root2.right
        return res
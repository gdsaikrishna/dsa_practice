'''
Link: https://leetcode.com/problems/binary-tree-postorder-traversal
'''

class RecursiveSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        def postorder(root):
            return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return postorder(root)
    
class IterativeSolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:  
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
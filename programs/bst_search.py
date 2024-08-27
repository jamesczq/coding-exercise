"""
Check if a given value is present in a BST.

Created on Sat Jun 25 2022
"""


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def search_bst(tree: BSTNode, key: int):
    return (
        tree
        if not tree or tree.data == key
        else (
            search_bst(tree.left, key)
            if key < tree.data
            else search_bst(tree.right, key)
        )
    )


def main():
    """         
    Test BST:
                         A[19]           
                   /              \
                /                     \
              B(7)                    I(43)
            /      \                 /     \
         C(3)       F(11)       J(23)       O(47)
         /  \           \           \           \
      D(2)   E(5)       G(17)        K(37)       P(53)
                        /            /    \
                    H(13)        L(29)     N(41)
                                     \
                                      M(31)
    
    """
    # Left-substree(root A)
    D, E = BSTNode(2), BSTNode(5)
    C = BSTNode(3, left=D, right=E)

    H = BSTNode(13)
    G = BSTNode(17, left=H)
    F = BSTNode(11, right=G)

    B = BSTNode(7, left=C, right=F)

    # Right-subtree(root A)
    M = BSTNode(31)
    L = BSTNode(29, right=M)

    N = BSTNode(41)

    K = BSTNode(37, left=L, right=N)

    J = BSTNode(23, right=K)

    P = BSTNode(53)
    O = BSTNode(47, right=P)

    I = BSTNode(43, left=J, right=O)

    # Root A
    A = BSTNode(19, left=B, right=I)

    k = 178
    a = search_bst(A, k)
    if not a:
        print("Not present")
    else:
        print(f"{k} is in the BST.")


if __name__ == "__main__":
    main()

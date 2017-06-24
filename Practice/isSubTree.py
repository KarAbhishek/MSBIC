def isSubTree(tree, subTree):
    if subTree is None:
        return True
    if tree is None:
        return False

    return isTreeEqual(tree, subTree) or isSubTree(tree.left, subTree) or isSubTree(tree.right, subTree)


def isTreeEqual(tree1, tree2):
    if tree1.val != tree2.val:
        return False
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return isTreeEqual(tree1.left, tree2.left) and isTreeEqual(tree1.left, tree2.left)
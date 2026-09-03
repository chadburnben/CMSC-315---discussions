"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.

Create a Real-World Application:
 Military Department Database
- Use IDs to organize departments to look up personnel more efficiently.
- Show how insertion order can affect the search efficiency.
- Reveal how BST hos advantages in managing hierarchical military structure
"""

class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the different node values such as department ID
        # and initialize left and right child references to None.
        # This allows the structure left and right to have each node point and start
        # up to two children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # The tree will grow as the department nodes are inserted
        # however there has not been any added so far, so the root is None.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Starts the root and smaller IDs go left.
        # The larger IDs however, must go right.
        # This ensures that later searches discard one whole
        # subtree after each comparison.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case found an empty spot, which is where the new
        # department node belongs.
        if node is None:
            return Node(value)

        # Recursive case: the value is smaller, so in this case
        # smaller department IDs go left.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Recursive case: the larger values or department IDs go right
        # and same with the equal values, so the BST property still holds.
        else:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Linear BST is more efficient than linear search for military
        # databases.
        # Linear search is required to check every department.
        # BST will eliminate half the remaining departments by
        # comparing the current node and then only follows one child.
        # This means that a balance tree is about O(log n) instead of
        # O(n), Each comparison will eliminate an entire subtree of departments
        # from consideration.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case: Reaches a missing child, so it reached an empty node and
        # so the department ID was not found in the tree.
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.

        When doing military departments, this produces sorted lost from all
        the department IDs.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Visits left subtree first: those IDs are all smaller.
        self._inorder_recursive(node.left, values)
        # Visits current department ID or node
        values.append(node.value)
        # Visits the right subtree last: those IDs are all larger.
        self._inorder_recursive(node.right, values)

    # This is my Real-World Scenario department structure
MILITARY_DEPARTMENTS = {
    1001: "Army",
    1002: "Navy",
    1003: "Air Force",
    1004: "Marines",
    1005: "Space Force",
    1006: "Coast Guard"
}

def department_name(dept_id):
    return MILITARY_DEPARTMENTS.get(dept_id, "Unknown department")


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Military Department Database")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    bst = BST()

    # Start on the middle ID first so both the left and right
    # subtrees fill. This helps keeps the tree from being a list.
    insertion_order = [1003, 1002, 1005, 1001, 1004, 1006, 1000, 1007]

    print("Department IDs inserted:")
    for dept_id in insertion_order:
        print(f"  {dept_id}: {department_name(dept_id)}")

    # Every insert will compare once and only walk one child.
    # This will cut the remaining search space instead of having
    # to scan each department as a list.
    for dept_id in insertion_order:
        bst.insert(dept_id)
        print(f"  Inserted {dept_id}: {department_name(dept_id)}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # Left, node, right does a visit to smaller IDs first.
    # The result is sorted by department ID.
    traversal_result = bst.inorder()
    print("In-order traversal (sorted IDs):", traversal_result)

    print("Departments in sorted ID order:")
    for dept_id in traversal_result:
        print(f"  {dept_id}: {department_name(dept_id)}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # The two IDs had been inserted, so the search will return True.
    # These two IDs were inserted, so search should return True.
    print("Search 1002 (Navy):", bst.search(1002))
    print("Search 1005 (Space Force):", bst.search(1005))

    # These two IDs weren't inserted, so they will return False.
    print("Search 1008 (not in tree):", bst.search(1008))
    print("Search 9999 (not in tree):", bst.search(9999))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # For the empty tree there is no root so the traversal is []
    # and the search doesn't have anywhere to start.
    empty_bst = BST()
    print("In-order on empty tree:", empty_bst.inorder())
    print("Search 1001 on empty tree:", empty_bst.search(1001))

    # The single-node tree the insert and search still work.
    single_bst = BST()
    single_bst.insert(1002)
    print("Single-node in-order:", single_bst.inorder())
    print("Search 1002 on single-node tree:", single_bst.search(1002))
    print("Search 1001 on single-node tree:", single_bst.search(1001))

    # The duplicate ID will go to the right of the child for this version.
    # BST property still holds and the in-order will stay sorted.
    print("Inserting duplicate 1003:")
    bst.insert(1003)
    print("In-order after duplicate insert:", bst.inorder())


if __name__ == "__main__":
    main()
"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================
STUDENT INSTRUCTIONS:
This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).
===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # For the missing start node, nothing is reachd, therefore a return an
    # empty order, which keeps the caller from crashing on incorrect input.
    if start not in graph:
        return []

    visited = set()
    order = []

    # There is a queue FIFO that is required so the BFS finishes the current level
    # before continuing the next one. The first place that is found is the
    # place expanded, and a stack reverses that and instead produces a depth-first behavior.
    queue = deque([start])
    visited.add(start)

    while queue:
        # A popleft is applied to remove the oldest node that is in the next
        # place in the hop order.
        node = queue.popleft()
        order.append(node)

        # The Neighbors are enqueued and aren't visited immediately, so they wait
        # behind every place at this level. It then marks if they were visited at enqueue
        # time and ensures that the same place is stopped from being added twice when
        # multiple roads or routes lead to it.
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # The BFS is different from DFS because it expands outward just one hop at a time.
    # While DFS follows one road to a dead end before it backtracks.
    # This means the BFS discovers the least amount of hops in an unweighted graph, and
    # DFS doesn't.
    return order


def add_undirected_edge(graph, a, b):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)


def display_graph(graph):
    """ This does a print of the adjacency list, which allows the structure to be visible before traversal."""
    for node in graph:
        neighbors = ", ".join(graph[node]) if graph[node] else "(no connections)"
        print(f"  {node} -> {neighbors}")


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # For my real-world graph, I created a road-trip map of places in or near the
    # states of Maryland, Virginia, West Virginia, and Utah. Every node represents a
    # place, and each edge is a direct drive or one cross-country flight.
    #
    # I have a mid-Atlantic cluster: Pasadena, Annapolis (Naval Academy),
    # the Washington Monument, and Harper's Ferry. A Utah cluster: Ogden,
    # Bluffdale, Provo, Orem, then national parks such as Goblin Valley, Escalante,
    # and Zion. 
    graph = {
        "Pasadena": ["Annapolis", "Washington Monument"],
        "Annapolis": ["Pasadena", "Washington Monument"],
        "Washington Monument": ["Pasadena", "Annapolis", "Harpers Ferry", "Ogden"],
        "Harpers Ferry": ["Washington Monument"],
        "Ogden": ["Washington Monument", "Bluffdale", "Provo"],
        "Bluffdale": ["Ogden", "Provo", "Goblin Valley"],
        "Provo": ["Ogden", "Bluffdale", "Orem"],
        "Orem": ["Provo"],
        "Goblin Valley": ["Bluffdale", "Escalante", "Zion"],
        "Escalante": ["Goblin Valley", "Zion"],
        "Zion": ["Goblin Valley", "Escalante"],
    }

    print("Nodes are places. Edges are direct drives, plus one flight.")
    display_graph(graph)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start = "Pasadena"
    order = bfs(graph, start)
    print(f"Start: {start}")
    print(f"Visit order: {' -> '.join(order)}")

    # There is a level-by-level view of the same run, and Level 0 is home.
    # Now every later level will be just one hop more away. Furthermore,
    # BFS will emit a whole level before any place on the next level and when
    # ordering a level inside a level will follow the adjacency-list order.
    print("Level 0: Pasadena")
    print("Level 1: Annapolis, Washington Monument")
    print("Level 2: Harpers Ferry, Ogden")
    print("Level 3: Bluffdale, Provo")
    print("Level 4: Goblin Valley, Orem")
    print("Level 5: Escalante, Zion")
    print("Local Maryland stops are finished before the Utah parks.")

    # Bryce Canyon is added, and it will be reached from Escalante then rerun.
    # This will most likely land on level 6, due to there only being one path that
    # goes through Escalante.
    print("\nAdded node 'Bryce Canyon' and edge Escalante -- Bryce Canyon.")
    add_undirected_edge(graph, "Escalante", "Bryce Canyon")
    display_graph(graph)
    updated = bfs(graph, start)
    print(f"Updated visit order: {' -> '.join(updated)}")
    print("Bryce Canyon is reached only through Escalante, so it is level 6.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # 1st edge case starts from a different place but has the same connected component
    # and the levels will be measured from Zion. This allows the Utah park to come first
    # Maryland will be last.
    other = bfs(graph, "Zion")
    print("1) Different start node (Zion):")
    print(f"   Visit order: {' -> '.join(other)}")
    print("   Zion is level 0. Escalante and Goblin Valley are level 1.")

    # 2nd edge case is a disconnected graph, and Antietam doesn't have a road on this map.
    # This means that a search from Pasadena won't reach it and the BFS will return the
    # component to the start.
    graph["Antietam"] = []
    disconnected = bfs(graph, "Pasadena")
    print("2) Disconnected graph (added isolated 'Antietam'):")
    print(f"   From Pasadena: {' -> '.join(disconnected)}")
    print("   Antietam is absent because no path reaches it.")
    only_antietam = bfs(graph, "Antietam")
    print(f"   From Antietam: {' -> '.join(only_antietam)}")
    print("   A start place with no edges returns only itself.")

    # 3rd edge case the start node is missing and the bfs() will check the memembership first
    # and return [], not just raise a KeyError.
    missing = bfs(graph, "Moab")
    print("3) Missing start node ('Moab'):")
    print(f"   Result: {missing}")
    print("   The start is not in the adjacency list, so the search stops.")

    # 4th edge case is a single-node graph.
    single = {"Solo": []}
    print("4) Single-node graph:")
    print(f"   Result: {bfs(single, 'Solo')}")
    print("   The queue drains after the only place. No neighbors exist.")

    # The last edge case is an empty graph.
    empty = {}
    print("5) Empty graph:")
    print(f"   Result: {bfs(empty, 'Anywhere')}")
    print("   There is no start node to enqueue, so the order is empty.")


if __name__ == "__main__":
    main()

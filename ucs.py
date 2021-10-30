from collections import OrderedDict


class UCS:
    def __init__(self, graph):
        self.graph = graph
        self.frontier = []
        self.visited = OrderedDict()

    def solve(self):
        pop_index = 0
        goal_state = None
        solution_cost = 0
        solution = []
        expanded_nodes = []
        iteration = -1

        while goal_state is None and iteration <= self.graph.maximum_depth:

            iteration += 1
            self.frontier.clear()
            self.visited.clear()
            self.frontier.append(self.graph.root)

            while len(self.frontier) > 0:

                self.sort_frontier(self.return_cost)

                current_node = self.frontier.pop(pop_index)
                self.visited[current_node] = None

                if self.is_goal(current_node):
                    goal_state = current_node
                    break

                self.add_to_frontier(current_node)

            # Add all visited nodes to expanded nodes, before clearing it.
            for node in self.visited:
                expanded_nodes.append(node)

        # Check if DFS_BFS_IDS was successful...
        if goal_state is None:
            print("No goal state found.")
            return

        # We need to calculate the cost of the solution AND get the solution itself...
        current = goal_state
        while current is not None:
            solution_cost += current.cost
            solution.insert(0, current)
            # Get the parent node and continue...
            current = current.parent

        # Print the results...
        self.print_results(solution_cost, solution, expanded_nodes)

    def add_to_frontier(self, current_node):
        nodes_to_add = []
        if current_node.east is not None and not self.is_in_visited(current_node.east):
            nodes_to_add.append(self.set_parent(current_node, current_node.east))
        if current_node.south is not None and not self.is_in_visited(current_node.south):
            nodes_to_add.append(self.set_parent(current_node, current_node.south))
        if current_node.west is not None and not self.is_in_visited(current_node.west):
            nodes_to_add.append(self.set_parent(current_node, current_node.west))
        if current_node.north is not None and not self.is_in_visited(current_node.north):
            nodes_to_add.append(self.set_parent(current_node, current_node.north))

        for node in nodes_to_add:
            self.frontier.append(node)

    def set_parent(self, parent_node, child_node):
        return child_node

    def is_in_visited(self, node):
        if node in self.visited:
            return True
        return False

    def is_goal(self, node):
        goal = self.graph.maze.goal
        if goal[0] == node.x and goal[1] == node.y:
            return True
        return False

    def sort_frontier(self, sort_by):
        self.frontier.sort(key=sort_by)

    def return_cost(self, node):
        return node.cost

    def print_results(self, solution_cost, solution, expanded_nodes):
        print("Uniform Cost Search(UCS):")
        print("Cost of the solution:", solution_cost)
        print("The solution path (" + str(len(solution)) + " nodes):", end=" ")
        for node in solution:
            print(node, end=" ")
        print("\nExpanded nodes (" + str(len(expanded_nodes)) + " nodes):", end=" ")
        for node in expanded_nodes:
            print(node, end=" ")
        print("\n")
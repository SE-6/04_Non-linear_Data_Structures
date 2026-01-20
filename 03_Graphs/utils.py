import matplotlib.pyplot as plt
import math


def draw_graph(graph):
    num_vertices = graph.num_vertices
    adj_matrix = graph.adj_matrix

    positions = {}
    offset = math.pi
    for i in range(num_vertices):
        angle = 2 * math.pi * i / num_vertices + offset
        x = math.cos(angle)
        y = math.sin(angle)
        positions[i] = (x, y)

    fig, ax = plt.subplots(figsize=(6, 6))

    # Plot nodes
    for i in range(num_vertices):
        x, y = positions[i]
        ax.scatter(x, y, s=300, color="lightblue", zorder=3)
        ax.text(x, y, graph.labels[i], fontsize=12, ha="center", va="center", zorder=4)

    # Plot directed edges, handling loops
    for i in range(num_vertices):
        for j in range(num_vertices):
            weight = adj_matrix[i][j]
            if weight != 0:
                start = positions[i]
                end = positions[j]
                if i == j:
                    # Draw loop (circle) around vertex
                    loop = plt.Circle(
                        (start[0], start[1] + 0.15),
                        0.15,
                        color="gray",
                        fill=False,
                        lw=2,
                    )
                    ax.add_patch(loop)
                    ax.text(
                        start[0],
                        start[1] + 0.35,
                        str(weight),
                        color="red",
                        fontsize=10,
                        ha="center",
                    )
                else:
                    ax.annotate(
                        "",
                        xy=end,
                        xycoords="data",
                        xytext=start,
                        textcoords="data",
                        arrowprops=dict(
                            arrowstyle="->", color="gray", lw=2, shrinkA=10, shrinkB=10
                        ),
                    )
                    mid_x = (start[0] + end[0]) / 2
                    mid_y = (start[1] + end[1]) / 2
                    ax.text(
                        mid_x,
                        mid_y,
                        str(weight),
                        color="red",
                        fontsize=10,
                        ha="center",
                        va="center",
                        zorder=5,
                    )

    ax.set_aspect("equal")
    # plt.title("Directed Graph")
    plt.axis("off")
    plt.show()


def draw_graph_nodes(graph):
    # 'graph.nodes' is our dictionary {label: Node_Object}
    nodes = list(graph.nodes.values())
    num_vertices = len(nodes)

    # 1. Calculate positions based on Node objects
    positions = {}
    offset = math.pi
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / num_vertices + offset
        x = math.cos(angle)
        y = math.sin(angle)
        positions[node] = (x, y)  # Map the actual Node object to its (x, y)

    fig, ax = plt.subplots(figsize=(6, 6))

    # 2. Plot Nodes
    for node, (x, y) in positions.items():
        ax.scatter(x, y, s=400, color="lightgreen", zorder=3, edgecolors="black")
        ax.text(
            x,
            y,
            node.label,
            fontsize=12,
            ha="center",
            va="center",
            zorder=4,
            fontweight="bold",
        )

    # 3. Plot Edges by iterating through each node's neighbors
    visited_edges = set()  # To avoid drawing the same undirected edge twice

    for node in nodes:
        start_pos = positions[node]
        for neighbor, weight in node.neighbors.items():
            end_pos = positions[neighbor]

            # For undirected graphs, we check if we've already drawn this connection
            edge_id = tuple(sorted((node.label, neighbor.label)))

            if node == neighbor:
                # Handle self-loops
                loop = plt.Circle(
                    (start_pos[0], start_pos[1] + 0.15),
                    0.15,
                    color="gray",
                    fill=False,
                    lw=1.5,
                )
                ax.add_patch(loop)
                ax.text(start_pos[0], start_pos[1] + 0.35, str(weight), color="red")

            elif edge_id not in visited_edges:
                # Draw the line
                ax.plot(
                    [start_pos[0], end_pos[0]],
                    [start_pos[1], end_pos[1]],
                    color="gray",
                    lw=1.5,
                    zorder=2,
                )

                # Calculate midpoint for weight label
                mid_x = (start_pos[0] + end_pos[0]) / 2
                mid_y = (start_pos[1] + end_pos[1]) / 2
                ax.text(
                    mid_x,
                    mid_y,
                    str(weight),
                    color="red",
                    fontsize=10,
                    ha="center",
                    va="center",
                    bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"),
                )

                visited_edges.add(edge_id)

    ax.set_aspect("equal")
    plt.axis("off")
    plt.show()

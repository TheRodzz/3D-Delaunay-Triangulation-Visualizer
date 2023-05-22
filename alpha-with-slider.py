import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import ipywidgets as widgets
from IPython.display import display
from IPython.display import display, clear_output

# Part 1: Construct Delaunay Triangulation
# Given a set of points, this function constructs a Delaunay Triangulation.
def construct_delaunay(points):
    tri = Delaunay(points)  # Compute Delaunay Triangulation
    return tri  # Return the triangulation object

# Part 2: Compute a-intervals for all simplices
# Given a Delaunay triangulation and an alpha value, this function computes the a-interval for each simplex in the triangulation.
def compute_a_intervals(tri, alpha):
    a_intervals = []  # List to store a-intervals for each simplex
    for simplex in tri.simplices:  # Loop through all simplices in the triangulation
        circumsphere = np.linalg.norm(np.hstack([tri.points[simplex], np.ones((4, 1))]), axis=1)  # Compute the radius of the circumsphere for the simplex
        if np.max(circumsphere) < alpha:  # If the radius of the circumsphere is less than alpha,
            a_intervals.append([np.max(circumsphere), np.inf])  # Append [max circumsphere radius, infinity] to a_intervals
        else:  # Otherwise,
            min_edge_len = np.min([np.linalg.norm(tri.points[simplex[(i+1)%3]] - tri.points[simplex[i]]) for i in range(3)])  # Compute the length of the shortest edge for the simplex
            a_intervals.append([alpha, min_edge_len/2])  # Append [alpha, half the length of the shortest edge] to a_intervals
    a_intervals.sort()  # Sort the a-intervals in ascending order of the upper limit
    return a_intervals  # Return the a-intervals for all simplices

# Part 3: a-shape visualizer
# Given a Delaunay triangulation, a-intervals for all simplices, and an alpha value, this function visualizes the a-shape for the triangulation.
def visualize_a_shape(tri, a_intervals, alpha):
    fig = plt.figure()  # Create a new figure
    if tri.points.shape[1] == 2:  # If the points are 2D,
        plt.triplot(tri.points[:, 0], tri.points[:, 1], tri.simplices.copy())  # Plot the Delaunay triangulation
    elif tri.points.shape[1] == 3:  # If the points are 3D,
        ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot
        ax.scatter(tri.points[:, 0], tri.points[:, 1], tri.points[:, 2], alpha=0.7)  # Scatter plot of the points

        # Loop through all simplices and their corresponding a-intervals
        for simplex, a_int in zip(tri.simplices, a_intervals):
            if a_int[0] <= alpha <= a_int[1]:  # If the alpha value lies in the a-interval for the simplex,
                verts = [tri.points[simplex[i]] for i in range(4)]  # Extract the vertices of the simplex
                collection = Poly3DCollection([verts], alpha=0.25, linewidths=0.5, edgecolors='k')
                ax.add_collection(collection)

        # The x, y, and z labels for the plot are set using ax.set_xlabel('X'), ax.set_ylabel('Y'), and ax.set_zlabel('Z'), respectively.
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    plt.show()

def update_visualization(alpha):
    clear_output(wait=True)  # Clear the current output
    alpha_intervals = compute_a_intervals(tri, alpha)  # Compute a-intervals for all simplices using the value of alpha
    visualize_a_shape(tri, alpha_intervals, alpha)  # Visualize the a-shape using the computed a-intervals and alpha value

# Test the implementation
nop = 50  # Number of points to be randomly generated
points = np.random.rand(nop, 3)  # Random points generated (x, y, z) between 0 to 1
tri = construct_delaunay(points)  # Construct Delaunay triangulation from the points

# Create a slider to change the alpha value
alpha_slider = widgets.FloatSlider(min=0, max=50, step=0.1, value=25, description="Alpha")
widgets.interact(update_visualization, alpha=alpha_slider)


'''The above code generates a 3D plot of the Delaunay triangulation and highlights the simplices whose circumradius is less 
than or equal to the given value of alpha. The value of alpha is set to alp variable, and the points are generated randomly in the range of (0,1).
The Delaunay triangulation and the highlighted simplices are visualized using the visualize_a_shape() function.'''

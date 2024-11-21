import matplotlib.pyplot as plt
# import time

class DynamicGraph:
    def __init__(self, xlim=(-10, 10), ylim=(-10, 10), title="Dynamic Graph"):
        # Create a figure and axis
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_title(title)
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        
        # Initialize an empty plot for points
        self.points, = self.ax.plot([], [], 'ro')  # 'ro' for red points
        self.x_data = []  # To store x-coordinates of points
        self.y_data = []  # To store y-coordinates of points

        # Show the plot in interactive mode
        plt.ion()
        plt.show()
    
    # remove all points
    def clear_points(self):
        self.x_data = []
        self.y_data = []

    # add a single point into the graph
    def add_point(self, x, y):
        """Add a new point to the graph dynamically."""
        self.x_data.append(x)
        self.y_data.append(y)
        self.points.set_data(self.x_data, self.y_data)  # Update the data
        plt.draw()  # Redraw the plot
        plt.pause(1)  # Pause to make updates visible
    
    # add a list of x points and y points
    def add_points(self,x_arr,y_arr):
        self.x_data = x_arr
        self.y_data = y_arr

    def close(self):
        """Close the plot window."""
        plt.ioff()
        plt.close(self.fig)


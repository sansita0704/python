import matplotlib.pyplot as plt


def get_coordinates(line_number):
    # Get x and y coordinates from user input
    print(f"Enter the coordinates for Line {line_number}:")
    x_input = input(f"Enter X coordinates for Line {line_number} (comma-separated): ")
    y_input = input(f"Enter Y coordinates for Line {line_number} (comma-separated): ")

    # Convert input strings to lists of floats
    x_coordinates = list(map(float, x_input.split(',')))
    y_coordinates = list(map(float, y_input.split(',')))

    return x_coordinates, y_coordinates


def plot_graph(x1, y1, x2, y2, x3, y3):
    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot the three lines
    plt.plot(x1, y1, marker='o', linestyle='-', color='b', label='Line 1')
    plt.plot(x2, y2, marker='x', linestyle='--', color='g', label='Line 2')
    plt.plot(x3, y3, marker='s', linestyle='-.', color='r', label='Line 3')

    # Add titles and labels
    plt.title('Three Line Graphs in One Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Add grid, legend, and display
    plt.grid()
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == '__main__':
    # Get coordinates for three lines
    x1, y1 = get_coordinates(1)
    x2, y2 = get_coordinates(2)
    x3, y3 = get_coordinates(3)

    # Plot the three lines on the same plot
    plot_graph(x1, y1, x2, y2, x3, y3)
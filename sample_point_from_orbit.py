import numpy as np
import random
import matplotlib.pyplot as plt

def sample_points_on_sphere(num_points):
    points = [[0, 0, -1]]
    for _ in range(num_points):
        theta = random.uniform(0, 2*np.pi)
        phi = random.uniform(0, np.pi)
        x = np.sin(phi) * np.cos(theta)
        y = np.sin(phi) * np.sin(theta)
        z = -1 + np.cos(phi)
        points.append((x, y, z))
    return points
    # for _ in range(num_points):
    #     z = round(random.uniform(-1, 1),2)
    #     theta = random.uniform(0, 2*np.pi)
    #     x = round(np.sqrt(1 - z**2) * np.cos(theta),2)
    #     y = round(np.sqrt(1 - z**2) * np.sin(theta),2)
    #     points.append([x, y, z])
    # return points

def visualize_points(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in points:
        ax.scatter(point[0], point[1], point[2], c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


if __name__ == "__main__":
    num_points = 500
    points = sample_points_on_sphere(num_points)
    # for point in points:
    #     print(point)

    # visualize_points(points)

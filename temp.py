import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_zolaman(ax):
    # 졸라맨의 몸통
    body_vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])
    body_faces = [
        [body_vertices[0], body_vertices[1], body_vertices[2], body_vertices[3]],
        [body_vertices[4], body_vertices[5], body_vertices[6], body_vertices[7]],
        [body_vertices[0], body_vertices[1], body_vertices[5], body_vertices[4]],
        [body_vertices[2], body_vertices[3], body_vertices[7], body_vertices[6]],
        [body_vertices[0], body_vertices[3], body_vertices[7], body_vertices[4]],
        [body_vertices[1], body_vertices[2], body_vertices[6], body_vertices[5]]
    ]
    for face in body_faces:
        draw_face(ax, face)

    # 졸라맨의 눈
    ax.scatter(0.3, 0.7, 1, color='black', s=100)
    ax.scatter(0.7, 0.7, 1, color='black', s=100)

    # 졸라맨의 입
    ax.plot([0.4, 0.6], [0.4, 0.4], zs=1, color='black')

    # 졸라맨의 팔
    arm_vertices = np.array([
        [0, 0.5, 0.75],
        [0, 0.5, 0.25],
        [0, 0.25, 0.25],
        [0, 0.25, 0.75],
        [1, 0.5, 0.75],
        [1, 0.5, 0.25],
        [1, 0.25, 0.25],
        [1, 0.25, 0.75]
    ])
    arm_faces = [
        [arm_vertices[0], arm_vertices[1], arm_vertices[2], arm_vertices[3]],
        [arm_vertices[4], arm_vertices[5], arm_vertices[6], arm_vertices[7]],
        [arm_vertices[0], arm_vertices[1], arm_vertices[5], arm_vertices[4]],
        [arm_vertices[2], arm_vertices[3], arm_vertices[7], arm_vertices[6]],
        [arm_vertices[0], arm_vertices[3], arm_vertices[7], arm_vertices[4]],
        [arm_vertices[1], arm_vertices[2], arm_vertices[6], arm_vertices[5]]
    ]
    for face in arm_faces:
        draw_face(ax, face)

    # 졸라맨의 다리
    leg_vertices = np.array([
        [0.25, 0, 0.25],
        [0.75, 0, 0.25],
        [0.75, 0, 0.75],
        [0.25, 0, 0.75],
        [0.25, 0, 0],
        [0.75, 0, 0],
        [0.75, 0, 1],
        [0.25, 0, 1]
    ])
    leg_faces = [
        [leg_vertices[0], leg_vertices[1], leg_vertices[2], leg_vertices[3]],
        [leg_vertices[4], leg_vertices[5], leg_vertices[6], leg_vertices[7]],
        [leg_vertices[0], leg_vertices[1], leg_vertices[5], leg_vertices[4]],
        [leg_vertices[2], leg_vertices[3], leg_vertices[7], leg_vertices[6]],
        [leg_vertices[0], leg_vertices[3], leg_vertices[7], leg_vertices[4]],
        [leg_vertices[1], leg_vertices[2], leg_vertices[6], leg_vertices[5]]
    ]
    for face in leg_faces:
        draw_face(ax, face)

def draw_face(ax, vertices):
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]
    ax.plot3D(x, y, z, color='blue')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
draw_zolaman(ax)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
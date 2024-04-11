import numpy as np
import cv2 as cv
from sample_point_from_orbit import sample_points_on_sphere
from load_camera_parameter import camera_parameter_load

# The given video and calibration data
video_file = 'data/chessboard.MOV'
file_name = 'result/calibration_results.txt'

def rotation_matrix_2d(angle):
    """
    2D 회전 변환 행렬 생성
    :param angle: 회전 각도 (라디안 단위)
    :return: 회전 변환 행렬
    """
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    return np.array([[cos_theta, -sin_theta, 0],
                     [sin_theta, cos_theta, 0],
                     [0, 0, 1]])


K, dist_coeff = camera_parameter_load(file_name)

board_pattern = (10, 7)
board_cellsize = 0.025
board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

# Open a video
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

points = sample_points_on_sphere(1000)
points = board_cellsize * np.array(points, dtype=np.float) * 2

# Prepare 3D points on a chessboard
obj_points = board_cellsize * np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])])

# Run pose estimation
while True:
    # Read an image from the video
    valid, img = video.read()
    if not valid:
        break

    # Estimate the camera pose
    success, img_points = cv.findChessboardCorners(img, board_pattern, board_criteria)
    if success:
        ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist_coeff)

        points = np.dot(points, rotation_matrix_2d(np.pi / 8))
        new_points, _ = cv.projectPoints(points, rvec, tvec, K, dist_coeff)

        for i, point in enumerate(new_points[1:]):
            r = (i / len(new_points)) * 255
            g = ((len(new_points) - i) / len(new_points)) * 255
            b = max(0,255-r) # 파란색 성분
            cv.circle(img, np.int32(point[0]), 2, (b,g,r), -1)

        # Print the camera position
        R, _ = cv.Rodrigues(rvec) # Alternative) `scipy.spatial.transform.Rotation`
        p = (-R.T @ tvec).flatten()
        info = f'XYZ: [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Show the image and process the key event
    cv.imshow('Pose Estimation (Chessboard)', img)
    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

video.release()
cv.destroyAllWindows()

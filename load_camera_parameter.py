import numpy as np

def camera_parameter_load(file_name):
    K = []
    dist_coeff = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                if line.startswith("RMS:"):
                    rms = float(line.split(":")[1].strip())
                elif line.startswith("Camera matrix (K):"):
                    for _ in range(3):
                        K.append(list(map(float, file.readline().strip().split())))
                elif line.startswith("Distortion coefficient:"):
                    dist_coeff = list(map(float, file.readline().strip().split()))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("File not found. Check file path or run camera calibration first!")

    print("Loaded RMS:", rms)
    print("Loaded Camera matrix (K):", K)
    print("Loaded Distortion coefficient:", dist_coeff)

    K = np.array(K)
    dist_coeff = np.array(dist_coeff)

    return K, dist_coeff

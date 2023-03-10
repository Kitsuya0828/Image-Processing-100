import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image


def hist_equal(img: np.ndarray, z_max: int=255):
	H, W, C = img.shape
	S = H * W * C

	out = img.copy()

	sum_h = 0

	for i in range(1, 255):
		ind = np.where(img == i)
		sum_h += len(img[ind])
		z_prime = z_max / S * sum_h
		out[ind] = z_prime

	out = out.astype(np.uint8)

	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)
    
    dt_now = datetime.datetime.now()
    save_path = f"{dt_now.strftime('%Y%m%d%H%M%S')}.jpg"
    plt.hist(img.ravel(), bins=255, rwidth=0.8, range=(0, 255))
    plt.savefig(save_dir + save_path)
    return {"path": save_path}


if __name__ == "__main__":
    sample_path = "../../files/sample/imori_dark.jpeg"
    save_dir = "../../files/"
    result_path = save_dir + solve(sample_path, save_dir)["path"]

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 3, 1)
    plt.title('input')
    sample_image = Image.open(sample_path)
    sample_array = np.asarray(sample_image)
    plt.imshow(sample_array)

    plt.subplot(1, 3, 2)
    plt.title('output')
    result_image = Image.open(result_path)
    result_array = np.asarray(result_image)
    plt.imshow(result_array)

    plt.show()

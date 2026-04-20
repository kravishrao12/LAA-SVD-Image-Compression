import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def compress_svd(channel, k):
    U, S, Vt = np.linalg.svd(channel, full_matrices=False)
    S_k = np.diag(S[:k])
    U_k = U[:, :k]
    Vt_k = Vt[:k, :]
    return np.dot(U_k, np.dot(S_k, Vt_k))

def compress_image(image, k):
    if len(image.shape) == 2:
        return compress_svd(image, k)
    else:
        channels = []
        for i in range(3):
            comp = compress_svd(image[:, :, i], k)
            channels.append(comp)
        return np.stack(channels, axis=2)

def mse(original, compressed):
    return np.mean((original - compressed) ** 2)

def compression_ratio(shape, k, channels=1):
    m, n = shape[0], shape[1]
    original = m * n * channels
    compressed = k * (m + n + 1) * channels
    return original / compressed

# ---------------- MAIN ----------------
img_path = "images/sample.jpg"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

img = cv2.imread(img_path)

if img is None:
    print("ERROR: Image not found. Put sample.jpg inside images folder.")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

k_values = [5, 20, 50, 100]

plt.figure(figsize=(12, 8))

for i, k in enumerate(k_values):
    comp = compress_image(img, k)
    comp = np.clip(comp, 0, 255).astype(np.uint8)

    err = mse(img, comp)
    ratio = compression_ratio(img.shape, k, channels=3)

    print(f"k={k} | MSE={err:.2f} | Compression Ratio={ratio:.2f}")

    cv2.imwrite(f"{output_dir}/compressed_k{k}.jpg",
                cv2.cvtColor(comp, cv2.COLOR_RGB2BGR))

    plt.subplot(2, 2, i+1)
    plt.imshow(comp)
    plt.title(f"k={k}")
    plt.axis("off")

plt.suptitle("SVD Image Compression")
plt.show()
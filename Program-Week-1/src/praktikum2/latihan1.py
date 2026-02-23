# ============================================
# PRAKTIKUM 2: DASAR-DASAR CITRA DIGITAL
# ============================================
# Nama:  Muhammad Rafi Fatihul Ihsan
# NIM:   24343016
# Kelas: 202523430039
# ============================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from PIL import Image

def load_sample_from_url(url):
    response = requests.get(url, timeout=10)
    img = Image.open(BytesIO(response.content))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def analyze_my_image(image_path, sample_url):

    print("="*60)
    print("ANALISIS CITRA UTAMA")
    print("="*60)

    img = cv2.imread(image_path)

    if img is None:
        print("Image tidak ditemukan. Periksa path.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width, channels = img.shape
    resolution = width * height
    aspect_ratio = width / height

    print("Dimensi      :", width, "x", height)
    print("Channels     :", channels)
    print("Resolusi     :", resolution, "pixel")
    print("Aspect Ratio :", round(aspect_ratio, 2))

    memory_color = img.size * img.dtype.itemsize
    memory_gray = gray.size * gray.dtype.itemsize

    print("Memori Color :", memory_color, "bytes")
    print("Memori Gray  :", memory_gray, "bytes")

    print("\nStatistik Grayscale")
    print("Mean :", np.mean(gray))
    print("Std  :", np.std(gray))
    print("Min  :", np.min(gray))
    print("Max  :", np.max(gray))

    # ==============================
    # TAMPILKAN GAMBAR
    # ==============================

    sample = load_sample_from_url(sample_url)
    sample_gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Citra Anda (Color)")
    plt.axis("off")

    plt.subplot(2,2,2)
    plt.imshow(gray, cmap="gray")
    plt.title("Citra Anda (Grayscale)")
    plt.axis("off")

    plt.subplot(2,2,3)
    plt.imshow(cv2.cvtColor(sample, cv2.COLOR_BGR2RGB))
    plt.title("Sample Lena (Color)")
    plt.axis("off")

    plt.subplot(2,2,4)
    plt.imshow(sample_gray, cmap="gray")
    plt.title("Sample Lena (Grayscale)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # ==============================
    # HISTOGRAM
    # ==============================

    plt.figure(figsize=(15,5))

    # Histogram grayscale
    plt.subplot(1,3,1)
    plt.hist(gray.ravel(), 256, [0,256])
    plt.title("Histogram Grayscale Anda")
    plt.xlabel("Intensitas")
    plt.ylabel("Frekuensi")

    # Histogram RGB
    plt.subplot(1,3,2)
    colors = ["b","g","r"]
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist, color=color)
    plt.title("Histogram RGB Anda")
    plt.xlabel("Intensitas")
    plt.ylabel("Frekuensi")

    # Histogram kumulatif
    plt.subplot(1,3,3)
    hist = np.histogram(gray.ravel(),256,[0,256])[0]
    cumulative = np.cumsum(hist)
    cumulative = cumulative / cumulative.max() * 100
    plt.plot(cumulative)
    plt.title("Histogram Kumulatif Anda")
    plt.xlabel("Intensitas")
    plt.ylabel("Kumulatif (%)")

    plt.tight_layout()
    plt.show()

    # ==============================
    # PERBANDINGAN RESOLUSI
    # ==============================

    h2, w2, c2 = sample.shape
    res2 = w2 * h2

    print("\n" + "="*60)
    print("PERBANDINGAN DENGAN SAMPLE")
    print("="*60)

    print("Citra Anda   :", width, "x", height, "| Resolusi:", resolution)
    print("Sample Lena  :", w2, "x", h2, "| Resolusi:", res2)

    if resolution > res2:
        print("Resolusi citra anda lebih tinggi dari sample")
    elif resolution < res2:
        print("Resolusi sample lebih tinggi dari citra anda")
    else:
        print("Resolusi keduanya sama")

# ======================================
# PATH
# ======================================

image_path = r"C:\Users\Pongo\Desktop\kuliah\Semester 4\Pengolahan Citra Digital\minggu 1\src\img\kucing_rafi.jpeg"
sample_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"

analyze_my_image(image_path, sample_url)

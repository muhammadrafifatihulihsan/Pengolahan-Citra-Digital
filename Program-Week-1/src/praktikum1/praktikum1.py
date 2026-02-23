# ============================================
# PRAKTIKUM 1: DASAR-DASAR CITRA DIGITAL
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

print("="*50)
print("=== PRAKTIKUM 1: DASAR-DASAR CITRA DIGITAL ===")
print("===     Representasi Citra, Resolusi,       ===")
print("===       Bit Depth, Aspect Ratio           ===")
print("="*50)

# =============== FUNGSI BANTU ===============

def download_sample_image():
    """Download sample image from internet"""
    # Menggunakan gambar Lena atau gambar sample lainnya
    # url = "https://www.bitvonline.com/cdn/uploads/images/2025/05/_3670_Bahlil-Heran-Indonesia-Impor-BBM-dari-Singapura--Lucu--Negara-Tak-Punya-Minyak--Kok-Bisa-Kita-Bergantung-.png"
    url = r"C:\Users\Pongo\Desktop\kuliah\Semester 4\Pengolahan Citra Digital\minggu 1\program\src\img\lena.jpg"

    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        print("✓ Gambar berhasil di-download")
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    except:
        print("! Gagal download, membuat dummy image")
        # Buat dummy image jika download gagal
        dummy = np.zeros((512, 512, 3), dtype=np.uint8)
        dummy[:,:] = [127, 127, 127]
        cv2.rectangle(dummy, (100,100), (400,400), (0,255,0), 3)
        cv2.circle(dummy, (256,256), 100, (255,0,0), 3)
        cv2.putText(dummy, "SAMPLE IMAGE", (150,450), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        return dummy

def analyze_image_properties(img, name="Image"):
    """Analyze and display image properties"""
    if len(img.shape) == 2:
        height, width = img.shape
        channels = 1
        img_type = "Grayscale"
    else:
        height, width, channels = img.shape
        img_type = "Color"
    
    resolution = width * height
    aspect_ratio = width / height
    depth = img.dtype.itemsize * 8
    
    print(f"\n{'─'*50}")
    print(f"📊 ANALISIS: {name}")
    print(f"{'─'*50}")
    print(f"🖼️  Tipe         : {img_type}")
    print(f"📐 Dimensi      : {width} x {height} pixel")
    print(f"🎨 Channel      : {channels} channel(s)")
    print(f"🔍 Resolusi     : {resolution:,} pixel")
    print(f"📏 Aspect Ratio : {aspect_ratio:.2f} ({width}:{height})")
    print(f"💎 Bit Depth    : {depth}-bit ({img.dtype})")
    
    memory_bytes = img.size * img.dtype.itemsize
    memory_kb = memory_bytes / 1024
    memory_mb = memory_kb / 1024
    
    print(f"💾 Ukuran Memori: {memory_bytes:,} bytes")
    print(f"                  {memory_kb:.2f} KB")
    print(f"                  {memory_mb:.2f} MB")
    
    if channels == 1:
        print(f"📊 Intensitas   : [{img.min()}, {img.max()}]")
        print(f"📊 Rata-rata    : {img.mean():.2f}")
        print(f"📊 Std Dev      : {img.std():.2f}")
    
    return {
        'width': width, 'height': height, 'channels': channels,
        'resolution': resolution, 'aspect_ratio': aspect_ratio,
        'depth': depth, 'memory_bytes': memory_bytes
    }

def display_image_grid(images, titles, rows, cols, figsize=(15, 10)):
    """Display multiple images in a grid"""
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.ravel() if rows > 1 or cols > 1 else [axes]
    
    for idx, (img, title) in enumerate(zip(images, titles)):
        if len(img.shape) == 2:
            axes[idx].imshow(img, cmap='gray')
        else:
            axes[idx].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axes[idx].set_title(title, fontsize=12, fontweight='bold')
        axes[idx].axis('off')
    
    plt.tight_layout()
    plt.show()

# =============== MAIN PRAKTIKUM ===============

print("\n" + "="*50)
print("📌 TAHAP 1: LOAD DAN ANALISIS CITRA SAMPLE")
print("="*50)

# 1. LOAD DAN ANALISIS CITRA SAMPLE
original_img = download_sample_image()
props_original = analyze_image_properties(original_img, "Original Color Image")

print("\n" + "="*50)
print("📌 TAHAP 2: REPRESENTASI MATRIKS CITRA")
print("="*50)

# 2. REPRESENTASI MATRIKS
print("\n🔍 Mengakses nilai pixel pada posisi tertentu:")
x, y = 100, 100
pixel_value = original_img[x, y]
print(f"   Pixel pada posisi ({x}, {y}): BGR = {pixel_value}")

print("\n🔍 Area 5x5 pixel dari posisi (100,100):")
print("   ", original_img[100:105, 100:105])
print("\n   ➤ Setiap pixel direpresentasikan sebagai array [B, G, R]")
print("   ➤ Nilai range: 0-255 untuk tiap channel")

print("\n" + "="*50)
print("📌 TAHAP 3: KONVERSI KE GRAYSCALE")
print("="*50)

# 3. KONVERSI GRAYSCALE
gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
props_gray = analyze_image_properties(gray_img, "Grayscale Image")

print("\n📝 Rumus Grayscale: Y = 0.299*R + 0.587*G + 0.114*B")

print("\n" + "="*50)
print("📌 TAHAP 4: ANALISIS PENGARUH BIT DEPTH")
print("="*50)

# 4. ANALISIS BIT DEPTH YANG BERBEDA
img_8bit = gray_img.astype(np.uint8)
img_4bit = (gray_img // 16).astype(np.uint8) * 16
img_2bit = (gray_img // 64).astype(np.uint8) * 64
img_1bit = (gray_img // 128).astype(np.uint8) * 255

print("\n📊 Perbandingan Bit Depth:")
print("   • 8-bit: 256 level intensitas (0-255)")
print("   • 4-bit: 16 level intensitas (0,16,32,...,240)")
print("   • 2-bit: 4 level intensitas (0,64,128,192)")
print("   • 1-bit: 2 level intensitas (0 dan 255)")

images_bitdepth = [img_8bit, img_4bit, img_2bit, img_1bit]
titles_bitdepth = [
    '8-bit (256 levels)\nKualitas Terbaik', 
    '4-bit (16 levels)\nKualitas Sedang', 
    '2-bit (4 levels)\nKualitas Rendah', 
    '1-bit (2 levels)\nBinary'
]
display_image_grid(images_bitdepth, titles_bitdepth, 1, 4, figsize=(16, 4))

print("\n" + "="*50)
print("📌 TAHAP 5: ANALISIS PENGARUH ASPECT RATIO")
print("="*50)

# 5. ANALISIS ASPECT RATIO
h, w = gray_img.shape[:2]
img_4_3 = cv2.resize(gray_img, (800, 600))
img_16_9 = cv2.resize(gray_img, (800, 450))
img_1_1 = cv2.resize(gray_img, (600, 600))
img_21_9 = cv2.resize(gray_img, (840, 360))

print("\n📊 Perbandingan Aspect Ratio:")
print("   • 4:3  - Standar TV/lama")
print("   • 16:9 - Widescreen/HDTV")
print("   • 1:1  - Persegi/Instagram")
print("   • 21:9 - Cinematic/Ultrawide")

images_aspect = [img_4_3, img_16_9, img_1_1, img_21_9]
titles_aspect = ['4:3 (800x600)', '16:9 (800x450)', '1:1 (600x600)', '21:9 (840x360)']
display_image_grid(images_aspect, titles_aspect, 2, 2, figsize=(12, 8))

print("\n" + "="*50)
print("📌 TAHAP 6: SEPARASI CHANNEL WARNA RGB")
print("="*50)

# 6. SEPARASI CHANNEL WARNA
b, g, r = cv2.split(original_img)
zeros = np.zeros_like(b)

blue_channel = cv2.merge([b, zeros, zeros])
green_channel = cv2.merge([zeros, g, zeros])
red_channel = cv2.merge([zeros, zeros, r])

print("\n📊 Informasi Channel RGB:")
print(f"   • Blue  Channel - Mean: {b.mean():.2f}, Std: {b.std():.2f}")
print(f"   • Green Channel - Mean: {g.mean():.2f}, Std: {g.std():.2f}")
print(f"   • Red   Channel - Mean: {r.mean():.2f}, Std: {r.std():.2f}")

images_channels = [original_img, blue_channel, green_channel, red_channel]
titles_channels = ['Original RGB', 'Blue Channel Only', 'Green Channel Only', 'Red Channel Only']
display_image_grid(images_channels, titles_channels, 2, 2, figsize=(12, 8))

print("\n" + "="*50)
print("📌 TAHAP 7: ANALISIS HISTOGRAM INTENSITAS")
print("="*50)

# 7. HISTOGRAM INTENSITAS
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Histogram grayscale
axes[0].hist(gray_img.ravel(), 256, [0, 256], color='gray', alpha=0.7)
axes[0].set_title('📊 Histogram Grayscale', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Intensitas Pixel')
axes[0].set_ylabel('Frekuensi')
axes[0].grid(True, alpha=0.3)
axes[0].axvline(gray_img.mean(), color='red', linestyle='--', label=f'Mean: {gray_img.mean():.1f}')
axes[0].legend()

# Histogram per channel warna
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([original_img], [i], None, [256], [0, 256])
    axes[1].plot(hist, color=color, linewidth=2)
axes[1].set_title('📊 Histogram per Channel RGB', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Intensitas Pixel')
axes[1].set_ylabel('Frekuensi')
axes[1].legend(['Blue', 'Green', 'Red'])
axes[1].grid(True, alpha=0.3)

# Cumulative histogram
cumulative_hist = np.cumsum(np.histogram(gray_img.ravel(), 256, [0, 256])[0])
cumulative_normalized = cumulative_hist / cumulative_hist.max() * 100
axes[2].plot(cumulative_normalized, color='purple', linewidth=2)
axes[2].set_title('📊 Histogram Kumulatif', fontsize=12, fontweight='bold')
axes[2].set_xlabel('Intensitas Pixel')
axes[2].set_ylabel('Kumulatif (%)')
axes[2].grid(True, alpha=0.3)
axes[2].axhline(50, color='red', linestyle='--', alpha=0.5, label='Median')
axes[2].legend()

plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("📌 TAHAP 8: ANALISIS UKURAN MEMORI")
print("="*50)

# 8. MEMORY ANALYSIS
print("\n💾 Perbandingan ukuran memori untuk berbagai format:\n")

sizes = [(640, 480), (1280, 720), (1920, 1080), (3840, 2160)]
formats = ['Grayscale (8-bit)', 'RGB (24-bit)', 'RGBA (32-bit)']

print("┌" + "─"*74 + "┐")
print(f"│ {'Resolution':<15} {'Format':<20} {'Memory Size':>35} │")
print("├" + "─"*74 + "┤")

for w, h in sizes:
    for fmt_idx, fmt_name in enumerate(formats):
        if fmt_name == 'Grayscale (8-bit)':
            channels = 1
            depth = 1
            color_depth = "8-bit"
        elif fmt_name == 'RGB (24-bit)':
            channels = 3
            depth = 3
            color_depth = "24-bit"
        else:
            channels = 4
            depth = 4
            color_depth = "32-bit"
        
        memory = w * h * depth
        memory_kb = memory / 1024
        memory_mb = memory_kb / 1024
        
        resolution_str = f"{w}x{h}"
        memory_str = f"{memory:,} bytes ({memory_mb:.2f} MB)"
        print(f"│ {resolution_str:<15} {fmt_name:<20} {memory_str:>35} │")
    print("├" + "─"*74 + "┤")
print("└" + "─"*74 + "┘")

# =============== RANGKUMAN ===============
print("\n" + "="*50)
print("📋 RANGKUMAN HASIL PRAKTIKUM")
print("="*50)

print(f"""
📌 KESIMPULAN:

1. REPRESENTASI CITRA:
   • Citra digital = matriks 2D/3D berisi nilai pixel
   • Citra warna: 3 channel (RGB/BGR)
   • Citra grayscale: 1 channel

2. RESOLUSI:
   • Original: {props_original['width']}x{props_original['height']} pixel
   • Total pixel: {props_original['resolution']:,} pixel
   • Semakin tinggi resolusi → detail lebih baik

3. BIT DEPTH:
   • 8-bit: 256 warna → kualitas terbaik
   • 4-bit: 16 warna → kualitas menurun
   • 2-bit: 4 warna → kualitas rendah
   • 1-bit: 2 warna → hanya hitam putih

4. ASPECT RATIO:
   • Mempengaruhi komposisi visual
   • Pemilihan rasio tergantung kebutuhan

5. UKURAN MEMORI:
   • Grayscale 8-bit: 1 byte/pixel
   • RGB 24-bit: 3 byte/pixel
   • RGBA 32-bit: 4 byte/pixel
   • 4K RGB: ~24 MB, 4K Grayscale: ~8 MB
""")

print("\n" + "="*50)
print("✅ PRAKTIKUM 1 SELESAI")
print("="*50)
print("\n📝 TUGAS MAKALAH:")
print("   1. Jelaskan teori dasar citra digital")
print("   2. Analisis setiap output praktikum")
print("   3. Buat kesimpulan dan saran")
print("   4. Upload makalah di bagian Assignment\n")
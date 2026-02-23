# ============================================
# LATIHAN 1: ANALISIS CITRA PRIBADI
# ============================================
# Nama  : 
# NIM   : 
# Kelas : 
# ============================================
# Petunjuk:
# 1. Ambil foto menggunakan smartphone/kamera digital
# 2. Simpan file foto (contoh: 'foto_saya.jpg')
# 3. Jalankan kode ini dan masukkan path foto Anda
# 4. Amati hasil analisis yang ditampilkan
# ============================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from pathlib import Path

def analyze_my_image(image_path, compare_image=None):
    """
    Analisis lengkap properti citra dari foto pribadi.
    
    Parameters:
        image_path (str): Path ke file gambar yang akan dianalisis
        compare_image (str, optional): Path ke gambar pembanding
    
    Returns:
        dict: Dictionary berisi hasil analisis
    """
    
    # ============= 1. LOAD CITRA =============
    print("\n" + "="*60)
    print("📸 ANALISIS CITRA PRIBADI")
    print("="*60)
    
    # Cek apakah file ada
    if not os.path.exists(image_path):
        print(f"❌ Error: File '{image_path}' tidak ditemukan!")
        print("   Pastikan path file sudah benar.")
        return None
    
    # Baca gambar
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Error: Tidak dapat membaca file gambar. Format mungkin tidak didukung.")
        return None
    
    print(f"✓ Gambar berhasil dimuat: {os.path.basename(image_path)}")
    
    # ============= 2. DIMENSI & RESOLUSI =============
    print("\n" + "-"*60)
    print("📐 1. DIMENSI DAN RESOLUSI")
    print("-"*60)
    
    h, w = img.shape[:2]
    channels = 1 if len(img.shape) == 2 else img.shape[2]
    resolution = w * h
    
    print(f"   Dimensi         : {w} x {h} pixel")
    print(f"   Resolusi        : {resolution:,} pixel")
    print(f"   Jumlah Channel  : {channels}")
    
    # ============= 3. ASPECT RATIO =============
    aspect_ratio = w / h
    print(f"\n📏 2. ASPECT RATIO")
    print(f"   Aspect Ratio    : {aspect_ratio:.3f} ({w}:{h})")
    
    # Klasifikasi aspect ratio umum
    if 1.33 <= aspect_ratio <= 1.36:
        ratio_type = "4:3 (Standar)"
    elif 1.77 <= aspect_ratio <= 1.8:
        ratio_type = "16:9 (Widescreen)"
    elif 0.99 <= aspect_ratio <= 1.01:
        ratio_type = "1:1 (Persegi)"
    elif 2.33 <= aspect_ratio <= 2.4:
        ratio_type = "21:9 (Cinematic)"
    else:
        ratio_type = "Lainnya"
    print(f"   Tipe Rasio      : {ratio_type}")
    
    # ============= 4. KONVERSI GRAYSCALE & PERBANDINGAN UKURAN =============
    print("\n" + "-"*60)
    print("🎨 3. KONVERSI GRAYSCALE DAN PERBANDINGAN UKURAN")
    print("-"*60)
    
    if channels == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("   ✓ Berhasil dikonversi ke grayscale")
    else:
        gray = img.copy()
        print("   ⚠ Gambar sudah grayscale")
    
    # Ukuran memori
    mem_rgb = img.size * img.dtype.itemsize
    mem_gray = gray.size * gray.dtype.itemsize
    mem_rgb_kb = mem_rgb / 1024
    mem_gray_kb = mem_gray / 1024
    penghematan = (1 - mem_gray/mem_rgb) * 100 if channels == 3 else 0
    
    print(f"\n   📊 Perbandingan Ukuran Memori:")
    print(f"      • RGB   : {mem_rgb:>10,} bytes ({mem_rgb_kb:.2f} KB)")
    print(f"      • Gray  : {mem_gray:>10,} bytes ({mem_gray_kb:.2f} KB)")
    if channels == 3:
        print(f"      • Hemat : {penghematan:.1f}%")
    
    # ============= 5. STATISTIK INTENSITAS =============
    print("\n" + "-"*60)
    print("📊 4. STATISTIK INTENSITAS")
    print("-"*60)
    
    # Statistik untuk grayscale
    print("   🔹 Grayscale Channel:")
    print(f"      • Min     : {gray.min()}")
    print(f"      • Max     : {gray.max()}")
    print(f"      • Mean    : {gray.mean():.2f}")
    print(f"      • Std Dev : {gray.std():.2f}")
    print(f"      • Median  : {np.median(gray):.2f}")
    
    # Statistik per channel jika RGB
    if channels == 3:
        print("\n   🔹 RGB Channels:")
        colors = ('Blue', 'Green', 'Red')
        for i, color in enumerate(colors):
            channel = img[:,:,i]
            print(f"      • {color:6} : min={channel.min():3d}, max={channel.max():3d}, "
                  f"mean={channel.mean():6.2f}, std={channel.std():6.2f}")
    
    # ============= 6. HISTOGRAM =============
    print("\n" + "-"*60)
    print("📈 5. VISUALISASI HISTOGRAM")
    print("-"*60)
    print("   Menampilkan histogram untuk semua channel...")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f'Analisis Histogram: {os.path.basename(image_path)}', fontsize=14, fontweight='bold')
    
    # Histogram grayscale
    axes[0,0].hist(gray.ravel(), 256, [0,256], color='gray', alpha=0.7)
    axes[0,0].axvline(gray.mean(), color='red', linestyle='--', label=f'Mean: {gray.mean():.1f}')
    axes[0,0].set_title('Grayscale Histogram')
    axes[0,0].set_xlabel('Intensitas')
    axes[0,0].set_ylabel('Frekuensi')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # Histogram RGB
    if channels == 3:
        colors_rgb = ('b', 'g', 'r')
        for i, col in enumerate(colors_rgb):
            hist = cv2.calcHist([img], [i], None, [256], [0,256])
            axes[0,1].plot(hist, color=col, linewidth=2)
        axes[0,1].set_title('RGB Channel Histograms')
        axes[0,1].set_xlabel('Intensitas')
        axes[0,1].set_ylabel('Frekuensi')
        axes[0,1].legend(['Blue', 'Green', 'Red'])
        axes[0,1].grid(True, alpha=0.3)
    else:
        axes[0,1].text(0.5, 0.5, 'Gambar Grayscale\n(tidak ada channel RGB)', 
                      ha='center', va='center', fontsize=12)
        axes[0,1].set_title('RGB Channel Histograms')
        axes[0,1].axis('off')
    
    # Histogram kumulatif
    cum_hist = np.cumsum(np.histogram(gray.ravel(), 256, [0,256])[0])
    cum_hist_norm = cum_hist / cum_hist.max() * 100
    axes[1,0].plot(cum_hist_norm, color='purple', linewidth=2)
    axes[1,0].axhline(50, color='red', linestyle='--', alpha=0.5, label='Median')
    axes[1,0].set_title('Histogram Kumulatif (Grayscale)')
    axes[1,0].set_xlabel('Intensitas')
    axes[1,0].set_ylabel('Kumulatif (%)')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # Tampilkan gambar asli kecil
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if channels == 3 else img
    axes[1,1].imshow(img_rgb, cmap='gray' if channels==1 else None)
    axes[1,1].set_title('Gambar Asli (Preview)')
    axes[1,1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # ============= 7. PERBANDINGAN DENGAN CITRA LAIN =============
    print("\n" + "-"*60)
    print("🔄 6. PERBANDINGAN DENGAN CITRA SAMPLE")
    print("-"*60)
    
    if compare_image and os.path.exists(compare_image):
        img2 = cv2.imread(compare_image)
        if img2 is not None:
            # Resize untuk perbandingan
            h2, w2 = img2.shape[:2]
            print(f"   Citra pembanding: {os.path.basename(compare_image)}")
            print(f"      Dimensi : {w2} x {h2} pixel")
            
            # Bandingkan beberapa parameter
            print("\n   📊 Perbandingan Parameter:")
            print(f"      {'Parameter':<20} {'Citra Anda':<20} {'Citra Sample':<20}")
            print(f"      {'-'*60}")
            
            # Resolusi
            res_you = resolution
            res_comp = w2 * h2
            print(f"      {'Resolusi (pixel)':<20} {res_you:<20,} {res_comp:<20,}")
            
            # Aspect ratio
            ar_you = aspect_ratio
            ar_comp = w2 / h2
            print(f"      {'Aspect Ratio':<20} {ar_you:<20.3f} {ar_comp:<20.3f}")
            
            # Mean grayscale
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) if len(img2.shape)==3 else img2
            mean_you = gray.mean()
            mean_comp = gray2.mean()
            print(f"      {'Mean Intensitas':<20} {mean_you:<20.2f} {mean_comp:<20.2f}")
            
            # Ukuran file
            size_you = os.path.getsize(image_path)
            size_comp = os.path.getsize(compare_image)
            print(f"      {'Ukuran File (bytes)':<20} {size_you:<20,} {size_comp:<20,}")
            
        else:
            print("   ⚠ Citra pembanding tidak dapat dibaca.")
    else:
        print("   ⚠ Tidak ada citra pembanding atau file tidak ditemukan.")
        print("   Untuk perbandingan, berikan parameter compare_image.")
    
    # ============= 8. RINGKASAN =============
    print("\n" + "="*60)
    print("✅ ANALISIS SELESAI")
    print("="*60)
    
    # Kumpulkan hasil dalam dictionary
    analysis_results = {
        'filename': os.path.basename(image_path),
        'dimensions': (w, h),
        'resolution': resolution,
        'channels': channels,
        'aspect_ratio': aspect_ratio,
        'aspect_ratio_type': ratio_type,
        'memory_rgb_bytes': mem_rgb,
        'memory_gray_bytes': mem_gray,
        'gray_stats': {
            'min': int(gray.min()),
            'max': int(gray.max()),
            'mean': float(gray.mean()),
            'std': float(gray.std()),
            'median': float(np.median(gray))
        }
    }
    
    return analysis_results

def download_sample_image():
    """Download sample image untuk perbandingan (jika dibutuhkan)"""
    import requests
    from io import BytesIO
    from PIL import Image
    
    url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        
        # Simpan sementara
        temp_path = "sample_lena.jpg"
        cv2.imwrite(temp_path, img_cv)
        print(f"✓ Sample image downloaded: {temp_path}")
        return temp_path
    except:
        print("⚠ Gagal download sample image.")
        return None

# ============= CONTOH PENGGUNAAN =============
if __name__ == "__main__":
    print("\n🔍 LATIHAN 1: ANALISIS CITRA PRIBADI")
    print("="*60)
    print("\nSilakan masukkan path file gambar Anda.")
    print("Contoh: C:/Users/Nama/Downloads/foto_saya.jpg")
    print("atau cukup tekan ENTER untuk menggunakan file default (foto_saya.jpg)\n")
    
    # Minta input path dari user
    user_path = r"C:\Users\Pongo\Desktop\kuliah\Semester 4\Pengolahan Citra Digital\minggu 1\src\img\kucing_rafi.jpeg"

    if not user_path:
        user_path = "foto_saya.jpg"
        print(f"   Menggunakan path default: {user_path}")
    
    # Opsi untuk menggunakan sample pembanding
    print("\n🔄 Gunakan citra pembanding?")
    print("   1. Ya, gunakan gambar sample Lena (otomatis download)")
    print("   2. Ya, gunakan file lain (masukkan path)")
    print("   3. Tidak, lewati perbandingan")
    pilihan = input("Pilihan (1/2/3) [default=1]: ").strip()
    
    compare_path = None
    if pilihan == '2':
        compare_path = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
    elif pilihan == '1' or pilihan == '':
        print("   Mendownload sample image Lena...")
        compare_path = download_sample_image()
    else:
        print("   Perbandingan dilewati.")
    
    # Jalankan analisis
    results = analyze_my_image(user_path, compare_image=compare_path)
    
    if results:
        print("\n📋 RINGKASAN HASIL :")
        for key, value in results.items():
            print(f"   {key}: {value}")
    
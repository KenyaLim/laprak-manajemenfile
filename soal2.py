import os

def tampilkan_soal(file_soal):
    if not os.path.exists(file_soal):
        print(f"File '{file_soal}' tidak ditemukan. Pastikan file berada di folder yang sama!")
        return

    try:
        with open(file_soal, 'r') as f:
            print(f"Nama file: {file_soal}")
            lines = f.readlines()
            
            for line in lines:
                if '||' in line:
                    soal, jawaban_benar = line.strip().split('||')
                    jawaban_user = input(f"{soal.strip()} Jawab: ").strip()
                    
                    if jawaban_user.lower() == jawaban_benar.strip().lower():
                        print("Jawaban benar!\n")
                    else:
                        print("Jawaban salah!\n")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

file_soal = "soal.txt"
tampilkan_soal(file_soal)

# Строки файлов
files_a_line = "data.db image.png log.txt"
files_b_line = "image.png script.py data.db"

files_A = set(files_a_line.split())
files_B = set(files_b_line.split())

common_files = files_A & files_B
lost_files = files_A - files_B

print("Общие:", ' '.join(sorted(common_files)))
print("Потерянные:", ' '.join(sorted(lost_files)))
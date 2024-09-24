import re
import subprocess

# Step 1: Read the file
file_path = r"C:\Users\ioung\AppData\Roaming\Rime\sync\19eeb228-5228-4410-ab6e-6f2d17805a9f\rime_ice.userdb.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Step 2: Extract Chinese words using regular expressions
chinese_words = re.findall(r'\t([\u4e00-\u9fff]+)', content)

# Step 3: Call run.py for TTS and save audio files
for word in chinese_words:
    # Call run.py with the Chinese word as input
    subprocess.run(['F:\pofice\ChatTTS\.venv\Scripts\python.exe', 'examples/cmd/run.py', word], check=True)
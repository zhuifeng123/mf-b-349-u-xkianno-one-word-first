import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write("luminous")
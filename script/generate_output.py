from datetime import datetime
import random
import os

os.makedirs("results", exist_ok=True)

now = datetime.utcnow().isoformat()
value = random.randint(1, 100000)
text = f"Hello Anthonia!\nTimestamp (UTC): {now}\nRandom value: {value}\n"

out_path = "results/output.txt"
with open(out_path, "w") as f:
    f.write(text)

print("Generated", out_path)
print("--- file contents ---")
print(text)

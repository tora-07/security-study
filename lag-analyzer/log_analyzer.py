success = 0
failed = 0
counts = {}

with open("auth.log") as f:
    for line in f:
        if "Accepted" in line:
            success += 1
        elif "Failed" in line:
            failed += 1
            parts = line.split()
            ip = parts[parts.index("from") + 1]
            if ip in counts:
                counts[ip] += 1
            else:
                counts[ip] = 1

print(f"ログイン成功:{success}回")
print(f"ログイン失敗:{failed}回")
print("・・・")

print("--- 失敗が多いIP TOP5 ---")
ranking = sorted(counts, key=counts.get, reverse=True)
for ip in ranking[:5]:
    print(f"{ip}: {counts[ip]}回")

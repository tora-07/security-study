import sys

if len(sys.argv) < 2:
    print("使い方:python3 log_analyzer.py ログファイル名")
    sys.exit()

filename = sys.argv[1]
THRESHOLD = 3

success = 0
failed = 0
counts = {}

with open(filename) as f:
    for line in f:
        if "Accepted" in line:
            success +=1
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
    if counts[ip] >= THRESHOLD:
        print(f"{ip}: {counts[ip]} 回 ⚠️ 要注意")
    else:
        print(f"{ip}: {counts[ip]} 回")

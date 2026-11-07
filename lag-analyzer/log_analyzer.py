uccess = 0
failed = 0
with open("auth.log") as f:
    for line in f:
        if "Accepted" in line:
            success +=1
        elif "Failed" in line:
            failed += 1
            parts = line.split()
            print(parts[parts.index("from") + 1])
print("・・・")
print(f"ログイン成功:{success}回")
print(f"ログイン失敗:{failed}回")

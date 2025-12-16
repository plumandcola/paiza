import requests, re, subprocess

# 幅
COL_WIDTH = 40

# パディング関数
def pad(s):
    if len(s) < COL_WIDTH:
        return s + " " * (COL_WIDTH - len(s))
    return s[:COL_WIDTH]

# ANSI colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

link = "" #ここに、paizaラーニングの問題の載っているURLを入れる
python_path = "main.py" #ここに、コードを書いたPythonファイルへのパスを入れる

res = requests.get(link)
#print(res.text)

for i in range(1, 10):
    found = re.search(rf"入力例{i}</dt>\n<dd>\n<p>(.*?)</p>", res.text)
    if found is None:
        continue

    input_i = found.group(1).replace("<br>", "\n")

    print(f"\n=== Sample Input {i} ===")
    print(input_i)

    result = subprocess.run(
        ["python3", python_path],
        input=input_i,
        text=True,
        capture_output=True
        )
    
    stdout = result.stdout
    stderr = result.stderr

    if result.returncode != 0:
        print(f"{RED}Runtime Error (exit code {result.returncode}){RESET}")
        print("\n--- 標準エラー出力 ---")
        print(f"{RED}{stderr.strip()}{RESET}")
        print("\n--- 標準出力 ---")
        print(stdout.strip())
        continue

    output_i = re.search(rf"出力例{i}</dt>\n<dd>\n<p>(.*?)</p>", res.text).group(1)

    # 行に分割
    expected_lines = output_i.split("<br>")
    result_lines = stdout.split("\n")

    #print(*result_lines, sep = "\n")

    # 行数を揃える
    max_len = max(len(expected_lines), len(result_lines))
    expected_lines += [""] * (max_len - len(expected_lines))
    result_lines += [""] * (max_len - len(result_lines))

    # ヘッダー
    print("   ", "|", f"Expected Output {i}".ljust(COL_WIDTH), "|", f"Your Output {i}")
    print("---", "+", "-" * COL_WIDTH, "+", "-" * COL_WIDTH)

    # 行ごとに比較して表示
    for j in range(max_len):
        e_pad = pad(expected_lines[j])
        r_pad = pad(result_lines[j])

        if expected_lines[j] == result_lines[j]:
            # 同じ行は緑
            print(f"{j+1:3} | {GREEN}{e_pad}{RESET} | {GREEN}{r_pad}{RESET}")
            continue
        else:
            # 異なる行は赤
            print(f"{j+1:3} | {RED}{e_pad}{RESET} | {RED}{r_pad}{RESET}")

# Security Study
サイバーセキュリティの学習記録

## 目標
2027年のボストンキャリアフォーラムでセキュリティ系インターンを獲得する

## ファイル構成
- linux-commands.md：Linuxコマンドの早見表
- bandit.md：OverTheWire Bandit の解き方メモ
- python/：Pythonの練習コードと作品

## 学習ログ
- 2026/10/30
  - GitHubを始めた
  - ターミナルとPythonの準備完了（Python 3.14.3）
  - Linuxの基本コマンドを練習した（pwd, ls, cd, mkdir, touch, echo, cat）
- 2026/10/31
  - Banditを始めた（Level 0〜4 クリア）
  - sshでサーバーにログインできた
  - `.` `..` `~` の意味、Tab補完を覚えた
  - 隠しファイル（ls -a）、file コマンド、ワイルドカード（*）を覚えた
- 2026/11/01
  - Bandit Level 5〜6 クリア
  - find（条件でファイルを探す）、man（説明書）を覚えた
  - エラーを消す 2>/dev/null を知った
  - 第1週の目標（Level 5）を前倒しで達成
- 2026/11/02
  - Bandit Level 7〜9 クリア
  - grep、sort、uniq、strings を覚えた
  - パイプ | でコマンドをつなぐ方法を覚えた
  - Pythonを始めた（print、変数、計算、f文字列）
  - 初めてのプログラム intro.py を作った
- 2026/11/03
  - Bandit Level 10〜12 クリア（Level 13 到達）
  - base64、ROT13（tr）、hexdump（xxd）、圧縮ファイルの解凍を学んだ
  - > でファイルを空にしてしまう失敗をして、原因を理解した
- 2026/11/07
  - Bandit Level 13 クリア（Level 14 到達）
  - 秘密鍵でのsshログイン、scp、chmod を覚えた
  - 鍵をコピペして壊してしまい、scp でファイルごと運ぶ方法で解決した

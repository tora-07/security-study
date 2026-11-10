# Log Analyzer

## Overview (English)
A Python tool that analyzes SSH authentication logs and detects possible brute-force attacks.
It counts successful and failed logins, ranks IP addresses by the number of failed attempts,
and flags suspicious IPs that exceed a threshold.

## 概要
sshのログイン記録（ログ）を読み込んで、総当たり攻撃をしている可能性のあるIPアドレスを見つけるツールです。
Bandit（Linux学習）で手作業でやっていた grep / sort / uniq の調査を、Pythonで自動化しました。

## できること
- ログイン成功・失敗の回数を数える
- 失敗したIPアドレスごとの回数を集計する
- 回数の多い順にTOP5を表示する
- 基準（THRESHOLD）以上失敗したIPに「要注意」をつける

## 使い方
python3 log_analyzer.py auth.log

## 実行例
ログイン成功:4回
ログイン失敗:14回
・・・
--- 失敗が多いIP TOP5 ---
203.0.113.55: 7回 ⚠️ 要注意
198.51.100.23: 4回 ⚠️ 要注意
203.0.113.8: 2回
192.0.2.10: 1回

※ auth.log は練習用の架空のログです（IPアドレスは説明用に予約された番号）

## 学んだこと・苦労したこと
- else で数えると関係ない行まで失敗に数えてしまうので、elif "Failed" に変えた
- IPアドレスは番号で決め打ちせず「from の次」で取り出すことで、ログの形が少し変わっても壊れないようにした
- 辞書のキーと値の関係、sorted の key= の意味を理解するのに時間がかかった

## 今後の改善
- 時間帯ごとの攻撃回数を集計する
- IPアドレスから国を調べる
- 来年作るハニーポットで集めた本物のログを分析する

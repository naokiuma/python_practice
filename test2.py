import os
import csv

desktop_dir = os.path.expanduser('~/Desktop')
ref = os.path.join(desktop_dir,"パイソン練習フォルダ","test.py")

# rだと読み込み。
# st = open(ref,"w")
# st.write("追加書き込み")
# st.close()

text = input('入力してください。')

# 自動で閉じる場合はwithを使う。
# また日本語が含む可能性があるならデフォルトでエンコーディングは書いておこう。
with open(ref,"w",encoding="utf-8") as f:
    f.write(text)



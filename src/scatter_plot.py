import matplotlib.pyplot as plt
import japanize_matplotlib

# 任意に指定する標準偏差のリスト
gyro_stds = [
# 極小平均
-0.38,
3.31,
4.28,
6.32,
7.19,
19.03,
# 0.23,
23.43,
29.8,
7.79,
15.4,
13.79,
14.03,
7.06,
23.48,
23.98,
21.39

# 角度範囲
# 60.35,
# 51.01,
# 52.63,
# 42.79,
# 59.84,
# 54.67,
# 54.94,
# 56.24,
# 57.8,
# 56.45,
# 56.59,
# 57.19,
# 59.72,
# 43.09,
# 43.19,
# 47.24,




# 58.27,
# 49.77,
# 51.06,
# 41.59,
# 58.52,
# 54.21,
# 53.72,
# 54.13,
# 60.85,
# 55.78,
# 55.32,
# 56.03,
# 57.13,
# 43.25,
# 43.19,
# 46.12,

# # 極小分散
# 19.49,
# 10.52,
# 17.52,
# 13.24,
# 5.47,
# None,
# 0.73,
# 2.82,
# 2.85,
# 5.92,
# 1.1,
# 5.58,
# 16.05,
# 23.46,
# None,
# 13.78,
# 1.42,
# 24.18,
# 12.88,
# 29.45,
# 36.89,
# 0.84,
# 7.84,
# 0.77,
# 38.22,
# 29.56,
# 22.97,
# 6.75,
# 7.95,
# 38.61,

# # 極小標準
# 4.42,
# 3.24,
# 4.19,
# 3.64,
# 2.34,
# None,
# 0.86,
# 1.68,
# 1.69,
# 2.43,
# 1.05,
# 2.36,
# 4.01,
# 4.84,
# None,
# 3.71,
# 1.19,
# 4.92,
# 3.59,
# 5.43,
# 6.07,
# 0.91,
# 2.8,
# 0.88,
# 6.18,
# 5.44,
# 4.79,
# 2.6,
# 2.82,
# 6.21,

# # 極大平均
# 56.34,
# 52.68,
# 44.11,
# 47.78,
# 36.66,
# None,
# 45.86,
# 51.52,
# 46.34,
# 44.65,
# 44.58,
# 58.91,
# 58.63,
# 67.39,
# None,
# 58.4,
# 50.44,
# 52.23,
# 56.19,
# 51.44,
# 44.82,
# 49.99,
# 50.38,
# 52.82,
# 72.7,
# 63.49,
# 55.59,
# 64.02,
# 62.41,
# 61.27,


# # 差の平均
# 50.06,
# 50.25,
# 49.72,
# 49.71,
# 39.79,
# None,
# 38.16,
# 42.75,
# 39.89,
# 45.32,
# 39.23,
# 50.9,
# 50.55,
# 48.15,
# None,
# 46.79,
# 46.17,
# 45.62,
# 44.22,
# 53.81,
# 52.71,
# 55.03,
# 52.55,
# 53.86,
# 49.49,
# 49.83,
# 49.53,
# 47.94,
# 49.01,
# 49.18,

# # 差の分散
# 11,
# 2.12,
# 22.03,
# 5.98,
# 1.49,
# None,
# 15.9,
# 4.99,
# 2.29,
# 4.94,
# 2.69,
# 9.73,
# 6.66,
# 13.48,
# None,
# 7.38,
# 1.71,
# 7.1,
# 21.92,
# 46.77,
# 46.68,
# 4.05,
# 3.19,
# 0.58,
# 14.71,
# 3.52,
# 6.99,
# 25.72,
# 10.18,
# 11.94,

# # 差の標準偏差
# 3.32,
# 1.46,
# 4.69,
# 2.45,
# 1.22,
# None,
# 3.99,
# 2.23,
# 1.51,
# 2.22,
# 1.64,
# 3.12,
# 2.58,
# 3.67,
# None,
# 2.72,
# 1.31,
# 2.66,
# 4.68,
# 6.84,
# 6.83,
# 2.01,
# 1.79,
# 0.76,
# 3.84,
# 1.87,
# 2.64,
# 5.07,
# 3.19,
# 3.46,

# # 平均-平均
# 50.88,
# 51.05,
# 49.63,
# 50.38,
# 39.97,
# None,
# 38.3,
# 43.06,
# 40.07,
# 43.35,
# 39.09,
# 51.33,
# 50.51,
# 48.15,
# None,
# 46.77,
# 46.33,
# 44.23,
# 44.17,
# 53.76,
# 50.33,
# 55.37,
# 52.62,
# 54.18,
# 50.36,
# 50.59,
# 50.35,
# 47.66,
# 49.81,
# 49.45,
]
# _________________________________________________
linear_acc_stds = [
# # 極大平均
58.27,
49.77,
51.06,
41.59,
58.52,
54.21,
53.72,
54.13,
60.85,
55.78,
55.32,
56.03,
57.13,
43.25,
43.19,
46.12,
# 極大値分散

# 28.43,
# 10.63,
# 17.81,
# 23.88,
# 7.83,
# None,
# 13.57,
# 3.08,
# 3.41,
# 35.15,
# 4.68,
# 5.06,
# 7.97,
# 27.46,
# None,
# 6.05,
# 1.35,
# 23.99,
# 14.28,
# 9.69,
# 56.4,
# 2.89,
# 1.24,
# 1.18,
# 81.29,
# 35.83,
# 12.33,
# 39.34,
# 21.75,
# 19.03,
# # 極大標準
# 5.33,
# 3.26,
# 4.22,
# 4.89,
# 2.8,
# None,
# 3.68,
# 1.76,
# 1.85,
# 5.93,
# 2.16,
# 2.25,
# 2.82,
# 5.24,
# None,
# 2.46,
# 1.16,
# 4.9,
# 3.78,
# 3.11,
# 7.51,
# 1.7,
# 1.11,
# 1.09,
# 9.02,
# 5.99,
# 3.51,
# 6.27,
# 4.66,
# 4.36,
]
# 点数のリスト (任意に指定)
scores = [
####上下のブレ
45.84545494,
8.58555277,
8.798692199,
6.643495613,
20.58588754,
48.49711639,
7.798411477,
23.12751327,
19.12937719,
8.471393072,
23.05695406,
17.89146606,
51.30974603,
6.757804107,
22.046786,
5.772659007
]

# 散布図を作成
fig, ax = plt.subplots(figsize=(8, 6))  # 1つのサブプロットを作成

# ジャイロセンサの標準偏差と点数の散布図
ax.scatter(gyro_stds, scores)
for i, (x, y) in enumerate(zip(gyro_stds, scores), start=1):
    if x is not None and y is not None:  # Noneでないデータのみ表示
        ax.text(x, y, f'{i}', fontsize=10, ha='center', va='bottom')
ax.set_xlabel('角度(度数)', fontsize=20)
ax.set_ylabel('上下のブレ', fontsize=20)
# ax.set_title('前後のブレと足の角度の範囲', fontsize=20)
ax.grid()
ax.tick_params(axis='both', labelsize=20)  # メモリの文字サイズを設定

plt.tight_layout()
plt.show()

# # 線形加速度センサの標準偏差と点数の散布図
# axes[1].scatter(linear_acc_stds, scores)
# for i, (x, y) in enumerate(zip(linear_acc_stds, scores), start=1):
#     if x is not None and y is not None:  # Noneでないデータのみ表示
#         axes[1].text(x, y, f'{i}', fontsize=10, ha='center', va='bottom')
# axes[1].set_xlabel('山の振幅の標準偏差' ,fontsize=20)
# axes[1].set_ylabel('アンケートによる点数',fontsize=20)
# axes[1].set_title('振幅の標準偏差とアンケート点数の散布図',fontsize=20)
# axes[1].tick_params(axis='both', labelsize=25)  # メモリの文字サイズを設定
# axes[1].grid()

plt.tight_layout()
plt.show()

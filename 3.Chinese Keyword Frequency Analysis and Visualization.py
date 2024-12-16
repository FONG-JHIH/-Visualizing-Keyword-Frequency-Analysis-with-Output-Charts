# -*- coding: utf-8 -*-
"""
此作品分析了文本資料中的關鍵詞語，透過數據清理、頻率統計及可視化技術，
深度挖掘消費者需求與市場趨勢，並以條形圖、詞雲圖、累積分布圖等六種圖表形象化展示結果，
為產品設計與行銷策略提供依據。
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.font_manager as fm

# 中文的基本設定（影響全局字體顯示）
plt.rcParams['font.family'] = 'Microsoft YaHei'  # 設定字體為 'Microsoft YaHei'
plt.rcParams['font.size'] = 12  # 設定字體大小為 12

# 指定特定字體的設定（適用於指定元素）
font_path = 'C:\\Windows\\Fonts\\msjhl.ttc'  # 指定標楷體字體文件的路徑
font_prop = fm.FontProperties(fname=font_path)
font_prop.set_style('normal')  # 設定字體樣式為正常
font_prop.set_size(12)  # 設定字體大小

# 讀取資料
keywords_data = pd.read_csv('關鍵詞詞頻分析.csv', encoding='utf-8-sig')

# 選取分析的關鍵詞
keywords_to_analyze = [
    "手術", "眼鏡", "眼睛", "戴", "雷射", "近視", "時間", "眼科", "檢查", "感覺", 
    "光度", "散光", "舒服", "推薦", "清楚", "乾眼", "遠視度數", "大學", "顏色", 
    "炫光", "模糊", "乾澀", "運動", "棕色", "驗光", "適應", "蔡司", "藥水", "感染", 
    "異物感", "清潔", "消毒", "漂亮", "含水量", "海昌", "購買", "寶島", "游泳"
]

# 篩選資料
filtered_data = keywords_data[keywords_data['關鍵詞語'].isin(keywords_to_analyze)]

# --- 條形圖（Bar Chart） ---
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_data, x='出現次數', y='關鍵詞語', palette='viridis')
plt.title('關鍵詞語出現次數 - 條形圖', fontproperties=font_prop)
plt.xlabel('出現次數', fontproperties=font_prop)
plt.ylabel('關鍵詞語', fontproperties=font_prop)
plt.tight_layout()
plt.savefig('Bar Chart條形圖.png')
plt.show()

# --- 詞雲圖（Word Cloud） ---
wordcloud = WordCloud(font_path=font_path, background_color='white', width=800, height=400)
word_freq = dict(zip(filtered_data['關鍵詞語'], filtered_data['出現次數']))
wordcloud.generate_from_frequencies(word_freq)
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('關鍵詞語出現次數 - 詞雲圖', fontproperties=font_prop)
plt.savefig('Word Cloud詞雲圖.png')
plt.show()

# --- 累積分布圖（Cumulative Distribution Chart） ---
filtered_data_sorted = filtered_data.sort_values(by='出現次數', ascending=False)
filtered_data_sorted['累積次數'] = filtered_data_sorted['出現次數'].cumsum()
filtered_data_sorted['累積百分比'] = (filtered_data_sorted['累積次數'] / filtered_data_sorted['出現次數'].sum()) * 100

plt.figure(figsize=(10, 6))
plt.plot(filtered_data_sorted['關鍵詞語'], filtered_data_sorted['累積百分比'], marker='o')
plt.xticks(rotation=45, fontproperties=font_prop)
plt.title('關鍵詞語累積百分比 - 累積分布圖', fontproperties=font_prop)
plt.xlabel('關鍵詞語', fontproperties=font_prop)
plt.ylabel('累積百分比 (%)', fontproperties=font_prop)
plt.tight_layout()
plt.savefig('Cumulative Distribution Chart累積分布圖.png')
plt.show()

# 繪製柱狀堆積圖（Stacked Bar Chart）
# 模擬類別數據（假設部分關鍵詞屬於不同類別）
categories = ["功能", "健康", "視覺", "品牌", "其他"]
filtered_data['類別'] = [categories[i % len(categories)] for i in range(len(filtered_data))]

stacked_data = filtered_data.pivot(index='關鍵詞語', columns='類別', values='出現次數').fillna(0)
stacked_data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('關鍵詞語分類堆積圖', fontsize=14)
plt.xlabel('關鍵詞語', fontsize=12)
plt.ylabel('出現次數', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('stacked_bar_chart關鍵詞語分類堆積圖.png')
plt.show()

# 繪製熱力圖（Heatmap）
plt.figure(figsize=(10, 6))
sns.heatmap(stacked_data, annot=True, fmt='.0f', cmap='YlGnBu', linewidths=.5)
plt.title('關鍵詞語熱力圖', fontsize=14)
plt.xlabel('類別', fontsize=12)
plt.ylabel('關鍵詞語', fontsize=12)
plt.tight_layout()
plt.savefig('heatmap關鍵詞語熱力圖.png')
plt.show()

# 繪製長尾圖（Long Tail Graph）
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['關鍵詞語'], filtered_data['出現次數'], marker='o', linestyle='-', color='g')
plt.title('關鍵詞語長尾圖', fontsize=14)
plt.xlabel('關鍵詞語（按次數降序排列）', fontsize=12)
plt.ylabel('出現次數', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yscale('log')  # 使用對數刻度顯示長尾效應
plt.tight_layout()
plt.savefig('long_tail_graph關鍵詞語長尾圖.png')
plt.show()

print("所有圖表已生成並保存！")
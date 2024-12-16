# 3.Chinese Keyword Frequency Analysis and Visualization
# Project Overview
This project focuses on analyzing Chinese text keywords using data cleaning, frequency statistics, and various visualization techniques. The program visualizes the distribution of high-frequency keywords in textual data and provides actionable insights for product design, marketing strategies, and user demand analysis.
# Key Features
1. Data Cleaning and Keyword Analysis
•	Stopword Filtering: Removes meaningless words using a predefined stopword list (customizable).
•	Data Processing: Cleans repetitive characters and irrelevant symbols to ensure data accuracy.
•	High-Frequency Keyword Statistics: Extracts core keywords using the TF-IDF algorithm.
2. Multi-Dimensional Data Visualization
•	Bar Chart: Displays the frequency of high-frequency keywords, revealing consumer hotspots.
•	Word Cloud: Visualizes popular keywords with font size indicating frequency.
•	Cumulative Distribution Chart: Shows the cumulative keyword distribution, adhering to the Pareto principle (80/20 rule).
•	Stacked Bar Chart: Highlights the proportion of keywords across different categories (e.g., functionality, brand, health).
•	Heatmap: Depicts the intensity distribution of keywords across categories.
•	Long Tail Graph: Displays the long-tail effect of keyword frequency, reflecting niche demands.
# How to Use
1.	Prepare the Dataset
o	Ensure the input file keyword_frequency_analysis.csv is loaded with the following columns:
	Keyword: Textual keywords.
	Frequency: Occurrence frequency of each keyword.
2.	Run the Program
o	Execute the Python script and ensure the following dependencies are installed:
	pandas
	matplotlib
	wordcloud
	seaborn
3.	Generated Visualizations
o	The program will automatically save the following visualizations as PNG files:
	Bar Chart: Bar Chart條形圖.png
	Word Cloud: Word Cloud詞雲圖.png
	Cumulative Distribution Chart: Cumulative Distribution Chart累積分布圖.png
	Stacked Bar Chart: stacked_bar_chart關鍵詞語分類堆積圖.png
	Heatmap: heatmap關鍵詞語熱力圖.png
	Long Tail Graph: long_tail_graph關鍵詞語長尾圖.png
# Program Structure
•	Data Cleaning and Processing
o	Loads the stopword list and removes irrelevant characters.
o	Structures textual data into an analyzable format.
•	Keyword Statistics
o	Extracts high-frequency keywords using the TF-IDF algorithm.
o	Conducts keyword frequency analysis and outputs results as a CSV file.
•	Data Visualization
o	Bar Chart: Illustrates the frequency distribution of high-frequency keywords.
o	Word Cloud: Provides an intuitive overview of popular keywords.
o	Long Tail Graph: Highlights the market value of low-frequency keywords.
# Applicable Scenarios
1.	Market Demand Analysis: Identifies user needs to assist in product development and marketing strategies.
2.	Text Topic Mining: Suitable for topic analysis in social media, reviews, and other textual data.
3.	User Behavior Research: Discovers potential user behavior patterns through keyword analysis.
# Recommendations for Results Application
1.	Focus on High-Frequency Keywords: Optimize product designs and marketing strategies around core needs such as "surgery," "glasses," and "comfort."
2.	Explore Niche Demands: Address the specific needs represented by long-tail keywords to expand into segmented markets.
3.	Leverage Visualization Insights: Use visualized results to enhance internal decision-making efficiency and improve stakeholder communication.
This project offers a comprehensive view of consumer needs through analysis and visualization. By combining market demand characteristics, it provides businesses with actionable data support for strategic planning and implementation.

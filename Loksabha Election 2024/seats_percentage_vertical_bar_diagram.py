import matplotlib.pyplot as plt

# Data for Vote Share in the 2024 Election
parties = [
    'BJP', 'INC', 'SP', 'AITC', 'YSRCP', 'BSP',
    'TDP', 'DMK', 'CPI(M)', 'RJD', 'Others'
]
vote_shares = [
    36.56, 21.96, 4.58, 4.37, 2.06, 2.04,
    1.98, 1.82, 1.76, 1.57, 21.3
]

# Colors for the bars (using unique colors for each party)
colors = [
    '#FF9933', '#00ADEF', '#007FFF', '#006400', '#FFD700', '#800080',
    '#FFA500', '#FF0000', '#808080', '#008000', '#D3D3D3'
]

# Plotting the bar chart
plt.figure(figsize=(12, 8))
bars = plt.bar(parties, vote_shares, color=colors)
plt.title('Vote Share Percentage of Parties in the 2024 Election')
plt.xlabel('Party')
plt.ylabel('Vote Share Percentage')
plt.xticks(rotation=45, ha='right')

# Adding vote share percentages above the bars
for bar, share in zip(bars, vote_shares):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{share:.2f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()

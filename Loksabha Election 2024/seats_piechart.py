import matplotlib.pyplot as plt

# Data
parties = [
    'BJP', 'INC', 'SP', 'AITC', 'DMK', 'TDP',
    'JD(U)', 'SHSUBT', 'NCPSP', 'SHS', 'Others'
]
seats = [
    240, 99, 37, 29, 22, 16,
    12, 9, 8, 7, 543 - (240 + 99 + 37 + 29 + 22 + 16 + 12 + 9 + 8 + 7)
]

# Colors for each party (using their official colors)
colors = [
    '#FF9933', '#00ADEF', '#007FFF', '#006400', '#FF0000', '#FFD700',
    '#808000', '#FFC0CB', '#800080', '#808080', '#D3D3D3'
]

# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(seats, colors=colors, startangle=90, counterclock=False)

# Adding a legend at the bottom with party names and seat numbers
labels = [f'{party} - {seat} seats' for party, seat in zip(parties, seats)]
plt.legend(labels, loc='upper a', bbox_to_anchor=(0.5, -0.05), ncol=3)

# Adding title
plt.title('Distribution of Seats in the Election (543 Total Seats)')

# Display the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


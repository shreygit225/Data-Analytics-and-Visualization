import matplotlib.pyplot as plt

# Data
parties = [
    'BJP', 'INC', 'SP', 'AITC', 'DMK', 'TDP',
    'JD(U)', 'SS(UBT)', 'NCP(SP)', 'SS', 'Other'
]
seat_shares = [
    44.20, 18.24, 6.82, 5.35, 4.06, 2.21,
    2.95, 1.66, 1.48, 1.29, 11.74
]

# Colors for each party (using their official colors)
colors = [
    '#FF9933', '#00ADEF', '#007FFF', '#006400', '#FF0000', '#FFD700',
    '#808000', '#FFC0CB', '#800080', '#808080', '#D3D3D3'
]

# Plotting the pie chart
plt.figure(figsize=(10, 7))
wedges, _ = plt.pie(seat_shares, labels=None, colors=colors, startangle=90, counterclock=False, autopct=None)

# Adding title
plt.title('Seat Share Percentage of Parties in the Election')

# Removing text from inside pie
for wedge in wedges:
    wedge.set_label('')

# Adding legend at the bottom
legend_labels = [f'{party} - {seat} seats' for party, seat in zip(parties, seat_shares)]
plt.legend(legend_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

# Display the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

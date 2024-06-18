import matplotlib.pyplot as plt

# Data for Seat Share
parties = [
    'BJP', 'INC', 'SP', 'AITC', 'DMK', 'TDP',
    'JD(U)', 'SHSUBT', 'NCPSP', 'SHS', 'Others'
]
seats_won = [
    240, 99, 37, 29, 22, 16,
    12, 9, 8, 7, 0   # Setting Others to 0 initially
]

# Calculate remaining seats
remaining_seats = 543 - sum(seats_won)
seats_won[-1] = remaining_seats

# Colors for the bars
colors = [
    '#FF9933', '#00ADEF', '#007FFF', '#006400', '#FF0000', '#FFD700',
    '#808000', '#FFC0CB', '#800080', '#808080', '#D3D3D3'
]

# Plotting the bar chart
plt.figure(figsize=(12, 8))
bars = plt.bar(parties, seats_won, color=colors)
plt.title('Seats Won by Each Party in the 2024 Election')
plt.xlabel('Party')
plt.ylabel('Number of Seats')
plt.xticks(rotation=45, ha='right')

# Adding seat numbers above the bars
for bar, seat in zip(bars, seats_won):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, str(seat), ha='center', va='bottom')

plt.tight_layout()
plt.show()

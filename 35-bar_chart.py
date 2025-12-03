import matplotlib.pyplot as plt

Months = ['January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November"]
Metro_ridership = [86.99, 86.65, 92.10, 87.59, 89.09, 92.19, 103.70, 99.07, 101.46, 93.27, 92.86]

plt.figure(figsize=(12, 6))  # (width, height) in inches
bars = plt.bar(Months, Metro_ridership, color='lightgreen', width=0.5)
plt.bar_label(bars, fmt='%.2f', rotation=90, fontweight='bold', padding=3, label_type='center')
# plt.bar_label(bars, label_type='center', fmt='%.2f')
plt.title(" Chennai Metro Ridership")
plt.ylabel("Metro Riders [in lakhs]")
plt.xlabel("Months - 2025")
plt.show()
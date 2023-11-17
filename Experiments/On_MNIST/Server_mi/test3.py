import matplotlib.pyplot as plt
import numpy as np

# Define the function to plot
def iv_curve(order, voltage):
    return (voltage ** order) / (1 + voltage ** order)

# Create the voltage range
voltage = np.linspace(0.8, 1.2, 100)



# Adjusting the plot to have all markers in black and hollow

# Clearing the previous plot
plt.clf()

# Define line styles, with all markers in black and hollow for each order
line_styles = {
    10: {'color': 'k', 'linestyle': '-', 'marker': 'o', 'markersize': 7, 'markerfacecolor': 'none', 'markeredgecolor': 'k'},
    20: {'color': 'r', 'linestyle': '--', 'marker': 's', 'markersize': 7, 'markerfacecolor': 'none', 'markeredgecolor': 'k'},
    40: {'color': 'b', 'linestyle': ':', 'marker': '^', 'markersize': 7, 'markerfacecolor': 'none', 'markeredgecolor': 'k'},
    100: {'color': 'g', 'linestyle': '-.', 'marker': 'D', 'markersize': 7, 'markerfacecolor': 'none', 'markeredgecolor': 'k'}
}

# Plot each curve with the specified line style and marker
for order, style_dict in line_styles.items():
    current = iv_curve(order, voltage)
    plt.plot(voltage, current, **style_dict, markevery=5, label=f'Order {order}')

# Customizing the plot to match the given style
plt.xlabel('Voltage (mV)')
plt.ylabel('Current (μA)')
plt.title('The science + ieee styles for IEEE papers:')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

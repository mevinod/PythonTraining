import numpy as np
import matplotlib.pyplot as plt


labels = 'BDC', 'MDC'
sizes = [70, 30]
color = ['Green', 'Red']
plt.pie(x=sizes, labels=labels, colors=color)
plt.show()


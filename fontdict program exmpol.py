import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [2100, 2255, 2300, 2400, 2500]
}

df = pd.DataFrame(data)

df.plot(kind="line", x="Month", y="Sales", marker="o")

plt.title("Monthly Sales Growth", fontdict={'family': 'serif', 'color': 'darkblue', 'size': 18, 'weight': 'bold'})
plt.xlabel("Month", fontdict={'family': 'monospace', 'color': 'green', 'size': 12})
plt.ylabel("Sales", fontdict={'family': 'monospace', 'color': 'red', 'size': 12})
plt.grid(True)
plt.show()

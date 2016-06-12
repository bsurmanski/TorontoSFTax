import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import tax

t = range(0, 300000, 100)
plt.title('Tax Toronto vs SF')
plt.xlabel('$Earned')
plt.ylabel('$Tax')
to_tax = plt.plot(t, [tax.TorontoTax(v) for v in t], 'r', label='Toronto')
sf_tax = plt.plot(t, [tax.SFTax(v) for v in t], 'b', label='SF')
plt.legend()
plt.show()

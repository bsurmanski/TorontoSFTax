import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import tax

fig, ax = plt.subplots()
ax.grid(True)
t = range(0, 300000, 100)
plt.xticks(range(0, 300000, 20000))
plt.yticks(range(0, 300000, 20000))
plt.title('Tax Toronto vs SF')
plt.xlabel('$Earned')
plt.ylabel('$Tax')
to_tax = plt.plot(t, [tax.TorontoTax(v) for v in t], 'b', label='Toronto')
sf_tax = plt.plot(t, [tax.SFTax(v) for v in t], 'm', label='SF')
mtl_tax = plt.plot(t, [tax.MontrealTax(v) for v in t], 'r', label='Montreal')
van_tax = plt.plot(t, [tax.VancouverTax(v) for v in t], 'g', label='Vancouver')
van_tax = plt.plot(t, [tax.SeattleTax(v) for v in t], 'y', label='Seattle')
plt.legend(loc=4)
plt.show()

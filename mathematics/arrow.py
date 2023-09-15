import matplotlib.pyplot as plt

x= plt.xlim(0,10)
y= plt.ylim(0,10)


plt.arrow(0,0,3, 2, head_width=0.1, head_length=0.1, color="blue")
plt.arrow(0,0,2, 3, head_width=0.1, head_length=0.1, color="blue")
plt.arrow(3,2,5, 3, head_width=0.1, head_length=0.1, color="blue")
plt.arrow(2,3,6, 2, head_width=0.1, head_length=0.1, color="blue")
plt.show()
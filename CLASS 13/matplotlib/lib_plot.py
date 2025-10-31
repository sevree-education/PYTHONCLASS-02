import matplotlib.pyplot as plt


names = ["oussama", "hichem", "sofiane", "hiba"]
averages = [12, 14, 15, 19]

#a simple line plot:
plt.plot(names, averages) # x axis labels, y axis labels
plt.title("STUDENT AVERAGES")
plt.xlabel("STUDENTS")
plt.ylabel("AVERAGES")
plt.ylim(0,20) #set y-axis range
plt.grid(True)
plt.savefig("./CLASS 13/matplotlib/averagesline.png", dpi = 150)
plt.close()
#plt.show() #display the plot

#a bar char:
plt.bar(names, averages)
plt.title("STUDENT AVERAGES")
plt.xlabel("STUDENTS")
plt.ylabel("AVERAGES")
plt.ylim(0,20) #set y-axis range
plt.tight_layout()
#plt.show()
plt.savefig("./CLASS 13/matplotlib/averagesbar.png", dpi = 150)
plt.close()
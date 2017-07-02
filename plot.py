import matplotlib
import xlrd
import numpy as np
import test
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

#from peakdetect import peakdetect

def to_percent(y, position):
    return position*5


workbook = xlrd.open_workbook("filelocation.xlsx")
sheet = workbook.sheet_by_index(0)
x_label = ""
y_lable = ""
x = []
y = []
for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        if rowx == 0:
                x_label = cols[0]
                y_lable = cols[1]
                continue
        #print str(rowx) + ":" + str(cols)
        x.append(cols[0])
        y.append(cols[1])
        # if rowx == 500:
        #        break

print "X MAX: " + str(max(x)) + " MIN " + str(min(x))
print "Y MAX: " + str(max(y)) + " MIN " + str(min(y))
print "%d" , (max(y)-min(y))/100

#Plotting to our canvas
fs = 20
# plt.figure(figsize=(9.42, 6.06))
plt.figure()
ax1 = plt.axes()

plt.plot(x, y, color="black")
plt.title('Title', fontsize=fs)
plt.xlabel("m/z", fontsize=10)
plt.ylabel("Relative Abundance", fontsize=10)

major_ticks = np.arange(0, 2000, 100)
minor_ticks = np.arange(0, 2000, 10)
ax1.set_xticks(major_ticks)
ax1.set_xticks(minor_ticks, minor=True)

#major_ticks = np.arange(0, 20001, 1000)
#minor_ticks = np.arange(0, 20001, 200)
major_ticks = np.arange(min(y), max(y)+1, (max(y)-min(y))/20)
minor_ticks = np.arange(min(y), max(y)+1, (max(y)-min(y))/100)

ax1.set_yticks(major_ticks)
ax1.set_yticks(minor_ticks, minor=True)


ax1.set_xlim(xmin=min(x), xmax=max(x))
ax1.set_ylim(ymin=min(y), ymax=max(y))
ax1.set_axisbelow(True)

formatter = FuncFormatter(to_percent)

# Set the formatter
plt.gca().yaxis.set_major_formatter(formatter)
# x, y ticks show out
plt.gca().get_yaxis().set_tick_params(which='both', direction='out' , labelsize=6, pad=0)
plt.gca().get_xaxis().set_tick_params(which='both', direction='out', labelsize=6, pad=0)
# hide ticks
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# hide border
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# ax1.spines['bottom'].set_visible(False)
# ax1.spines['left'].set_visible(False)
# ax1.set_xlim(xmax=1900)
# ax1.set_yticks(major_ticks)
# ax1.set_yticks(minor_ticks, minor=True)

maxtab, mintab = test.peakdet(y, 8000)
#print maxtab
print maxtab[0]
for i in maxtab:
        ax1.annotate("%.2f" % x[int(i[0])], xy=(x[int(i[0])], y[int(i[0])]), ha = 'center', fontsize=8 )#,weight="bold"ha='center',
        #print x[int(i[0])]
print len(maxtab)
plt.savefig('foo.png', bbox_inches='tight')
# plt.show()
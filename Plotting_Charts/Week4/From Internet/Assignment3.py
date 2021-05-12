import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import matplotlib.colors as col
import matplotlib.cm as cm

%matplotlib notebook

# Use the following data for this assignment:
np.random.seed(12345)

df = pd.DataFrame([
    np.random.normal(32000, 200000, 3650),
    np.random.normal(43000, 100000, 3650),
    np.random.normal(43500, 140000, 3650),
    np.random.normal(48000, 70000, 3650)
],
                  index=[1992, 1993, 1994, 1995])

# Get the means and standard deviations
df_mean = df.mean(axis=1)
df_std = df.std(axis=1)

n = df.shape[1]

# y default
mean = np.mean(df_mean.values)
y = mean

# Compute the 95% confidence intervals
yerr = df_std / np.sqrt(n) * st.norm.ppf(1 - 0.05 / 2)
conf_ints = [
    st.norm.interval(alpha=0.95, loc=mu, scale=se)
    for mu, se in zip(df_mean, df_std / np.sqrt(n))
]


# Compute the probablility of the mean > y for each column
def compute_probs(y, conf_int):
    if y < np.min(conf_int):
        result = 1.0
    elif y > np.max(conf_int):
        result = 0.0
    else:
        result = (np.max(conf_int) - y) / (np.max(conf_int) - np.min(conf_int))
    return result


# Compute probabilities
probs = [compute_probs(y, ci) for ci in conf_ints]

# Setup the colormap
cc = ['seismic', 'bwr', 'coolwarm']
cmap = cm.get_cmap(cc[2])
cpick = cm.ScalarMappable(cmap=cmap, norm=col.Normalize(vmin=0, vmax=1.0))
cpick.set_array([])

# Setup the plot
plt.figure()
bars = plt.bar(range(len(df)),
               df_mean,
#                width=1,
               edgecolor='gray',
               yerr=yerr,
               alpha=0.8,
               color=cpick.to_rgba(probs),
               capsize=7)

# Add the colorbar
cbar = plt.colorbar(cpick, orientation="vertical")  # "horizontal"

# Turn off some plot rectangle spines
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]

# Add the horizontal line
hoz_line = plt.axhline(y=y, color='gray', linewidth=1, linestyle='--')

# Set ticks and labels
plt.title('Even Harder: interactive y axis')

plt.xlabel('Year')
plt.ylabel('Value')

plt.xticks(range(len(df)), df.index)
yt_o = plt.gca().get_yticks()
yt = np.append(yt_o, y)
plt.gca().set_yticks(yt)
y_text = plt.text(1.5, 55000, 'y = %d' % y, bbox=dict(fc='white', ec='k'))


# Add interactivity
def onclick(event):
    y = event.ydata
    hoz_line.set_ydata(event.ydata)
    yt = np.append(yt_o, y)
    plt.gca().set_yticks(yt)
    y_text = plt.text(1.5, 55000, 'y = %d' % y, bbox=dict(fc='white', ec='k'))

    probs = [compute_probs(y, ci) for ci in conf_ints]
    for i in range(len(df)):
        bars[i].set_color(cpick.to_rgba(probs[i]))
        bars[i].set_edgecolor('gray')


plt.gcf().canvas.mpl_connect('button_press_event', onclick)


#HARDEST
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import matplotlib.colors as col
import matplotlib.cm as cm

%matplotlib notebook

# Use the following data for this assignment:
np.random.seed(12345)

df = pd.DataFrame([
    np.random.normal(32000, 200000, 3650),
    np.random.normal(43000, 100000, 3650),
    np.random.normal(43500, 140000, 3650),
    np.random.normal(48000, 70000, 3650)
],
                  index=[1992, 1993, 1994, 1995])

# Get the means and standard deviations
df_mean = df.mean(axis=1)
df_std = df.std(axis=1)

n = df.shape[1]

# y default
mean = np.mean(df_mean.values)
yu = mean + 5000
yd = mean - 5000
ys = [yu, yd]

# Compute the 95% confidence intervals
yerr = df_std / np.sqrt(n) * st.norm.ppf(1 - 0.05 / 2)
conf_ints = [
    st.norm.interval(alpha=0.95, loc=mu, scale=se)
    for mu, se in zip(df_mean, df_std / np.sqrt(n))
]


# Compute the probablility in the y-range for each column
def compute_probs(ys, conf_int):
    yu = max(ys)
    yd = min(ys)
    if yd <= np.min(conf_int) and yu >= np.max(conf_int):
        result = 1.0
    elif yu <= np.min(conf_int) or yd >= np.max(conf_int):
        result = 0.0
    elif yu >= np.max(conf_int):
        result = (np.max(conf_int) - yd) / (np.max(conf_int) -
                                            np.min(conf_int))
    else:
        result = (yu - np.min(conf_int)) / (np.max(conf_int) -
                                            np.min(conf_int))
    return result


# Compute probabilities
probs = [compute_probs(ys, ci) for ci in conf_ints]

# Setup the colormap
cc = ['seismic', 'bwr', 'coolwarm']
cmap = cm.get_cmap('OrRd')
cpick = cm.ScalarMappable(cmap=cmap, norm=col.Normalize(vmin=0, vmax=1.0))
cpick.set_array([])

# Setup the plot
plt.figure()
bars = plt.bar(range(len(df)),
               df_mean,
#                width=1,
               edgecolor='gray',
               yerr=yerr,
               alpha=0.8,
               color=cpick.to_rgba(probs),
               capsize=7)

# Add the colorbar
cbar = plt.colorbar(cpick, orientation="vertical")  # "horizontal"

# Turn off some plot rectangle spines
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]

# Add the horizontal line
hoz_line_u = plt.axhline(y=yu, color='gray', linewidth=1, linestyle='--')
hoz_line_d = plt.axhline(y=yd, color='gray', linewidth=1, linestyle='--')
plt.fill_between(range(-1, len(df) + 1), yd, yu, color='gray', alpha=0.25)

# Set ticks,labels, xlim, title...
plt.title('Hardest: compare each bar to a range')

plt.xlabel('Year')
plt.ylabel('Value')

plt.xlim(-0.5, 3.5)

plt.xticks(range(len(df)), df.index)
yt_o = plt.gca().get_yticks()
yt = np.append(yt_o, ys)
plt.gca().set_yticks(yt)
y_text = plt.text(1,
                  55000,
                  "y range : {:.0f}~{:.0f}".format(yd, yu),
                  bbox=dict(fc='white', ec='k'))

# Add interactivity
def onclick(event): 
    
    yu = max(ys)
    yd = min(ys)
    
    plt.fill_between(range(-1, len(df) + 1), 0, 60000, color='white', alpha=1)
    y = event.ydata
    
    if abs(y-yu) > abs(y-yd):
        yd=y
        ys[1]=y
        hoz_line_d.set_ydata(yd)
    else:
        yu=y
        ys[0]=y
        hoz_line_u.set_ydata(yu)
    plt.fill_between(range(-1, len(df) + 1), yd, yu, color='gray', alpha=0.25)

    yt = np.append(yt_o, ys)
    plt.gca().set_yticks(yt)
    y_text = plt.text(1,
                      55000,
                      "y range : {:.0f}~{:.0f}".format(yd, yu),
                      bbox=dict(fc='white', ec='k'))

    
    probs = [compute_probs(ys, ci) for ci in conf_ints]
    for i in range(len(df)):
        bars[i].set_color(cpick.to_rgba(probs[i]))
        bars[i].set_edgecolor('gray')
    

plt.gcf().canvas.mpl_connect('button_press_event', onclick)

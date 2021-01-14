import numpy as np
from math import pi
from matplotlib import pyplot as plt

# Sort the group mean by descending order
def sort_categories_by_mean(labels, sorted_index):
    sorted_categories_by_mean = np.zeros_like(labels)
    for i in range(len(sorted_index)):
        sorted_categories_by_mean[np.where(labels == sorted_index[i])[0]] = i + 1
    
    return sorted_categories_by_mean

# Calculte the group mean per each component
def calc_mean_components_by_group(items_per_component,group_mean, group_num):
    mean_per_component = dict()
    
    for component in list(items_per_component.keys()):
        if len(items_per_component[component]) == 1 :
            mean_per_component[component] = group_mean[group_num - 1][items_per_component[component][0] - 1]
        else :
            tmp = list()
            for j in items_per_component[component]:
                tmp.append(group_mean[group_num - 1][j - 1])
            mean_per_component[component] = np.mean(tmp)
            
    return mean_per_component

# Draw radar plot
def make_spider(categories, values, ax, group, linestyle):
  
    N = len(categories)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, color='grey', size=15)

    ax.set_rlabel_position(0)
    plt.yticks([-1,0,1], ["-1","0","1"], color="grey", size=12)
    plt.ylim(-2,2)


    values = list(values)
    values.append(values[0])

    ax.plot(angles, values, linewidth=2, linestyle = linestyle)
    ax.fill(angles, values, alpha=0.4)
        
    plt.title(group, size=15, y=1.1)


# Draw radar plot
def plot_spider(x, y, ax=None, linestyle='solid', color='b', fill=True, yticks=[0, 0.5, 1], ylim=[-0.08, 1]):
    N = len(x)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    if ax is None:
        ax = plt.gca()
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)

    y = list(y)
    y.append(y[0])  # to close the circle

    ax.plot(angles, y, linewidth=2, linestyle=linestyle, color=color)
    if fill:
        ax.fill(angles, y, alpha=0.4)

    plt.xticks(angles[:-1], x, color='grey', size=15)

    plt.yticks(yticks, ['{:.1f}'.format(yt) for yt in yticks], color="grey", size=12)
    plt.ylim(ylim)

    # print(ax.spines.keys()) # ['polar', 'start', 'end', 'inner']
    ax.spines['polar'].set_visible(False)  # redundant
    # ax.spines['inner'].set_visible(False)

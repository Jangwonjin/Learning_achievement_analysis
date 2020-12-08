import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from matplotlib import pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
from matplotlib import cm

# Elbow method
def elbow_method(x):
    inertias = []
    ks = [i for i in range(2, 10)]
    for k in ks:
        model = KMeans(n_clusters=k, random_state=0)
        model.fit(x)
        inertias.append(model.inertia_)
    
    plt.plot(range(2,10), inertias, 'o-')
    plt.title('elbow method')
    
# Draw the silhouette diagram
def plot_silhouette_diagram(X, labels, silhouette_scores):
    plt.figure(figsize=(11, 9))

    for k in (3, 4, 5, 6):
        plt.subplot(2, 2, k - 2)
        
        y_pred = labels[k - 3]
        silhouette_coefficients = silhouette_samples(X, y_pred)

        padding = len(X) // 30
        pos = padding
        ticks = []
        for i in range(k):
            coeffs = silhouette_coefficients[y_pred == i + 1]
            coeffs.sort()

            color = cm.Spectral( i / k)
            plt.fill_betweenx(np.arange(pos, pos + len(coeffs)), 0, coeffs,
                              facecolor=color, edgecolor=color, alpha=0.7)
            ticks.append(pos + len(coeffs) // 2)
            pos += len(coeffs) + padding

        plt.gca().yaxis.set_major_locator(FixedLocator(ticks))
        plt.gca().yaxis.set_major_formatter(FixedFormatter(range(k)))
        if k in (3, 5):
            plt.ylabel("Cluster")

        if k in (5, 6):
            plt.gca().set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
            plt.xlabel("Silhouette Coefficient")
        else:
            plt.tick_params(labelbottom=False)

        plt.axvline(x=silhouette_scores[k - 3], color="red", linestyle="--")
        plt.title("$k={}$".format(k), fontsize=16)
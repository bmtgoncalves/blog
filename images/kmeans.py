import imageio
from sklearn.cluster import KMeans

im = imageio.imread('cambodja.jpg')
kmeans = KMeans(n_clusters=10)

n_row, n_col, n_chan = im.shape

im_array = im.reshape((n_row*n_col, n_chan))

kmeans.fit(im_array)

colors = kmeans.cluster_centers_

new_im_array = colors[kmeans.labels_].astype('uint8')
new_im_array = new_im_array.reshape((n_row, n_col, n_chan))

new_im = imageio.core.util.Image(new_im_array)

imageio.imwrite('temp.jpg', new_im)

print(colors.astype('int'))
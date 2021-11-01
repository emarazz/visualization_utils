import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image

from typing import List


def show_grid(imgs : List[List[Image.Image]], titles : List[str] = [], figsize : tuple = (20,16), axes_pad : tuple = (0.1,0.2)) -> None:
    ''' Shows a grid of images.
        
        Args:
            imgs (list of list of PIL Image) : The outer list defines the order of the columns where the images of the inner list will be displayed.
            titles (list of str) :  The order of the list defines the titles for each column.
            figsize (tuple, optional) : Defines the figure size. This parameter is passed as an argument to the plt.figure() instance. The default value is (20, 16).
            axes_pad (tuple, optional) : Defines the axes pad horizontally and vertically. This parameter is passed as an argument to the ImageGrid() instance. The default value is (0,1,0.3).
    
    '''

    n_cols = len(imgs)
    n_rows = len(imgs[0])

    fig = plt.figure(figsize = figsize)
    grid = ImageGrid(
                        fig, 111,
                        nrows_ncols=(n_rows, n_cols),
                        axes_pad=axes_pad,
                        direction='column', 
                    )

    for ax, img in zip(grid, [img for img_cols in imgs for img in img_cols]):
        ax.imshow(img)
        ax.set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])

    # If titles is not empty, it adds a title to each column
    if titles:
        axs = np.reshape(grid, (n_cols, n_rows))
        for j, title in enumerate(titles):
            axs[j,0].set_title(title)

    plt.show()
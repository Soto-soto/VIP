# 各種ライブラリをインポートする
from PIL import Image,  ImageOps # 画像を開くのに必要
import matplotlib.pyplot as plt # 画像を表示するのに必要
import numpy as np # 画像をmatplotlibで表示するのに必要
from random import randint

# 画像を9分割した内の1つを反転する関数
def ランダム反転(image):
    img_width, img_height = image.size
    x=randint(0,2)
    y=randint(0,2)
    
    def _三分の一(width: int, height: int, split_num: tuple):
        im = Image.open('vim.png')
        w3 = width/3
        h3 = height/3
        return (w3*split_num[0], h3*split_num[1], w3*(split_num[0]+1), h3*(split_num[1]+1))

    
    graph = Image.new('RGB', (img_width, img_height))
    for i in range(3):
        dst = Image.new('RGB', (img_width, int(img_height/3)))
        for j in range(3):
            img = image.crop((_三分の一(img_width,img_height, (j,i))))
            if (i == x) & (j == y):
                img = ImageOps.mirror(img)
            dst.paste(img, (int(img_width*j/3),0))
        graph.paste(dst, (0,int(img_height*i/3)))
    return graph

# 画像を表示する関数
def show_image():
    # matplotlibで表示する
    im = Image.open('vim.png')
    while(True):
        im = ランダム反転(im)
        plt.imshow(np.array(im))
        # 画面に出力する
        plt.show(block=False)
        plt.pause(5) # 5秒待つ
        plt.clf()


# 実行する
if __name__ == '__main__':
    # 上記関数を実行する
    show_image()

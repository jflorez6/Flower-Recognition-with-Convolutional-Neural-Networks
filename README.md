# Introduction
Welcome to my Flower Recognition repository! I will update this README soon with more info, but for now you can see all the notebooks to see how this works. I utilize image data to train a neural network in Tensorflow on several classes (currently 10) of flowers (~ 600-900 images each). The data I use here is an extension of the original [Flowers Recognition](https://www.kaggle.com/alxmamaev/flowers-recognition) data set from Kaggle, which consisted of images of flowers representing five species. I have since added 5 more classes of flowers and uploaded the current data set to Kaggle as the publicly available [Extended Flowers Recognition](https://www.kaggle.com/jonathanflorez/extended-flowers-recognition/activity) data set. While you can visit Kaggle to download this data set, this repository will always have the most up to date version of the data set.

If you are interested in downloading more images you are welcome to use the [Image Scraping with Chrome Notebook](./image-scraping-with-Chrome.ipynb). You will need the following packages if you want to run this code:

- PIL
- os
- selenium
- time
- io
- requests
- hashlib
- yandex-images-download

*Note this is not a complete list of packaages required to run the code in this repository. Will add more complete description in the near future!

Lastly, you can visit the two other notebooks in this repository to see how I do [Flower Classification with my own CNN in Tensorflow](./flower-recognition-with-cnn.ipynb
) as well as [Flower Classification using Transfer Learning](./flower-recognition-using-transfer-learning.ipynb)

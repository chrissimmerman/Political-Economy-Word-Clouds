import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
walrasFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\walras-elements.txt", "r", encoding="utf-8")
walrasTxt = walrasFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may", "heroy"])

#importing image
walrasMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\walras.png"))

#generating word cloud
walrasWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 180000, mask = walrasMask, stopwords=stopwords, background_color=None, mode = "RGBA")
walrasWC.generate(walrasTxt)

#generating colors from image
image_colors = ImageColorGenerator(walrasMask)
plt.imshow(walrasWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\walrascloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
walrasFile.close()

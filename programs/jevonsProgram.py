import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
jevonsFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\jevons-theory.txt", "r", encoding="utf-8")
jevonsTxt = jevonsFile.read()


#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["gif", "will", "must", "may"])

#importing image
jevonsMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\jevons.png"))

#generating word cloud
jevonsWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 90000, mask = jevonsMask, stopwords=stopwords, background_color=None, mode = "RGBA")
jevonsWC.generate(jevonsTxt)

#generating colors from image
image_colors = ImageColorGenerator(jevonsMask)
plt.imshow(jevonsWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\jevonscloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
jevonsFile.close()

import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
millFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\mill.txt", "r", encoding="utf-8")
millTxt = millFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may", "much", "8sect"])

#importing image
millMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\mill-mask.png"))

#generating word cloud
millWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 460000, mask = millMask, stopwords=stopwords, background_color="white")
millWC.generate(millTxt)

#generating colors from image
image_colors = ImageColorGenerator(millMask)
plt.imshow(millWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\millcloud.png", dpi = 300)
plt.show()

#closing text
millFile.close()

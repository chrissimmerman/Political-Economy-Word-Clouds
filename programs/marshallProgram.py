import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
marshallFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\marshall-principles.txt", "r", encoding="utf-8")
marshallTxt = marshallFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may", "much", "8sect"])

#importing image
marshallMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\marshall.png"))

#generating word cloud
marshallWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 350000, mask = marshallMask, stopwords=stopwords, background_color=None, mode = "RGBA")
marshallWC.generate(marshallTxt)

#generating colors from image
image_colors = ImageColorGenerator(marshallMask)
plt.imshow(marshallWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\marshallcloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
marshallFile.close()

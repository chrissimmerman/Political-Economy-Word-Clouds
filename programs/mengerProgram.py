import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
mengerFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\menger-principles.txt", "r", encoding="utf-8")
mengerTxt = mengerFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may"])

#importing image
mengerMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\menger.png"))

#generating word cloud
menger_wc = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 110000, mask = mengerMask, stopwords=stopwords, background_color=None, mode = "RGBA")
menger_wc.generate(mengerTxt)

#generating colors from image
image_colors = ImageColorGenerator(mengerMask)
plt.imshow(menger_wc.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\mengercloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
mengerFile.close()

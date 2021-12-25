import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
clarkFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\clark-philosophy.txt", "r", encoding="utf-8")
clarkTxt = clarkFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may"])

#importing image
clarkMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\clark.png"))

#generating word cloud
clarkWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 350000, mask = clarkMask, stopwords=stopwords, background_color=None, mode = "RGBA")
clarkWC.generate(clarkTxt)

#generating colors from image
image_colors = ImageColorGenerator(clarkMask)
plt.imshow(clarkWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\clarkcloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
clarkFile.close()

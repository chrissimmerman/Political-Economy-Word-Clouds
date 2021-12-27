import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
keynesFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\keynes.txt", "r", encoding="utf-8")
keynesTxt = keynesFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may", "much"])

#importing image
keynesMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\keynes-mask.png"))

#generating word cloud
keynesWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 120000, mask = keynesMask, stopwords=stopwords, background_color="white")
keynesWC.generate(keynesTxt)

#generating colors from image
image_colors = ImageColorGenerator(keynesMask)
plt.imshow(keynesWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\keynescloud.png", dpi = 300)
plt.show()

#closing text
keynesFile.close()

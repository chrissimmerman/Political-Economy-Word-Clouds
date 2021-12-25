import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
malthusFile = open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\malthusPrinciples.txt", "r", encoding="utf-8")
malthusTxt = malthusFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will"])

#importing image
malthusMask = np.array(Image.open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\malthus.png"))

#generating word cloud
malthus_wc = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 270000, mask = malthusMask, stopwords=stopwords, background_color=None, mode = "RGBA")
malthus_wc.generate(malthusTxt)

#generating colors from image
image_colors = ImageColorGenerator(malthusMask)
plt.imshow(malthus_wc.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\malthusCloud2.png", transparent=True, dpi = 300)
plt.show()

#closing text
malthusFile.close()

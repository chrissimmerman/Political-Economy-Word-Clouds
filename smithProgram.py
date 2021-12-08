import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
smithFile = open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\smithWON.txt", "r", encoding="utf-8")
smithTxt = smithFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)

#importing image
smithMask = np.array(Image.open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\smith.png"))

#generating word cloud
smith_wc = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 700000, mask = smithMask, stopwords=stopwords, background_color=None, mode = "RGBA")
smith_wc.generate(smithTxt)

#generating colors from image
image_colors = ImageColorGenerator(smithMask)
plt.imshow(smith_wc.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\smithCloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
smithFile.close()

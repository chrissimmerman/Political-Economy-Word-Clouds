import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

ricardoFile = open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\ricardoPrinciples.txt", "r", encoding="utf-8")
ricardoTxt = ricardoFile.read()
stopwords = set(STOPWORDS)
stopwords.update(["u", "will"])

ricardoMask = np.array(Image.open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\ricardo.png"))

ricardoWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 160000, mask = ricardoMask, stopwords=stopwords, background_color=None, mode = "RGBA")

ricardoWC.generate(ricardoTxt)

image_colors = ImageColorGenerator(ricardoMask)

plt.imshow(ricardoWC.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.savefig("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\ricardoCloud.png", transparent=True, dpi = 300)
plt.show()

ricardoFile.close()
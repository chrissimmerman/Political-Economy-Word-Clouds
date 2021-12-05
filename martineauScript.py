import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

martineauFile = open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\martineauIllustrations.txt", "r", encoding="utf-8")
martineauTxt = martineauFile.read()
stopwords = set(STOPWORDS)
stopwords.update(["u", "will"])

martineauMask = np.array(Image.open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\martineau.png"))

martineau_wc = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 920000, mask = martineauMask, stopwords=stopwords, background_color=None, mode = "RGBA")

martineau_wc.generate(martineauTxt)

image_colors = ImageColorGenerator(martineauMask)

plt.imshow(martineau_wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.savefig("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\martineauCloud.png", transparent=True, dpi = 300)
plt.show()

martineauFile.close()
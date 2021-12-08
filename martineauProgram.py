import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
martineauFile = open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\martineauIllustrations.txt", "r", encoding="utf-8")
martineauTxt = martineauFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["u", "will"])

#importing image
martineauMask = np.array(Image.open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\martineau.png"))

#generating word cloud
martineau_wc = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 920000, mask = martineauMask, stopwords=stopwords, background_color=None, mode = "RGBA")
martineau_wc.generate(martineauTxt)

#generating colors from image
image_colors = ImageColorGenerator(martineauMask)
plt.imshow(martineau_wc.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\martineauCloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
martineauFile.close()

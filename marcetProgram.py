import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
marcetFile = open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\marcetConversations.txt", "r", encoding="utf-8")
marcetTxt = marcetFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "may", "must"])

#importing image
marcetMask = np.array(Image.open("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\marcet.png"))

#generating word cloud
marcet_wc = WordCloud(font_path="C:\\WINDOWS\\FONTS\\sylfaen.TTF", max_words = 100000, mask = marcetMask, stopwords=stopwords, background_color=None, mode = "RGBA")
marcet_wc.generate(marcetTxt)

#generating colors from image
image_colors = ImageColorGenerator(marcetMask)
plt.imshow(marcet_wc.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("C:\\Users\\chris\\Documents\\GitHub\\Political-Economy-Word-Clouds\\marcetCloud.png", transparent=True, dpi = 300)
plt.show()

#closing text
marcetFile.close()

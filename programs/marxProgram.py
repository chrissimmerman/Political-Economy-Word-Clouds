import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
marxFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\marx.txt", "r", encoding="utf-8")
marxTxt = marxFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may", "much", "thus", "one"])

#importing image
marxMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\marxMask.png"))

#generating word cloud
marxWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\SYLFAEN.TTF", max_words = 350000, mask = marxMask, stopwords=stopwords, background_color="white")
marxWC.generate(marxTxt)

#generating colors from image
image_colors = ImageColorGenerator(marxMask)
plt.imshow(marxWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\marxCloud.png", dpi = 300)
plt.show()

#closing text
marxFile.close()

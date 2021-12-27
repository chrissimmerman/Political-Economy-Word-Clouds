import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#importing text
seniorFile = open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\senior.txt", "r", encoding="utf-8")
seniorTxt = seniorFile.read()

#defining words to exclude
stopwords = set(STOPWORDS)
stopwords.update(["will", "must", "may", "much", "thus", "one"])

#importing image
seniorMask = np.array(Image.open("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\senior.png"))

#generating word cloud
seniorWC = WordCloud(font_path="C:\\WINDOWS\\FONTS\\SYLFAEN.TTF", max_words = 115000, mask = seniorMask, stopwords=stopwords, background_color="white")
seniorWC.generate(seniorTxt)

#generating colors from image
image_colors = ImageColorGenerator(seniorMask)
plt.imshow(seniorWC.recolor(color_func=image_colors), interpolation="bilinear")

#saving and showing word cloud
plt.axis("off")
plt.savefig("E:\\OneDrive\\CS Projects\\Economics Word Cloud\\seniorCloud.png", dpi = 300)
plt.show()

#closing text
seniorFile.close()

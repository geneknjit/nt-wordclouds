import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import PIL.Image as Image

def remove_punctuation(text):
    text = text.replace('?', '').replace('!', '').replace('.', '').replace(',', '').replace(';', '').replace(':', '')
    text = text.replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '')
    text = text.replace('"', '').replace("'", '').replace('“', '').replace('”', '').replace('‘', '').replace('’', '')
    text = text.replace('—', '').replace('-', '').replace('…', '').replace('...', '').replace('..', '').replace('_', '')
    text = text.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '')
    text = text.replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace('ʹ', '').replace('\r\n', ' ')
    return text

stopwords = set(STOPWORDS)
stopwords.add('â')
stopwords.add('said')
stopwords.add('will')
stopwords.add('say')
stopwords.add('says')
stopwords.add('one')
stopwords.add('saying')
stopwords.add('also')
stopwords.add('like')
stopwords.add('man')
stopwords.add('thing')
stopwords.add('things')
stopwords.add('come')
stopwords.add('came')
stopwords.add('go')
stopwords.add('went')
stopwords.add('began')
for i in range(100):
    stopwords.add(f'{str(i)}a')

mask = np.array(Image.open("oval.png"))

def read_gospel_and_generate_wordcloud(gospel_name):
    with open(f'{gospel_name}.txt', 'r') as f:
        gospel = f.read().strip()
        gospel = remove_punctuation(gospel)

    gospel_cloud = WordCloud(prefer_horizontal=1, mask=mask, width=800, height=400,
                             background_color='white', stopwords=stopwords).generate(gospel)

    plt.figure(num=f'{gospel_name}')
    plt.plot()
    plt.imshow(gospel_cloud, interpolation='bicubic')
    plt.axis('off')
    plt.show()

read_gospel_and_generate_wordcloud("Matthew")
read_gospel_and_generate_wordcloud("Mark")
read_gospel_and_generate_wordcloud("Luke")
read_gospel_and_generate_wordcloud("John")
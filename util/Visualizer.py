import matplotlib.pyplot as plt
from wordcloud import WordCloud

class Visualizer:
    #Display the data

    @staticmethod
    def generate_word_cloud(dtm, stop_words):
        wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
                        max_font_size=150, random_state=42)

        plt.rcParams['figure.figsize'] = [16, 6]

        wc.generate(dtm[0])
        plt.subplot(3, 4, 0)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title("Overview")

        plt.show()
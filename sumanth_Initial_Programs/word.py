from urllib.request import urlopen
passage = urlopen("https://www.dictionary.com/browse/passage")
passage_words = []
for line in passage:
    line_words = line.split()
    for word in line_words:
        passage_words.append(word)
passage.close()
passage_words


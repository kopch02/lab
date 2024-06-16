import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
nltk.download('punkt')
import natasha as nt

newcorpus = PlaintextCorpusReader('newcorpus/', r'.*\.txt')
#Задание корпуса
data = newcorpus.raw(newcorpus.fileids())
sent_tokens = nltk.sent_tokenize(data)


def Normalize(text):
    #Инициализируем вспомогательные объекты библиотеки natasha
    segmenter = nt.Segmenter()
    morph_vocab = nt.MorphVocab()
    emb = nt.NewsEmbedding()
    morph_tagger = nt.NewsMorphTagger(emb)
    ner_tagger = nt.NewsNERTagger(emb)
    #Убираем знаки пунктуации из текста
    word_token = text.translate(str.maketrans("", "", string.punctuation)).replace("—", "")
    #Преобразуем очищенный текст в объект Doc и
    doc = nt.Doc(word_token)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.tag_ner(ner_tagger)
    #Приводим каждое слово к его изначальной форме
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    resDict = {_.text: _.lemma for _ in doc.tokens}
    #Возвращаем результат в виде списка
    return [resDict[i] for i in resDict]


def Response(user_response):
    user_response = user_response.lower()
    robo_response=''#Будущий ответ нашего бота
    sent_tokens.append(user_response)#Временно добавим запрос пользователя в наш корпус.
    TfidfVec = TfidfVectorizer(tokenizer=Normalize)#Вызовем векторизатор TF-IDF
    tfidf = TfidfVec.fit_transform(sent_tokens)#Создадим вектора
    vals = cosine_similarity(tfidf[-1], tfidf)#Через метод косинусного сходства найдем предложение снаилучшим результатом
    idx=vals.argsort()[0][-2]#Запомним индексы этого предложения
    flat = vals.flatten()#сглаживаем полученное косинусное сходство
    flat.sort()
    req_tfidf = flat[-2]
    sent_tokens.remove(user_response)
    if(req_tfidf==0): #Если сглаженное значение будет равно 0, то ответ не был найден
        robo_response=robo_response+"Извините, я не нашел ответа..."
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
from keytotext import pipeline

nlp = pipeline("mrm8488/t5-base-finetuned-common_gen")

#keywords = ['I', 'cricket']

def sentenceGen(keywords):

    sentence = nlp(keywords)

    return sentence




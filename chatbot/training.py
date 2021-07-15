import random
import json
import pickle

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer


from  tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())
words=[]
classes=[]
documents=[]
ignore_words=['!','?','.',',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list=nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            # print(f"documents{documents}")
            # print(f"words_list{word_list}")
            # print(f"words{words}")
            # print(f"Classes{classes}")

words=[lemmatizer.lemmatize(word) for word in words if word not in ignore_words]
words=sorted(set(words))
classes=sorted(set(classes))

pickle.dump(words,open('words.pk1','wb'))
pickle.dump(classes,open('classes.pk2','wb'))
training=[]
ouput_empty=[0]*len(classes)
print(len(documents))
for document in documents:
    bag=[]
    word_pattern=document[0]
    word_pattern=[lemmatizer.lemmatize(word.lower()) for word in word_pattern]
    for word in words:#comparing word from document to words list
        bag.append(1) if word in word_pattern else bag.append(0) #27sets of  document comparing with worf_patter which is in order
       # checks each word with word pattern untill end of all words.which complets 1 loop. bag will have 49 words in each iteration UPDATES
       #1 if word in pattern

    output_row=list(ouput_empty)
    output_row[classes.index(document[1])]=1 #updates 1 in loc of classes (27 loops)
    training.append([bag,output_row])

random.shuffle(training)
training=np.array(training)

x_train=list(training[:,0])
y_train=list(training[:,1])

model=Sequential()
model.add(Dense(units=128,input_shape=(len(x_train[0]),),activation='relu'))
model.add(Dropout(0.50))
model.add(Dense(units=128,activation='relu'))
model.add(Dropout(0.50))
model.add(Dense(len(y_train[0]),activation='softmax'))
sgd=SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)

model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
model.fit(np.array(x_train), np.array(y_train),epochs=100,batch_size=5,verbose=1)

model.save('chatbot model.model')
print("Done")
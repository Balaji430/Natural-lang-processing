# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:10:05 2020

@author: balaj
"""

import nltk

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
               
# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenizing words
words = nltk.word_tokenize(paragraph)

para_2 = """Venkateswara Temple is a Hindu temple situated in the hill town of Tirumala at Tirupati in Chittoor district of Andhra Pradesh, India. 
            The Temple is dedicated to Venkateswara, a form of Vishnu, 
            who is believed to have appeared here to save mankind from trials and troubles of Kali Yuga.
            Hence the place has also got the name Kaliyuga Vaikuntham and the Lord here is referred to as Kaliyuga Prathyaksha Daivam.
            The temple is also known by other names like Tirumala Temple, Tirupati Temple, Tirupati Balaji Temple. 
            Venkateswara is known by many other names: Balaji, Govinda, and Srinivasa.
            [3]The temple is run by body Tirumala Tirupati Devasthanams (TTD) which is under direct control of Andhra Pradesh Government.
            The head of TTD is appointed by Andhra Pradesh Government. 
            The revenue from this shrine is used by Andhra Pradesh government .[4]Tirumala Hills are part of Seshachalam Hills range. 
            The hills are 853 metres (2,799 ft) above sea level. 
            The Hills comprises seven peaks, representing the seven heads of Adisesha. 
            The temple lies on the seventh peak -Venkatadri, on the southern banks of Sri Swami Pushkarini, a holy water tank. 
            Hence the temple is also referred to as "Temple of Seven Hills". Tirumala town covers about 10.33 sq mi (26.75 km2) in area.
            The Temple is constructed in Dravidian architecture and is believed to be constructed over a period of time starting from 300 AD. 
            The Garbagruha (Sanctum Sanctorum) is called AnandaNilayam.
            The presiding deity, Venkateswara, is in standing posture and faces east in Garbha gruha. 
            The temple follows Vaikhanasa Agama tradition of worship. 
            The temple is one of the eight Vishnu Swayambhu Kshetras and is listed as 106th and the last earthly Divya Desam. 
            The Temple premises had two modern Queue complex buildings to organise the pilgrim rush, 
            Tarigonda Vengamamba Annaprasadam complex for free meals to Pilgrims, 
            hair tonsure buildings and a number of pilgrim lodging sites."""
            
sent_w = nltk.sent_tokenize(para_2)
words_w = nltk.word_tokenize(para_2)



from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


stemmer = PorterStemmer()

sent_ti = []
# Stemming
for i in range(len(sent_w)):
    words_1 = nltk.word_tokenize(sent_w[i])
    words_1 = [stemmer.stem(word) for word in words_1 if word not in set(stopwords.words('english'))]
    sent_w[i] = ' '.join(words_1)   


'''
    SETUP:
        - Install the required libraries using, `pip install -r requirements.txt`
    USER FLOW:
        - Enter a paragraph
        - Ask question 
        - Press q to exit
'''

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from transformers import logging
from transformers import pipeline

logging.set_verbosity_error()

import warnings
warnings.simplefilter("ignore")

model_name = "deepset/roberta-base-squad2"

print("\nDEMONSTRATION OF `Question and Answering using ml model` :)\n")

print("Instantiating the model...")

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

print("\nEnter the paragraph,\n")
context=input() 

while(True):
    print()
    print("** To exit, press q **")
    print("-> Enter your question\n")
    question=input()
    
    if(question=='q'):
        break
    
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)

    print("Answer :\33[45m{}\033[0m".format(res["answer"]))

    print("Answer confidence :\033[1;32;40m {0:.2f}\033[0m, With 1 being the highest and 0 the lowest ".format(res["score"]))
    print()
    print(context)


# Sample paragraph and questions

# Para

# Our study firstly demonstrated the regional disparity of COVID - 19 in Chongqing municipality and further thoroughly compared the differences between severe and non - severe patients. The 28 - day mortality of COVID - 19 patients from 3 designed hospitals of Chongqing is 1. 5 %, lower than that of Hubei province and mainland China including Hubei province. However, the 28 - mortality of severe patients was relatively high, with much higher when complications occurred. Notably, the 28 - mortality of critically severe patients complicated with severe ARDS is considerably as high as 44. 4 %. Therefore, early diagnosis and intensive care of critically severe COVID - 19 cases, especially those combined with ARDS, will be considerably essential to reduce mortality.

# Questions

# What is the para about?
# Where was the observation taken?
# What are the various places in Chogquing municiplity were the test taken from?
# Total number of mortality?
# When was the morality high?
# What are the complications?
# How to reduce the morality?
# Was the morality rate higher than other provinces?
# Compared to other provinces, Was the mortality higher?


# Question and Answering bot

The bot is capable of understanding the context of any paragraph/article given to it and can answer questions related to the context. This is accomplished by the underlying machine learning model which has been trained with a dataset that contains wide variety of question and its answers across various context.

### Getting started, 
#### Installation and Execution

- Install the necessary libraries, `pip install -r requirements.txt`
- Run the script using, `python QandA-bot.py`

#### Training the paragraph and the program flow
- Once the script is started, There would be a prompt in the terminal asking you to **"Enter the paragraph"**.
- Insert/Type the paragraph that you would like to question.
- The script then understand the context of the paragraph.
- Once it is done with learning the context, The script would again prompt in the terminal mentioning **"Enter your question"**
- Now you can ask any question, The bot would response with **an answer and a score representing its confidence on the answer.**
- If the question is not related to the paragraph or if the question isn't framed properly, then the response from the bot would be random and the confidence score will also be close to zero.
- Once answered, the script then prompts for another question. This process is repeated until you exit the script.
- To exit the script, Enter `q` during the question prompt.

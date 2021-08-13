import pandas
import os
import re
from .emoname import *

def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = re.sub(r'('+emot+')', "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()), text)
    return text

class Emoji:
    ''' Remove the emoji from the sentence'''
    
    def __init__(self, dataframe):
        self.UNICODE_EMO = UNICODE_EMO
        self.dataframe = dataframe
        self.columns = dataframe.columns
        
    def rem_emoji_text(self, userstring):
        ''' Convert the text into emoji meaning
            emoji.remoji.rem_emoji_text(string)
            '''
        try:
            return convert_emojis(userstring)
        except Exception as e:
            print(e)
    def rem_emoji_dataframe(self, target_column):
        '''convert emoji from tareget column into emoji meaning
            emoji.remoji.rem_emoji_dataframe([column_name])
        '''
        if(target_column not in self.columns):
            # if target column is not present in the data frame
            print(f"Try with column present in Data Frame like {self.columns}")
        else:
            try:
                return self.dataframe[target_column].apply(lambda x:  convert_emojis(x))
            except Exception as e:
                print(e)

import re
import os

abbreviation = ['ROFL', 'STFU', 'ICYMI', 'TL;DR', 'LMK', 'NVM', 'TGIF', 'TBH', 'TBF', 'RN', 'QOTD', 'OOTD', 'BRB', 'BTW', 'LOL', 'TTYL', 'HMU', 'FWIW', 'IMO', 'IMHO', 'IDK', 'TBA', 'TBD', 'ILY', 'MCM', 'WCW', 'BF', 'GF', 'CTA', 'UGC', 'SMS', 'MMS', 'RCS', 'ROI', 'CTR', '5G']
fullform = [' Rolling on floor laughing ', ' Shut the *swear word!* up', ' In case you missed it', ' Too long, didn’t read', ' Let me know', ' Nevermind ', ' Thank goodness it’s Friday', ' To be honest', ' To be frank', ' Right now', ' Quote of the day', ' Outfit of the day', ' Be right back', ' By the way', ' Laugh out loud', ' Talk to you later', ' Hit me up', ' For what it’s worth', ' In my opinion', ' In my humble opinion', ' I don’t know', ' To be announced', ' To be decided', ' I love you', ' Man crush Monday', ' Woman crush Wednesday', ' Boyfriend', ' Girlfriend', ' Call to action', ' User-generated content', ' Short message service', ' Multimedia messaging service', ' Rich communication services', ' Return on investment', ' Click-through rate', ' 5th generation, meaning the newest generation of mobile communications']

# Translator function
def translator(user_string):
    '''Takes the sentence replace the abbreviation words by their full form'''
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        # Removing Special Characters.
        _str = re.sub('[^a-zA-Z0-9]+', '', _str)
        if _str.upper() in abbreviation:
                idx = abbreviation.index(_str.upper())
                user_string[j] = fullform[idx]
        j = j + 1
    return ' '.join(user_string)

        
class Abbreviations:
    ''' Remove the abbreviation from the sentence using 
        remove_abb.remove_abb_dataframe'''
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.columns = dataframe.columns
    

    def remove_abb_dataframe(self, target_column):
        '''
        Remove the abbreviation from column given in the data frame
        
        '''
        if(target_column not in self.columns):
            # if target column is not present in the data frame
            print(f"Try with column present in Data Frame like {self.columns}")
        
        else:
            # if target column is present in data frame
            try:
                return self.dataframe[target_column].apply(lambda x:  translator(x))
            except Exception as e:
                print(e)
    
    
    def remove_abb_text(self, userstring):
        '''
        remove abbreviation of the text given
        '''
        try:
            return translator(userstring)
        except Exception as e:
            print(e)

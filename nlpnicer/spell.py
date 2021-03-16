
import re
from textblob import TextBlob

def spellcheck(user_string):
    '''Text blob library for correction'''
    _str = TextBlob(user_string)
    return str(_str.correct())

class Spell:
    '''Remove spell mistake from the text or column given in the data frame
            
            rem_spell_mistk.spellcheck(string) remove spell mistakes(if any) 
            from the string given as input
            
            rem_spell_mistk.spellcheck_dataframe(df, [column]) remove the spell 
            mistakes from data[column]'''
    def __init__(self, df):
        self.df = df
        self.columns = self.df.columns
        
    def spellcheck_text(self, user_string):
        '''spell correction of the string given spellcheck_text(string)'''
        return spellcheck(user_string)
    
    def spellcheck_dataframe(self, column):
        '''spell correction of the string given spellcheck_dataframe(column)'''
        if(column not in self.columns):
            # if target column is not present in the data frame
            print(f"Try with column present in Data Frame like {self.columns}")
        
        else:
            # if target column is present in data frame
            try:
                return self.df[column].apply(lambda x:  spellcheck(x))
            except Exception as e:
                print(e)

# to clean the file :
import csv, re
import os

def translator(user_string):
    '''Takes the sentence replace the abbreviation words by their full form'''
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        # File path which consists of Abbreviations.
        fileName = "abbreviation.csv"

        # File Access mode [Read Mode]
        with open(fileName, "r") as myCSVfile:
            dataFromFile = csv.reader(myCSVfile)
            # Removing Special Characters.
            _str = re.sub('[^a-zA-Z0-9]+', '', _str)
            for row in dataFromFile:
                if _str.upper() == row[0]:
                    # If match found replace it with its appropriate phrase in text file.
                    user_string[j] = row[1]
            myCSVfile.close()
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

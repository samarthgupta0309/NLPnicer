# NLPnicer - -new way for improving data quality in NLP

NLPnicer is a initiative which solves the 21st century problem of expressing yourself in emoticons or in abbreviation.
Cleaning your data is the biggest headache in a data scientist life. In Natural Language processing having emoticons, abbreviations, etc are the impurity with majority of people either drop or run a `for` loop which replaces the emoticons or abbreviation with their meaning.

Imagine you're going for review sentiments and you find the case
<p align='center'>
  <img src = 'https://github.com/samarthgupta0309/nlpnicer/blob/main/images/reviewimg1.png'></img>
 </p>

Three problematic things are here: 
  * first spelling of "coool" 
  * the lit emoji  
  * abbreviation BTW

These things have to treated
If you want this why don't you give NLPnicer a shot. Let us do the hardwork. This is what you have to do
1. Install NLPnicer 
```
!pip install nlpnicer
```
2. Import modules
```
import nlpnicer
from nlpnicer.abbreviation import Abbreviations
from nlpnicer.emoji import Emoji
from nlpnicer.spell import Spell
```
3. Handling abbreviations
```
handle_Abbreviation = Abbreviations(dataFrame)

handle_Abbreviation.remove_abb_dataframe(column_name)
>>> returns processed dataFrame[column_name]

handle_Abbreviation.remove_abb_text("LOL!!")
>>>returns processed text Here, "Laugh out loud"
```
4. Handling Emojis
```
handle_emoji = Emoji(dataFrame)

handle_emoji.rem_emoji_dataframe(column_name)
>>> returns processed dataFrame[column_name]

handle_emoji.rem_emoji_text("❤️")
>>>returns processed text Here, "Red Heart"
```
5. Handling spelling check/Error
```
handle_spell = Spell(dataFrame)

handle_spell.spellcheck_dataframe(column_name)
>>> returns processed dataFrame[column_name]

handle_spell.spellcheck_text("Now that's goood")
>>>returns processed text Here, "Now that's good"
```
The NLPnicer is just in inital phase contributing to this would make it even more better :)

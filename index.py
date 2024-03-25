# imports PywebIO, Json modules
# Dev notes WORK IN PROGRESS (Problem is on line 13)
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
# clears screen of previous fact
    clear()

put_html("<p align=""left""> <h2><img src="smile.jpg" alt="Place holder" width = "7%" > Fun Fact Generator </h2></p>") 
                
# fetches fun facts 
url = "https://uselessfacts.jsph.pl/random.json?language=en" 
# Uses GET request
response = requests.requests("GET", url)
# Loads GET request into json
data = json.loads(response.text)

useless_fact = data['text']
# styles the button
style(put_text(useless_fact), 'color: blue; font-size: 30px')
put_buttons([dict(label='Click me', value='outline-success',  
              color='outline-success')], onclick=get_fun_fact)
# Driver function
if _name_ == '_main_':
# adds logo and header
 put_html(" <p align=""left""><h2><img src="smile.jpg" alt ="Place Holder" width="7%" > Fun Fact Generator</h2></p>")  
# holds fact and adds button
put_buttons( [dict(label='Click me', value='outline-success',  
              color='outline-success')], onclick=get_fun_fact)
hold()
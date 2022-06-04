#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob
from flask import Flask    
app = Flask(__name__)

from flask import render_template,request

@app.route("/", methods=["GET", "POST"])   #@ decorator
def index():   #index is first function, the filename of the HTML file
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="Waiting for input."))

if __name__=="__main__":
    app.run()
#http://127.0.0.1:5000/ port is a special address: 5000 is door number, if you want to change it just insert somewhere port number = 1234?


# In[ ]:





# In[ ]:





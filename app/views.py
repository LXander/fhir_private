from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import jsonexample as jp
import set_private as sp


@app.route('/index')
def index():
    user = {'nickname': 'Dear Doctor'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/')
@app.route('/submit', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested for OpenID="%s", remember_me=%s' %
        #     (form.openid.data, str(form.remember_me.data)))

        return render_template('index.html',
                          title="Result",
                          form = form)
        #return redirect('/index')
    return render_template('submit.html', 
                           title='Submit',
                           form=form)


#@app.route('/patient')
#def set():

@app.route('/patient',methods=['GET','POST'])
def set():
    e = jp.simple
    reserved_word = 'test'
    fieldname = 'fieldname'
    class_list,class_dict,form = sp.strcture_json(e,reserved_word,fieldname)
    length = len(class_list)
    if form.validate_on_submit():
        sp.set_mask(form,e,reserved_word,fieldname)
        return render_template('temp.html')
    return render_template('bt.html',class_list=class_list,form =form,length = length,
                           str = str,getattr= getattr,fieldname = fieldname,word_len=len(reserved_word),reserved_word = reserved_word)


@app.route('/private_submit',methods=['GET','POST'])
def private_submit():
    pass
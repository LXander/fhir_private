from flask import render_template, flash, redirect
from app import app
from forms import set_query_form
from forms import set_patient_from_and_class
import jsonexample as jp
import set_private as sp
import private_extrace as pe

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
    form = set_query_form()
    if form.validate_on_submit():
        #flash('Login requested for OpenID="%s", remember_me=%s' %
        #     (form.openid.data, str(form.remember_me.data)))
        keys = pe.extend_option(form)
        return render_template('index.html',
                          title="Result",
                          form = form,keys = keys)
        #return redirect('/index')
    return render_template('submit.html', 
                           title='Submit',
                           form=form)


#@app.route('/patient')
#def set():

@app.route('/patient',methods=['GET','POST'])
def set():
    e = jp.w
    reserved_word = 'test'
    fieldname = 'fieldname'
    class_list,class_dict,form = sp.strcture_json(e,reserved_word,fieldname)
    length = len(class_list)
    if form.validate_on_submit():
        sp.set_mask(form,e,reserved_word,fieldname)
        return render_template('temp.html',form= form)
    return render_template('btt.html',class_list=class_list,form =form,length = length,len = len,
                           str = str,getattr= getattr,fieldname = fieldname,word_len=len(reserved_word),reserved_word = reserved_word)


@app.route('/patient_test',methods=['GET','POST'])
def set_form():
    e = jp.w
    patient_info_form,patient_info_class = set_patient_from_and_class(e)
    if patient_info_form.validate_on_submit():
        return render_template('temp.html',form= patient_info_form)
    return render_template('private_set.html',form = patient_info_form,patient_info = patient_info_class)



@app.route('/private_submit',methods=['GET','POST'])
def private_submit():
    pass
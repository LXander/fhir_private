from flask import render_template, flash, redirect
from app import app
from forms import set_query_form
from forms import set_relative_info,init_setting
import jsonexample as jp
import set_private as sp
import private_extrace as pe
import json
import parser as pr




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
    o = jp.ob_ep
    s = jp.seq_ep
    o = jp.read_ob
    #e = jp.read_p
    patient_info_form,patient_info_class,observation = set_relative_info(e,o,[s])
    if patient_info_form.validate_on_submit():

        pe.get_private_profile(patient_info_form,patient_info_class,observation,e)

        return render_template('temp.html',form= patient_info_form)
    return render_template('private_set.html',form = patient_info_form,patient_info = patient_info_class,observation = observation)

@app.route('/display_test',methods=['GET','POST'])
def display_result():
    private_profile = json.dumps(jp.private_policy)
    seq = json.dumps(jp.seq_ep)
    raw_ob = json.dumps(jp.ob_ep)
    raw_json_patient = json.dumps(jp.w)
    raw_seq = [seq]
    selected_keys = pe.simple_key + pe.complex_key
    patient,observation = pe.display(selected_keys, private_profile, raw_json_patient,raw_ob,raw_seq)
    return render_template('display_result.html',patient_info = patient,observation = observation)

@app.route('/re_display',methods=['GET','POST'])
def re_display():
    private_profile = json.dumps(jp.private_policy)
    seq = json.dumps(jp.seq_ep)
    raw_ob = json.dumps(jp.ob_ep)
    raw_json_patient = json.dumps(jp.w)
    raw_seq = [seq]
    selected_keys = pe.simple_key + pe.complex_key
    patient,observation,sequences = pr.display(selected_keys, private_profile, raw_json_patient,raw_ob,raw_seq)
    return render_template('rebuild_show.html',patient_info = patient,observation = observation,sequences = sequences)

@app.route('/rebuild_set',methods=['GET','POST'])
def rebuild_set():
    e = jp.w
    e = jp.read_p

    o = jp.ob_ep
    o = jp.read_ob

    s = jp.seq_ep
    s = jp.seq_ep

    form,patient,observation,sequences = init_setting(e,[o],[s])
    if form.validate_on_submit():
        pr.get_private_profile(form,patient,observation,sequences,e)
        return render_template('temp.html',form=form)
    return render_template('rebuild_set.html',form=form,patient_info=patient,observation = observation,sequences = sequences)



@app.route('/masked_content')
def masked_content_info():
    return render_template('masked_content.html')

@app.route('/private_submit',methods=['GET','POST'])
def private_submit():
    pass
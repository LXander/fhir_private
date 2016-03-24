from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
import private_extrace as pe


#patient_info_key = ['name','telecom','gender','birthDate','deceased','contact','address','maritalStatus','multipleBirth','animal','communication']

class LoginForm(Form):
    identifier= StringField('identifier', validators=[DataRequired(message=u'You must input patient\'s ID')])

    #remember_me = BooleanField('address', default=False)



class Patient_from(Form):
    pass


def set_patient_from_and_class(json_file):
    patient_info_class = pe.patient_info(json_file)

    for i in range(patient_info_class.field_num):
        fieldkey=  "boolean_field_"+str(i)
        setattr(Patient_from,fieldkey,BooleanField(fieldkey,default=False))

    form = Patient_from()
    return form,patient_info_class

def set_query_form():
    patient_info_key = pe.get_option()
    for i in range(len(patient_info_key)):
        setattr(LoginForm,patient_info_key[i],BooleanField(patient_info_key[i],default=False))

    form = LoginForm()
    return form



from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
import private_extrace as pe




class LoginForm(Form):
    identifier= StringField('identifier', validators=[DataRequired(message=u'You must input patient\'s ID')])
    active = BooleanField('active',default=False)
    name = BooleanField('name',default=False)
    telecom = BooleanField('telecom',default=False)
    gender = BooleanField('gender',default=False)
    birthDate = BooleanField('birthDate',default=False)
    address = BooleanField('address',default=False)
    maritalStatus = BooleanField('maritalStatus',default=False)

    contact_relationship = BooleanField('contact_relationship',default=False)
    contact_name = BooleanField('contact_name',default=False)
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




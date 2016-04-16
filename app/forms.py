from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
import private_extrace as pe


#patient_info_key = ['name','telecom','gender','birthDate','deceased','contact','address','maritalStatus','multipleBirth','animal','communication']

class LoginForm(Form):
    identifier= StringField('identifier', validators=[DataRequired(message=u'You must input patient\'s ID')])
    disease = StringField('disease')

    #remember_me = BooleanField('address', default=False)



class Patient_from(Form):
    pass


def set_relative_info(patient,observation,sequences):
    patient_info = pe.patient_info(patient)


    observation = pe.ob_info(observation)
    if sequences:
        for se in sequences:
            observation.add_sequence(se)

    num = patient_info.field_num

    observation.init_seq(num)

    for i in range(observation.field_num):
        fieldkey=  "boolean_field_"+str(i)
        setattr(Patient_from,fieldkey,BooleanField(fieldkey,default=False))

    form = Patient_from()
    return form,patient_info,observation

def set_query_form():
    patient_info_key = pe.get_option()
    for i in range(len(patient_info_key)):
        setattr(LoginForm,patient_info_key[i],BooleanField(patient_info_key[i],default=False))

    form = LoginForm()
    return form



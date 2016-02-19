from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired




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





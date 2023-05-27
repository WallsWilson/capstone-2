from flask_wtf import FlaskForm;
from wtforms import DecimalField, StringField, TextAreaField;
from wtforms.validators import DataRequired, NumberRange, Length;

class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])

    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(min=0, max=5)])

    review_text = TextAreaField('Review Text', validators=[DataRequired(), Length(max=500)])

    

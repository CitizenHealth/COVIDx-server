import json
from datetime import datetime
form_submission_text = """
{
  "form": "demographics",
  "responses": {
    "how_are_you_feeling": 5,
    "fever_best_guess": 3,
    "year_of_birth": 1800,
    "sex": "female",
    "country": "af",
    "current_symptoms": [],
    "race": [],
    "ethnicity": [],
    "how_are_you_feeling": 3,
    "temperature": 2000.5,
    "temperature_scale": "fahrenheit",
    "year_of_birth": 2020,
    "sex": "other",
    "country": "ar",
    "zip_code": "12345",
    "email": "test@test.com",
    "current_symptoms": [
      "fever",
      "chills",
      "fatigue",
      "dry_cough",
      "wet_cough",
      "shortness_of_breath",
      "loss_of_taste",
      "loss_of_smell",
      "diarrhea",
      "sore_throat",
      "nausea",
      "vomiting",
      "pressure_in_chest",
      "pink_eye",
      "headache",
      "confusion",
      "rash_on_feet",
      "abdominal_pain",
      "chest_pain",
      "muscle_pain",
      "loss_of_appetite",
      "hoarseness",
      "no_symptoms"
    ],
    "race": [
      "white",
      "middle_eastern_north_african",
      "black",
      "east_southeast_asian",
      "south_asian",
      "central_asian",
      "native_americans_indigenous",
      "pacific_islander",
      "hispanic",
      "1234",
      "324",
      ""
    ],
    "ethnicity": [
      "african_american",
      "afro_caribbean",
      "arab",
      "bengali",
      "chinese",
      "dutch",
      "english",
      "french",
      "german",
      "hmong",
      "irish",
      "indian",
      "inuit",
      "japanese",
      "korean",
      "navajo",
      "polish",
      "russian",
      "thai",
      "turk",
      "somali",
      "spaniard",
      "vietnamese",
      "test",
      "test",
      "test",
      ""
    ]
  }
}
"""
form_json = json.loads(form_submission_text)
form_name = form_json['form']
form_submission = form_json['responses']
form_types = [type(x) for x in form_submission.values()]
def process_form_submission(form_data):
    req_data = {
            k: '^_^'.join(v) if type(v) == list 
            else datetime.strptime(v, '%m/%d/%Y') 
            if 'date' in k and v is not None
            else v for k, v in form_data.items()
        }
    return req_data
z = process_form_submission(form_submission)

col_map = {
    str: lambda k, l: f"{k} = db.Column(db.String({max(l // 10 * 10, 80)}))",
    int: lambda k, l: f"{k} = db.Column(db.Integer())",
    float: lambda k, l: f"{k} = db.Column(db.Float())",
    datetime: lambda k, l: f"{k} = db.Column(db.DateTime())",
    bool: lambda k, l: f"{k} = db.Column(db.Boolean())",
    list: lambda k, l: f"{k} = db.Column(db.String({max(l * 2, 300)}))"
}
columns = '\n    '.join(sorted([col_map[type(form_submission[k]) if type(v) == str else str](k, len(v) if type(v) == str else -1) for k, v in z.items()]))
output_class = f"""
from app import db

class {form_name.title()}(db.Model):
    __tablename__ = "{form_name.lower()}"

    survey_response_id = db.Column(
        db.Integer(),
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"))
    submitted_date = db.Column(db.DateTime())
    
    {columns}

    @property
    def as_json(self):
        return {{col.name: getattr(self, col.name) for col in self.__table__.columns}}
"""


with open(f'./{form_name.title()}.py', 'w') as f:
  f.write(output_class)

# with open(f'./test.py', 'a') as f:
#   f.write(
#     f"""
#       from {form_name.title()} import {form_name.title()}
#       classes['{form_name.lower()}'] = {form_name.title()}
#     """
#   )

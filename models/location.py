from sqlalchemy import CheckConstraint
from app import db


# class Location(db.Model):
#     """
#     figure out where they were at any given time
#     """
#     __tablename__ = "location"

#     location_id = db.Column(db.String(50), primary_key=True, unique=True, nullable=True)
#     survey_id = db.Column(db.Integer(), db.ForeignKey('survey_metadata.survey_id'))
#     latitude = db.Column(db.Float())
#     longitude = db.Column(db.Float())
#     date = db.Column(db.DateTime())
#     zip_code = db.Column(db.String(25))

#     @property
#     def as_json(self):
#         return {col.name: getattr(self, col.name) for col in self.__table__.columns}

#     def __repr__(self):
#         return f"location_id => {self.location_id}"


# class StateResults(db.Model):
#     """
#     figure out where they were at any given time
#     """
#     __tablename__ = "state_results"

#     state = db.Column(db.String(50))
#     positive = db.Column(db.Integer())
#     positiveScore = db.Column(db.Integer())
#     negativeScore = db.Column(db.Integer())
#     negativeRegularScore = db.Column(db.Integer())
#     commercialScore = db.Column(db.Integer())
#     grade = db.Column(db.String(5))
#     score = db.Column(db.Integer())
#     negative = db.Column(db.Integer())
#     pending = db.Column(db.Integer())
#     hospitalizedCurrently = db.Column(db.Integer())
#     hospitalizedCumulative = db.Column(db.Integer())
#     inIcuCurrently = db.Column(db.Integer())
#     inIcuCumulative = db.Column(db.Integer())
#     onVentilatorCurrently = db.Column(db.Integer())
#     onVentilatorCumulative = db.Column(db.Integer())
#     recovered = db.Column(db.Integer())
#     lastUpdateEt = db.Column(db.String(50))
#     checkTimeEt = db.Column(db.String(50))
#     death = db.Column(db.Integer())
#     hospitalized = db.Column(db.Integer())
#     total = db.Column(db.Integer())
#     totalTestResults = db.Column(db.Integer())
#     posNeg = db.Column(db.Integer())
#     fips = db.Column(db.String(50))
#     dateModified = db.Column(db.String(50))
#     dateChecked = db.Column(db.String(50))
#     notes = db.Column(db.String(100))
#     hash = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
#     latitude = db.Column(db.Float())
#     longitude = db.Column(db.Float())


#     @property
#     def as_json(self):
#         return {
#             "state": self.state, 
#             "latitude":self.latitude,
#             "longitude": self.longitude,
#             "dateChecked": self.dateChecked,
#             "positive": self.positive,
#             "negative": self.negative,
#             "hospitalized": self.hospitalized,
#             "recovered": self.recovered,
#             "total": self.total,
#             "totalTestResults": self.totalTestResults
#         }

#     def __repr__(self):
#         return f"role name => {self.name}"
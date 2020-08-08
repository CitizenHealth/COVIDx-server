from .health_checkin import HealthCheckin
from .Demographics import Demographics
from .Personal_Decisions import Personal_Decisions
from .City_State_Decisions import City_State_Decisions
from .Emotional_Health import Emotional_Health
from .Home_Conditions import Home_Conditions
from .Medical_History import Medical_History
from .Testing_Questions import Testing_Questions
from .Work_Conditions import Work_Conditions

form_response_models = {
        v.__name__.lower(): v
        for v in [
            HealthCheckin,
            Demographics,
            Personal_Decisions,
            City_State_Decisions,
            Emotional_Health,
            Home_Conditions,
            Medical_History,
            Testing_Questions,
            Work_Conditions
        ]
}
print(form_response_models)


from .health_checkin import HealthCheckin
from .demographics import Demographics

form_response_models = {
        v.__name__: v
        for v in [
            HealthCheckin,
            Demographics
        ]
}
print(form_response_models)


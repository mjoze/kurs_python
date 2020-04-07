""" Pomyśl co sprawia, że ssak jest ssakiem?
Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki."""


class Ssak:
    differentiated_teeth = True
    developed_brain = True
    warm_blooded = True
    they_care_about_children = True
    cervical_vertebrae_7 = True

    def __init__(self, body_hair, viviparous, feed_milk):
        self.body_hair = body_hair
        self.viviparous = viviparous
        self.feed_milk = feed_milk


Dziobak = Ssak(True, False, True)
print(Dziobak.__dict__)
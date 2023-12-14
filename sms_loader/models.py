from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CharField, ForeignKey, BooleanField, SET_NULL

<<<<<<< HEAD
=======
from sms_loader.variables import STATUS_MESSAGE
>>>>>>> 2dd6654 (Add Plantuml)


class Sms(models.Model):
    original_id = CharField(max_length=255)
    destinatiare = CharField(max_length=255, verbose_name='destinataire')
    proprietaire = ForeignKey(get_user_model(), verbose_name='propriétaire', on_delete=SET_NULL)
    contenu = CharField(max_length=1000)
<<<<<<< HEAD
    etat = CharField(max_length=2, choices=STATUS_MESSAGE)
=======
    status = CharField(max_length=2, choices=STATUS_MESSAGE, verbose_name='status')
>>>>>>> 2dd6654 (Add Plantuml)

    def __str__(self):
        if self.pk == None :
            return '-'
        return f'Message à {self.destinatiare}'







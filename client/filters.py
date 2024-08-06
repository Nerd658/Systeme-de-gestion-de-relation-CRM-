from commande.models import Commande

import django_filters 

class CommandFilter (django_filters.FilterSet) :
    class Meta :
        model = Commande
        fields = [
            "status",
            "produit",
            "date_creation",
            ]
        
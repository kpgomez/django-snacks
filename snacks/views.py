# from django.shortcuts import render
#
# # Create your views here.
from django.views.generic import TemplateView


# configure the view
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Physalis_peruviana_fruits_close-up.jpg",
                "title": "Golden Berry",
                "description": "Delicious cross reminiscent of a pineapple and cherry tomato",
                "reference_url": "https://en.wikipedia.org/wiki/Physalis_peruviana"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/21/-365photo_2017_edition_Food_%2832033206853%29.jpg",
                "title": "Charcuterie Board",
                "description": "Meat, cheese, fruit board",
                "reference_url": "https://en.wikipedia.org/wiki/Charcuterie_board"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Avocado_Hass_-_single_and_halved.jpg",
                "title": "Avocado",
                "description": "Delicious and smooth",
                "reference_url": "https://en.wikipedia.org/wiki/Avocado"
            }
        ]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


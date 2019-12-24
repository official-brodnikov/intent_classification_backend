# noinspection PyUnresolvedReferences
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
from intents_classifier import module
from .category_single_views import CategorySingleView
from .models import Requests
from .models import Categories


class PredictCategory(APIView):
    def get(self, request):
        body_params = QueryDict(request.body)
        content = body_params['content']
        id_predict_category = module.predict(content)
        if id_predict_category == -1:
            return Response({"result": None, "error": "The request could not be processed due to a syntax error."})
        return CategorySingleView.get(self, request, id_predict_category)

    def put(self, request):
        list_requests = []
        list_categories = []
        requests = Requests.objects.all()
        for request in requests:
            list_categories_for_one_request = request.categories.all()
            if request.is_marked_up:
                list_categories.append(list_categories_for_one_request[0].id)
                list_requests.append(request.content)

        history = module.fit(list_requests, list_categories)
        # myString = ' | '.join(list_requests)
        # myString = " | ".join(str(x) for x in list_categories)
        return Response({"result": "Модель переобучена"})


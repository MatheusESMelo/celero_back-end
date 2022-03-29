import json as simplejson


class ListModelMixin:
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)

        dict_serialized_data = simplejson.loads(simplejson.dumps(serializer.data))

        return dict_serialized_data

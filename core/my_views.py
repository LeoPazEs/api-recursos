from rest_framework.generics import ListAPIView

class DynamicSerializerListAPIView(ListAPIView): 
    fields = None
    
    def get_fields(self, *args, **kwargs): 
        """
        Return the fields to use for the serializer.
        Defaults to using `self.fields`.
        """
        assert self.fields is not None, (
            "'%s' should either include a `fields` attribute, "
            "or override the `get_serializer()` method."
            % self.__class__.__name__
        )
        return self.fields
    
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        fields = self.get_fields()
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(fields=fields, *args, **kwargs)

# English Dictionary

**Serializers**
- Allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.
- Serializers also provide deserialization

**Model Serializers**
- The model serializer class closely maps to Django model definitions
- You can create a Serializer class with fields that correspond to the model fields.
- Includes simple implementations of `.create()` and `.update()`

**Objectives**
- API Views
    - The DRF provides an API View class which subclasses Django View Claases.
    - The API View has its own response and request instances and doesn't use Django's HttpResponse or HttpRequest.
    - These are the most basic and customizable
    - They have methods that mirror the standard http methods such as get, post, put, patch, and delete.

- Django REST Framework
    - Use POST method to add new objects to the API

- Authentication schemes
    - The default authentication schemes can be set globally in the settings module by adding a setting for default authentication classes.
    - Settings include BasicAuthentication, TokenAuthentication, SessionAuthentication, RemoteUserAuthentication and CustomAuthentication.

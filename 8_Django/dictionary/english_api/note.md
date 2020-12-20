# English Dictionary

**Serializers**
- Allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.
- Serializers also provide deserialization

**Model Serializers**
- The model serializer class closely maps to Django model definitions
- You can create a Serializer class with fields that correspond to the model fields.
- Includes simple implementations of `.create()` and `.update()`
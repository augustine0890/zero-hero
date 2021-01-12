# Store App

**SerializerMethodField**
- `get_` is the prefix to the field name for the method that is called.
- Serializer for One or Many Instances
    - __many=True__ creates a list of serialized model instances
    - __many=False__ (the default) will serialize only one model instance

**Serializer Field Configuration**
- __write_only=True__ means a field can be written to but will not appear in any API response.
- __validated_data__: data that has already passed through serializer and model validation process. It's used to create or update a model.

## Django REST Framework Test Cases
**Django REST framework has four types of API test cases**
- APISimpleTestCase
- APITransactionTestCase
- APITestCase
- APILiveServerTestCase
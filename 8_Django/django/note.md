# Django App

### Making queries

`python manage.py shell`

- Creating objects
`Model(fiels=<value>, field=<value>)`

- Filtering<br>
`Model.objects.filter(fieldtext__startswith='What')
    .exclude(field_date__gte=datetime.date.today())
    .exclude(field_text__icontains="text")
    .filter(field_date__gte=datetime.date(2005, 1, 30)
)`

- Limiting<br>
`Model.objects.all()[:5]`
`Model.objects.order_by('field')[0]`
`Model.objects.order_by('field')[0:1].get()`

- Lookups<br>
`Model.objects.filter(field_date__lte='date')`
`Model.objects.get(field_text__exact='text')`
`Model.objects.filter(field_name='text_name')`
`Model.objects.filter(entry__headline__contains='Lennon')`
`Model.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)`
`Model.objects.exclude(entry__headline__contains='Lennon', entry__pub_date__year=2008)`

- Filter reference fields<br>
`from django.db.models import F`
`Model.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))`

- The pk lookup<br>
`Model.objects.filter(pk__in=[1,4,2])`
`Model.objects.filter(pk__gt=14)`

- Caching and QuerySets<br>
```
queryset = Model.objects.all()
print([p.headline for p in queryset])
print([p.pub_date for p in queryset])
model.objects.all()
model.objects.filter(id=1)
model.objects.filter(field_text__startswith="")
model.objects.get(field_date__year=<int>)
model.objects.get(id=1)
model.filter(field__contains='text')
```

- Querying JSONField<br>
```python
from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
```

`Model.objects.filter(data=None)`
`Model.objects.filter(data__isnull=True)`
`Model.objects.filter(data__owner__other_pets__0__name='Fishy')`
`Model.objects.filter(data__contains={'owner': 'Bob'})`
`Model.objects.filter(data__contained_by={'breed': 'collie', 'owner': 'Bob'})`
`Model.objects.filter(data__has_key='owner')`
`Model.objects.filter(data__has_keys=['breed', 'owner'])`
`Model.objects.filter(data__has_any_keys=['owner', 'breed'])`

- Complex lookups with Q objects<br>
```python
from django.db.models import Q
Q(question__startswith="What")

Model.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```

- Related Objects
```
e = Model.objects.get(id=3)
e.authors.all()
e.authors.count()
e.authors.filter(name__contains="John")

a = Author.objects.get(id=1)
a.entry_set.all()
a.entry_set.set([e1, e2])
a.entry_set.set([e1.pk, e2.pk])

- Blog object b with id=5:
Model.objects.filter(blog=b) # Query using object instance
Model.objects.filter(blog=b.id) # Query using id from instance
Model.objects.filter(blog=5) # Query using id directly
```

### Aggregation

```python
from django.db.models import Avg, Min, Max, Sum, FloatField, Count, Q

Model.objects.count()
Model.objects.all().aggregate(Avg('field'))
Model.objects.all().aggregate(Max('field'))
Model.objects.aggregate(Avg('field'))
Model.objects.aggregate(field_diff=Max('field', output_field=FloatField()) - Avg('field'))
Model.objects.annotate(num_field=Count('field'))
above_5 = Count('model', filter=Q(model__rating__gt=5))
below_5 = Count('model', filter=Q(model__rating__lte=5))

Model.objects.filter(field__startswith="Django").annotate(num_field=Count('field'))
```

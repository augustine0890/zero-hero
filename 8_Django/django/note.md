# Django App

**Play with the API**
`python manage.py shell`

```
model.objects.all()
model.objects.filter(id=1)
model.objects.filter(field_text__startswith="")
model.objects.get(field_date__year=<int>)
model.objects.get(id=1)

```
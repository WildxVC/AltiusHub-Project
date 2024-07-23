from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Task

@registry.register_document
class TaskDocument(Document):
    class Index:
        name = 'tasks'

    class Django:
         model = Task
         fields = [
             'title',
             'description',
             'due_date',
             'priority',
         ]
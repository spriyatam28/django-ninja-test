from ninja import NinjaAPI, Schema
from .models import HelloEntry

api = NinjaAPI()


class HelloSchema(Schema):
    name: str = "Anon"
    age: int = 18
    is_student: bool = True

@api.get("/")
def index(request):
    return "Hello, World!"

@api.get("/hello")
def get_all(request):
    entries = HelloEntry.objects.all().values("name", "age", "is_student")

    return {"values": list(entries)}


@api.post("/hello")
def hello(request, data: HelloSchema):
    entry = HelloEntry.objects.create(
        name = data.name,
        age = data.age,
        is_student = data.is_student
    )
    return {"message": f"Hello, {data.name}", "id": entry.id}


@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

import typing
import asyncio
import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class Book:
    title: str
    author: str
    password: strawberry.Private[str] = "hidden"


@strawberry.type
class Query:
    books: typing.List[Book]


def get_books():
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)

    @strawberry.field
    def name(self) -> str:
        return "Haico"


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f"Adding {title} by {author}")

        return Book(title=title, author=author)


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(
        self, target: int = 100
    ) -> typing.AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

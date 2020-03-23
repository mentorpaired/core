import graphene

import app.schema


class Query(app.schema.Query, graphene.ObjectType):
    pass


class Mutation(app.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
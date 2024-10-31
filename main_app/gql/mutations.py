from graphene import ObjectType


class









class Mutation(ObjectType):
    add_employee = AddEmployee.Field()
    add_job = AddJob.Field()










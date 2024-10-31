from graphene import Schema
from gql.schema import  Query
from gql.mutation import  Mutation
from flask import Flask
from flask_graphql import GraphQLView
from main_app.db.database import db_session, connection_url


app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

schema = Schema(query=Query, mutation=Mutation)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(host='localhost',
            # debug=True,
            port=5002)





















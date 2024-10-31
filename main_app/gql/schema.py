import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from main_app.db.database import db_session
from main_app.db.models import MissionModel, TargetModel, CityModel, TargetTypeModel


class Mission(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        Interfaces = (graphene.relay.Node, )


class Target(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypeModel
        Interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    mission_by_id = graphene.Field(Mission, id=graphene.Int(required=True))
    mission_by_date = graphene.List(Mission, beginning_date=graphene.Date(required=True), ending_date=graphene.Date(required=True))
    mission_by_country = graphene.List(Mission, country_id=graphene.Int(required=True))
    mission_by_target_industry = graphene.List(Mission, target_industry=graphene.String(required=True))
    aircraft_by_mission = graphene.List(Mission, mission_id=graphene.Int(required=True))
    attack_result_by_mission_type = graphene.List(Target, target_type=graphene.String(required=True))


    def resolve_mission_by_id(self, info, id):
        return db_session.query(MissionModel).get(id)

    def resolve_mission_by_date(self, info, beginning_date, ending_date):
        return db_session.query(MissionModel).filter(
            MissionModel.mission_date.between(beginning_date, ending_date)
        ).all()

    def resolve_mission_by_country(self, info, country_id):
        return db_session.query(MissionModel).join(
            MissionModel.targets
        ).join(
            TargetModel.city
        ).join(
            CityModel.country
        ).filter(
            CityModel.country_id == country_id
        ).all()

    def resolve_mission_by_target_industry(self, info, target_industry):
        return db_session.query(MissionModel).join(
            MissionModel.targets
        ).filter(
            TargetModel.target_industry == target_industry
        ).all()

    def resolve_aircrafts_by_mission(self, info, target_type):
        return db_session.query(TargetModel).join(
            TargetModel.target_type
        ).join(
            TargetModel.mission
        ).filter(
            TargetTypeModel.target_type_name == target_type
        ).all()



schema = graphene.Schema(query=Query)










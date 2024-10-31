from graphene import ObjectType, Mutation, Int, String, Boolean, Field, InputObjectType, Date, Float
from .schema import Mission, Target
from main_app.db.models import MissionModel, TargetModel, CountryModel, CityModel, TargetTypeModel
from main_app.db.database import db_session


class AddMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_lost = Float()

    success = Boolean()
    mission = Field(Mission)

    @staticmethod
    def mutate(root, info, mission_id, aircraft_lost, aircraft_failed, aircraft_returned, bombing_aircraft, attacking_aircraft, airborne_aircraft, mission_date):
        inserted_mission = MissionModel(aircraft_lost=aircraft_lost, aircraft_failed=aircraft_failed, aircraft_returned=aircraft_returned, bombing_aircraft=bombing_aircraft, attacking_aircraft=attacking_aircraft, airborne_aircraft=airborne_aircraft, mission_date=mission_date, mission_id=mission_id)
        db_session.add(inserted_mission)
        db_session.commit()
        db_session.refresh(inserted_mission)
        return AddMission(mission=inserted_mission, success=True)


class AddTarget(Mutation):
    class Arguments:
        target_id = Int()
        mission_id = Int()
        city_id = Int()
        target_type_id = Int()
        target_industry = String()
        target_priority = Int()

    success = Boolean()
    target = Field(Target)

    @staticmethod
    def mutate(root, info, target_priority, target_industry, target_type_id, city_id, mission_id, target_id):
        inserted_target = TargetModel(target_priority=target_priority, target_industry=target_industry, target_type_id=target_type_id, city_id=city_id, target_id=target_id, mission_id=mission_id)
        db_session.add(inserted_target)
        db_session.commit()
        db_session.refresh(inserted_target)
        return AddTarget(target=inserted_target, success=True)


class UpdateMissionResult(Mutation):
    class Arguments:
        aircraft_returned = Mission()

    mission = Field(Mission)

    @staticmethod
    def mutate(root, info, aircraft_returned):
        updated_mission = db_session.query(MissionModel).get(aircraft_returned.id)
        updated_mission.name = aircraft_returned.name
        updated_mission.email = aircraft_returned.email
        db_session.commit()
        db_session.refresh(updated_mission)
        return UpdateMissionResult(mission=updated_mission)

class Mutation(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
    update_mission = UpdateMissionResult.Field()










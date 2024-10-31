from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class MissionModel(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(String)
    attacking_aircraft = Column(String)
    bombing_aircraft = Column(String)
    aircraft_returned = Column(Integer)
    aircraft_failed = Column(Integer)
    aircraft_lost = Column(Integer)

    targets = relationship("TargetModel", back_populates="mission")

class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    city_id = Column(Integer, ForeignKey("cities.city_id"))
    target_type_id = Column(Integer, ForeignKey("targettypes.target_type_id"))
    target_industry = Column(String)
    target_priority = Column(Integer)

    mission = relationship("MissionModel", back_populates="targets")
    city = relationship("CityModel", back_populates="targets")
    target_type = relationship("TargetTypeModel", back_populates="targets")


class CountryModel(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)

    cities = relationship("CityModel", back_populates="country")


class CityModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    country_id = Column(Integer, ForeignKey("countries.country_id"))

    country = relationship("CountryModel", back_populates="cities")

    targets = relationship("TargetModel", back_populates="city")


class TargetTypeModel(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)

    targets = relationship("TargetModel", back_populates="target_type")










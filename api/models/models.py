from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BusSchedule(Base):
    __tablename__ = "bus_schedule"
    id = Column(Integer, primary_key=True, index=True)
    bus_name = Column(String, index=True)
    station = Column(String)
    time = Column(String)

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    bus_name = Column(String, ForeignKey('bus_schedule.bus_name'))
    station = Column(String, ForeignKey('bus_schedule.station'))
    notify_before = Column(Integer)
    email = Column(String)

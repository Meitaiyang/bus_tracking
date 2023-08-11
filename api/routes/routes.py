from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from api.models.models import BusSchedule, Subscription
from api.database import SessionLocal, get_db

router = APIRouter()

@router.get("/bus_schedule/{bus}/{station}")
async def get_schedule(bus: str, station: str, db: Session = Depends(get_db)):
    bus_schedule = db.query(BusSchedule).filter(BusSchedule.bus_name == bus, BusSchedule.station == station).first()
    if bus_schedule:
        return {"arrival_time": bus_schedule.time}
    raise HTTPException(status_code=404, detail="Bus or station not found")

@router.post("/subscribe/")
async def subscribe(subscription: Subscription, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    background_tasks.add_task(send_email, subscription.email, "You have successfully subscribed!")
    return {"status": "success"}

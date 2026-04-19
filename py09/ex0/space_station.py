from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0, le=100)
    oxygen_level: float = Field(..., ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status_map = {True: 'Operational', False: 'Offline'}
        print(f"Status: {status_map[station.is_operational]}\n")

    except ValidationError as e:
        print(f"Unexpected error: {e}")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Deep Space Nine",
            crew_size=25,
            power_level=80,
            oxygen_level=92,
            last_maintenance=datetime.now()
        )

    except ValidationError as e:
        print("========================================")
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

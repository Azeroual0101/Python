from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    # ✅ VALID
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2024-05-01T10:00:00"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
        )

        print("Valid contact:", contact)

    except ValidationError as e:
        print("Unexpected error:", e)

    print("\n" + "=" * 40)

    # ❌ INVALID
    try:
        AlienContact(
            contact_id="BAD",
            timestamp=datetime.fromisoformat("2024-05-01T10:00:00"),
            location="X",
            contact_type=ContactType.telepathic,
            signal_strength=15.0,
            duration_minutes=0,
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()

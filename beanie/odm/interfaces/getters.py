from abc import abstractmethod

from motor.motor_asyncio import AsyncIOMotorCollection

from beanie.odm.settings.base import ItemSettings


class OtherGettersInterface:
    @classmethod
    @abstractmethod
    def get_settings(cls) -> ItemSettings:
        pass

    @classmethod
    def get_motor_collection(cls) -> AsyncIOMotorCollection:
        settings = cls.get_settings()
        if settings.motor_collection is None:
            raise ValueError("Motor collection is not set")

        if settings.read_preference or settings.write_concern:
            return settings.motor_collection.with_options(
                read_preference=settings.read_preference,
                write_concern=settings.write_concern,
            )
        return settings.motor_collection

    @classmethod
    def get_collection_name(cls) -> str:
        return cls.get_settings().name  # type: ignore

    @classmethod
    def get_bson_encoders(cls):
        return cls.get_settings().bson_encoders

    @classmethod
    def get_link_fields(cls):
        return None

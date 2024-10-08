import uuid
from typing import Type, Any, List

from loguru import logger


class CRUDServiceMixin:
    def __init__(self, repository: Any) -> None:
        self._repo = repository

    async def list(self, limit: int, offset: int, **filters) -> List[Type[Any]]:
        logger.debug(f"{self._repo.model.__name__} - Service - list")
        result = await self._repo.list(limit, offset, **filters)
        return result

    async def get(self, id: uuid.UUID) -> Type[Any]:
        logger.debug(f"{self._repo.model.__name__} - Service - get_by_id")
        result = await self._repo.get(id)
        return result

    async def create(self, entity: Type[Any]) -> Type[Any]:
        logger.debug(f"{self._repo.model.__name__} - Service - create")
        entity.id = uuid.uuid4()
        result = await self._repo.create(entity)
        return result

    async def update(self, id: uuid.UUID, update_data: dict) -> Type[Any]:
        logger.debug(f"{self._repo.model.__name__} - Service - update")
        result = await self._repo.update(id, update_data)
        return result

    async def delete(self, id: uuid.UUID) -> None:
        logger.debug(f"{self._repo.model.__name__} - Service - delete")
        entity = await self._repo.get(id)
        await self._repo.delete(entity)
        return None

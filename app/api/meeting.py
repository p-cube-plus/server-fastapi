from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.meeting import (
    MeetigPost,
    MeetingDTO,
    MeetingParams,
    MeetingPatch,
    MeetingPut,
)
from app.service.meeting import MeetingService

router = CustomAPIRouter(
    prefix="/meetings",
)


@router.get("", response_model=list[MeetingDTO])
async def get_meeting_list(
    meeting_params: Annotated[MeetingParams, Depends()],
    service: Annotated[MeetingService, Depends()],
):
    meeting_list = await service.get(**meeting_params.dict())
    return meeting_list


@router.get("/{id}", response_model=MeetingDTO)
async def get_meeting_by_id(id: int, service: Annotated[MeetingService, Depends()]):
    meeting = await service.get(id=id)
    return meeting[0]


@router.post("", response_model=MeetingDTO)
async def create_meeting(
    meeting_post: MeetigPost, service: Annotated[MeetingService, Depends()]
):
    new_meeting = await service.create([meeting_post])
    return new_meeting[0]


@router.put("/{id}", response_model=MeetingDTO)
async def replace_meeting(
    id: int,
    meeting_put: MeetingPut,
    service: Annotated[MeetingService, Depends()],
):
    replaced_meeting = await service.update(meeting_put, exclude_unset=False, id=id)
    return replaced_meeting[0]


@router.patch("/{id}", response_model=MeetingDTO)
async def update_meeting(
    id: int,
    meeting_patch: MeetingPatch,
    service: Annotated[MeetingService, Depends()],
):
    updated_meeting = await service.update(meeting_patch, id=id)
    return updated_meeting[0]


@router.delete("/{id}", response_model=MeetingDTO)
async def delete_meeting(id: int, service: Annotated[MeetingService, Depends()]):
    deleted_meeting = await service.delete(id=id)
    return deleted_meeting[0]

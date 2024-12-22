from typing import Annotated

from fastapi import APIRouter, Depends

from app.dto.meeting import MeetingCreate, MeetingRead, MeetingUpdate
from app.service.meeting import MeetingService

router = APIRouter(
    prefix="/meeting",
)


@router.get("", response_model=list[MeetingRead])
async def get_meeting_list(service: Annotated[MeetingService, Depends()]):
    meeting_list = await service.get_all()
    return meeting_list


@router.get("/{id}", response_model=MeetingRead)
async def get_meeting_by_id(id: str, service: Annotated[MeetingService, Depends()]):
    meeting = await service.get(id)
    return meeting


@router.post("", response_model=MeetingRead)
async def create_meeting(
    meeting: MeetingCreate, service: Annotated[MeetingService, Depends()]
):
    new_meeting = await service.create(meeting)
    return new_meeting


@router.put("/{id}", response_model=MeetingRead)
async def update_meeting(
    id: int, meeting: MeetingUpdate, service: Annotated[MeetingService, Depends()]
):
    updated_meeting = await service.update(id, meeting)
    return updated_meeting


@router.delete("/{id}", response_model=MeetingRead)
async def delete_meeting(id: int, service: Annotated[MeetingService, Depends()]):
    deleted_meeting = await service.delete(id)
    return deleted_meeting

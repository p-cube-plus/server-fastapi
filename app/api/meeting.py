from typing import Annotated

from fastapi import APIRouter, Depends

from app.dto.meeting import MeetingCreate, MeetingDelete, MeetingRead, MeetingUpdate
from app.service.meeting import MeetingService

router = APIRouter(
    prefix="/meeting",
)


@router.get("", response_model=list[MeetingRead])
async def get_meeting_list(service: Annotated[MeetingService, Depends()]):
    meeting_list = await service.get_all()
    return meeting_list


@router.get("/{meeting_id}", response_model=MeetingRead)
async def get_meeting_by_id(
    meeting_id: str, service: Annotated[MeetingService, Depends()]
):
    meeting = await service.get_by_id(meeting_id)
    return meeting


@router.post("", response_model=MeetingRead)
async def create_meeting(
    meeting: MeetingCreate, service: Annotated[MeetingService, Depends()]
):
    new_meeting = await service.create(meeting)
    return new_meeting


@router.put("", response_model=MeetingRead)
async def update_meeting(
    meeting: MeetingUpdate, service: Annotated[MeetingService, Depends()]
):
    updated_meeting = await service.update(meeting)
    return updated_meeting


@router.delete("", response_model=MeetingRead)
async def delete_meeting(
    meeting: MeetingDelete, service: Annotated[MeetingService, Depends()]
):
    deleted_meeting = await service.delete(meeting)
    return deleted_meeting

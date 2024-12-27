from typing import Annotated

from fastapi import APIRouter, Depends, Request

from app.dto.meeting import MeetingPayload, MeetingRequest, MeetingResponse
from app.service.meeting import MeetingService

router = APIRouter(
    prefix="/meetings",
)


@router.get("", response_model=list[MeetingResponse])
async def get_meeting_list(
    request: Request,
    meeting_payload: Annotated[MeetingPayload, Depends()],
    service: Annotated[MeetingService, Depends()],
):
    meeting_list = await service.get_all(MeetingPayload(**request.query_params))
    return meeting_list


@router.get("/{id}", response_model=MeetingResponse)
async def get_meeting_by_id(id: int, service: Annotated[MeetingService, Depends()]):
    meeting = await service.get(id)
    return meeting


@router.post("", response_model=MeetingResponse)
async def create_meeting(
    meeting: MeetingRequest, service: Annotated[MeetingService, Depends()]
):
    new_meeting = await service.create(meeting)
    return new_meeting


@router.put("/{id}", response_model=MeetingResponse)
async def update_meeting(
    id: int, meeting: MeetingPayload, service: Annotated[MeetingService, Depends()]
):
    updated_meeting = await service.update(id, meeting)
    return updated_meeting


@router.delete("/{id}", response_model=MeetingResponse)
async def delete_meeting(id: int, service: Annotated[MeetingService, Depends()]):
    deleted_meeting = await service.delete(id)
    return deleted_meeting

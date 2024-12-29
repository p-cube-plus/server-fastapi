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
    meeting_list = await service.get(**request.query_params)
    return meeting_list


@router.get("/{id}", response_model=MeetingResponse)
async def get_meeting_by_id(id: int, service: Annotated[MeetingService, Depends()]):
    meeting = await service.get(id=id)
    return meeting[0]


@router.post("", response_model=MeetingResponse)
async def create_meeting(
    meeting_request: MeetingRequest, service: Annotated[MeetingService, Depends()]
):
    new_meeting = await service.create([meeting_request])
    return new_meeting[0]


@router.put("/{id}", response_model=MeetingResponse)
async def replace_meeting(
    id: int,
    meeting_request: MeetingRequest,
    service: Annotated[MeetingService, Depends()],
):
    replaced_meeting = await service.replace(meeting_request, id=id)
    return replaced_meeting[0]


@router.patch("/{id}", response_model=MeetingResponse)
async def update_meeting(
    id: int,
    meeting_payload: MeetingPayload,
    service: Annotated[MeetingService, Depends()],
):
    updated_meeting = await service.update(meeting_payload, id=id)
    return updated_meeting[0]


@router.delete("/{id}", response_model=MeetingResponse)
async def delete_meeting(id: int, service: Annotated[MeetingService, Depends()]):
    deleted_meeting = await service.delete(id=id)
    return deleted_meeting[0]

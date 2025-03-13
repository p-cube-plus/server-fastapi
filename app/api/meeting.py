from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.meeting import (
    MeetingDTO,
    MeetingParams,
    MeetingPatch,
    MeetingPost,
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
    meeting_list = await service.get(id=id)
    if not meeting_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Meeting not found"
        )
    return meeting_list[0]


@router.post("", response_model=MeetingDTO)
async def create_meeting(
    meeting_post: MeetingPost, service: Annotated[MeetingService, Depends()]
):
    new_meeting_list = await service.create([meeting_post])
    return new_meeting_list[0]


@router.put("/{id}", response_model=MeetingDTO)
async def replace_meeting(
    id: int,
    meeting_put: MeetingPut,
    service: Annotated[MeetingService, Depends()],
):
    replaced_meeting_list = await service.update(
        meeting_put, exclude_unset=False, id=id
    )
    if not replaced_meeting_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Meeting not found"
        )
    return replaced_meeting_list[0]


@router.patch("/{id}", response_model=MeetingDTO)
async def update_meeting(
    id: int,
    meeting_patch: MeetingPatch,
    service: Annotated[MeetingService, Depends()],
):
    updated_meeting_list = await service.update(meeting_patch, id=id)
    if not updated_meeting_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Meeting not found"
        )
    return updated_meeting_list[0]


@router.delete("/{id}", response_model=MeetingDTO)
async def delete_meeting(id: int, service: Annotated[MeetingService, Depends()]):
    deleted_meeting_list = await service.delete(id=id)
    if not deleted_meeting_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Meeting not found"
        )
    return deleted_meeting_list[0]

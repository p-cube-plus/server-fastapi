from typing import Annotated

from fastapi import Depends

from app.core.routing import CustomAPIRouter
from app.dto.attendance_member import (
    AttendanceMemberDTO,
    AttendanceMemberPost,
    AttendanceUserParams,
    AttendanceUserPatch,
    AttendanceUserPost,
    AttendanceUserPut,
)
from app.service.attendance_member import AttendanceMemberService

router = CustomAPIRouter(
    prefix="/attendances/{attendance_id}/users",
)


@router.get("", response_model=list[AttendanceMemberDTO])
async def get_attendance_user_list(
    attendance_id: int,
    attendance_user_params: Annotated[AttendanceUserParams, Depends()],
    service: Annotated[AttendanceMemberService, Depends()],
):
    attendance_user_list = await service.get(
        attendance_id=attendance_id, **attendance_user_params.dict()
    )
    return attendance_user_list


@router.get("/{user_id}", response_model=AttendanceMemberDTO)
async def get_attendance_user_by_user_id(
    attendance_id: int,
    user_id: int,
    service: Annotated[AttendanceMemberService, Depends()],
):
    attendance_user = await service.get(attendance_id=attendance_id, user_id=user_id)
    return attendance_user[0]


@router.post("", response_model=AttendanceMemberDTO)
async def create_attendance_user(
    attendance_id: int,
    attendance_user_post: AttendanceUserPost,
    service: Annotated[AttendanceMemberService, Depends()],
):
    new_attendance_user = await service.create(
        [
            AttendanceMemberPost(
                attendance_id=attendance_id, **attendance_user_post.dict()
            )
        ]
    )
    return new_attendance_user[0]


@router.put("/{user_id}", response_model=AttendanceMemberDTO)
async def update_attendance_user(
    attendance_id: int,
    user_id: int,
    attendance_user_put: AttendanceUserPut,
    service: Annotated[AttendanceMemberService, Depends()],
):
    updated_attendance_user = await service.update(
        attendance_user_put,
        exclude_unset=False,
        attendance_id=attendance_id,
        user_id=user_id,
    )
    return updated_attendance_user[0]


@router.patch("/{user_id}", response_model=AttendanceMemberDTO)
async def patch_attendance_user(
    attendance_id: int,
    user_id: int,
    attendance_user_patch: AttendanceUserPatch,
    service: Annotated[AttendanceMemberService, Depends()],
):
    patched_attendance_user = await service.update(
        attendance_user_patch, attendance_id=attendance_id, user_id=user_id
    )
    return patched_attendance_user[0]


@router.delete("/{user_id}", response_model=AttendanceMemberDTO)
async def delete_attendance_user(
    attendance_id: int,
    user_id: int,
    service: Annotated[AttendanceMemberService, Depends()],
):
    deleted_attendance_user = await service.delete(
        attendance_id=attendance_id, user_id=user_id
    )
    return deleted_attendance_user[0]

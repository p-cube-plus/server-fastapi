from typing import Annotated

from fastapi import Depends, HTTPException, status

from app.core.routing import CustomAPIRouter
from app.dto.membership import (
    MembershipDTO,
    MembershipParams,
    MembershipPatch,
    MembershipPost,
    MembershipPut,
)
from app.service.membership import MembershipService

router = CustomAPIRouter(
    prefix="/memberships",
)


@router.get("", response_model=list[MembershipDTO])
async def get_membership_list(
    membership_params: Annotated[MembershipParams, Depends()],
    service: Annotated[MembershipService, Depends()],
):
    membership_list = await service.get(**membership_params.dict())
    return membership_list


@router.get("/{user_id}", response_model=MembershipDTO)
async def get_membership_by_user_id(
    user_id: int, service: Annotated[MembershipService, Depends()]
):
    membership_list = await service.get(user_id=user_id)
    if not membership_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Membership not found"
        )
    return membership_list[0]


@router.post("", response_model=MembershipDTO)
async def create_membership(
    membership_post: MembershipPost, service: Annotated[MembershipService, Depends()]
):
    new_membership_list = await service.create([membership_post])
    return new_membership_list[0]


@router.put("/{user_id}", response_model=MembershipDTO)
async def replace_membership(
    user_id: int,
    membership_put: MembershipPut,
    service: Annotated[MembershipService, Depends()],
):
    replaced_membership_list = await service.update(
        membership_put, exclude_unset=False, user_id=user_id
    )
    if not replaced_membership_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Membership not found"
        )
    return replaced_membership_list[0]


@router.patch("/{user_id}", response_model=MembershipDTO)
async def update_membership(
    user_id: int,
    membership_patch: MembershipPatch,
    service: Annotated[MembershipService, Depends()],
):
    updated_membership_list = await service.update(membership_patch, user_id=user_id)
    if not updated_membership_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Membership not found"
        )
    return updated_membership_list[0]


@router.delete("/{user_id}", response_model=MembershipDTO)
async def delete_membership(
    user_id: int, service: Annotated[MembershipService, Depends()]
):
    deleted_membership_list = await service.delete(user_id=user_id)
    if not deleted_membership_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Membership not found"
        )
    return deleted_membership_list[0]

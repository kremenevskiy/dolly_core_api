from fastapi import APIRouter
from pydantic import BaseModel

from src.exceptions import NotFound
from src.logger import logger
from src.schemas import OKResponse, OKResponseWithUserID
from src.user import model, service

user_router = APIRouter(prefix='/user')


@user_router.post('/create-new-user')
async def create_new_user(user_request: model.User) -> OKResponse:
    await service.create_new_user(user_request)

    return OKResponse(status=True)


# admin
@user_router.get('/add-whitelist')
async def add_user_to_whitelist(username: str) -> OKResponseWithUserID:
    user_id = await service.add_user_to_whitelist(username=username)
    return OKResponseWithUserID(status=True, user_id=user_id)


@user_router.get('/delete-whitelist')
async def delete_user_from_whitelist(username: str) -> OKResponse:
    await service.delete_user_from_whitelist(username=username)
    return OKResponse(status=True)


@user_router.get('/find/profile')
async def find_user(username: str) -> model.UserProfile:
    logger.info(f'find user: username={username}')
    user = await service.find_user(username=username)

    logger.info(f'user found: user={user}')

    return await service.get_user_profile(user)


@user_router.get('/profile/{user_id}')
async def user_profile(user_id: str) -> model.UserProfile:
    user = await service.get_user(user_id)

    return await service.get_user_profile(user)


class SubscribeRequest(BaseModel):
    subscription_id: int


class SubscribeResponse(OKResponse):
    referral_info: model.ReferralBonusGenerations | None = None


@user_router.post('/{user_id}/subscribe')
async def user_buy_subscription(user_id: str, req: SubscribeRequest) -> SubscribeResponse:
    resp = SubscribeResponse(status=True)

    additional = await service.subscribe_user(
        user_id=user_id,
        subscription_id=req.subscription_id,
    )

    if additional is not None:
        resp.referral_info = additional.referral_info

    return resp


@user_router.post('/{user_id}/add-payment-info')
async def user_add_payment_info(
    user_id: str,
    payment_details: model.PaymentDetails,
) -> OKResponse:
    await service.store_user_payment(
        user_id=user_id,
        payment_details=payment_details.model_dump(),
    )
    return OKResponse(status=True)


@user_router.get('/{user_id}/subscription')
async def active_subscription(user_id: str) -> OKResponse:
    sub = await service.get_active_subscribe(user_id)
    if sub is None:
        raise NotFound()

    return OKResponse(status=True)


@user_router.get('/{user_id}/limit/model')
async def check_user_model_limit(user_id: str) -> OKResponse:
    await service.check_subscription_limits(user_id, model.OperationType.CREATE_MODEL)

    return OKResponse(status=True)


class UpdateLimitsRequest(BaseModel):
    update_generation_count: int
    update_models_count: int


@user_router.put('/{user_id}/admin/limits')
async def add_user_limits(user_id: str, req: UpdateLimitsRequest) -> OKResponse:
    await service.update_user_limits(user_id, req.update_generation_count, req.update_models_count)

    return OKResponse(status=True)


@user_router.post('/{user_id}/refund')
async def refund_user(user_id: str, req: SubscribeRequest) -> OKResponse:
    await service.refund_user(user_id, req.subscription_id)

    return OKResponse(status=True)

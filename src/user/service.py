from datetime import UTC, datetime, timedelta

from src.model import service as model_service
from src.subcription import service as sub_service
from src.user import exception
from src.user.model import OperationType, User, UserSubscriptionState
from src.user.repository import UserRepository

user_repository = UserRepository()


async def create_new_user(user: User) -> None:
    await user_repository.create_new_user(user)


async def get_user_id_from_username(username: str) -> str:
    user_id = await user_repository.get_user_id_from_user_username(username)
    if user_id is None:
        raise exception.UserNotFound()
    return user_id


async def add_user_to_whitelist(username: str) -> None:
    user_id = await get_user_id_from_username(username=username)
    await user_repository.add_user_to_whitelist(user_id)


async def subcribe_user(user_id: str, sub_id: str):
    subcription = await sub_service.get_subcription(sub_id)

    end_date = datetime.now(UTC) + timedelta(seconds=subcription.duration)

    state = UserSubscriptionState(
        user_id=user_id,
        subcription_id=sub_id,
        start_date=datetime.now(UTC),
        end_date=end_date,
        photo_by_promnt_count=subcription.photo_by_prompt_limit,
        photo_by_image_count=subcription.photo_by_image_limit,
    )

    await user_repository.save_user_sub_state(state)


async def update_sub_state(user: User, operation: OperationType) -> None:
    user_sub_state = await user_repository.get_user_subcription_state(user.user_id)

    if operation == OperationType.GENERATE_BY_IMAGE:
        user_sub_state.photo_by_image_count -= 1
        if user_sub_state.photo_by_image_count <= 0:
            raise OperationOutOfLimit(operation)

    elif operation == OperationType.GENERATE_BY_PROMNT:
        user_sub_state.photo_by_promnt_count -= 1
        if user_sub_state.photo_by_promnt_count <= 0:
            raise OperationOutOfLimit(operation)

    elif operation == OperationType.CREATE_MODEL:
        count = await model_service.get_user_models_count(user.user_id)

        if count >= user.models_max:
            raise OperationOutOfLimit(operation)

    await user_repository.save_user_sub_state(user_sub_state)

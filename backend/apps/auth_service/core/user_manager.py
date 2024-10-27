import logging
import uuid
from typing import Optional, TYPE_CHECKING


from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, IntegerIDMixin

from ..models.user import User
from ..dependencies.users import get_user_db

from ..types.user_id import UserIdType

SECRET = "SECRET"

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from fastapi import Request


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self,
        user: User,
        request: "Optional[Request]" = None,
    ):
        log.warning(
            "User %r has registered",
            user.id,
        )

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: "Optional[Request]" = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: "Optional[Request]" = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )
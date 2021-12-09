import typing

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsPrivate(BoundFilter):
    key = "is_private"

    def __init__(self, is_private: typing.Optional[bool] = None):
        self.is_private = is_private

    async def check(self, message: types.Message) -> bool:
        if self.is_private is None:
            return
        if not self.is_private:
            return False
        return message.chat.type == types.ChatType.PRIVATE

import random

from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import support_ids
from loader import dp

support_callback = CallbackData("ask_support", "messages", "user_id", "as_user")
cancel_support_callback = CallbackData("cancel_support", "user_id")

async def check_support_available(support_id):
    state = dp.current_state(chat=support_id, user=support_id)
    state_str = str(
        await state.get_data()
    )
    if state_str == "in_support":
        return
    else:
        return support_id

async def get_support_manager():
    random.shuffle(support_ids)
    for support_id in support_ids:
        support_id = await check_support_available(support_id)
        if support_id:
            return support_id
    else:
        return

async def support_keyboard(messages, user_id=None):
    if user_id:
        contact_id = int(user_id)
        as_user = "no"
        text = "Foydalanuvchiga javob berish"
    else:
        contact_id = await get_support_manager()
        as_user = "yes"
        if messages == "many" and contact_id is None:
            return False
        elif messages == "one" and contact_id is None:
            contact_id = random.choice(support_ids)
        if messages == "one":
            text = "Texnik yordamga 1 ta xabar yozing"
        else:
            text = "Operatorga yozing"
    keyboard = InlineKeyboardMarkup()
    
    keyboard.add(
        InlineKeyboardButton(
            text=text,
            callback_data=support_callback.new(
                messages=messages,
                user_id=contact_id,
                as_user=as_user
            )
        )
    )
    
    if messages == "many":
        keyboard.add(
            InlineKeyboardButton(
                text="Seansni tugatish",
                callback_data=cancel_support_callback.new(
                    user_id=contact_id
                )
            )
        )
    return keyboard
    
    


def cancel_support(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Seansni tugatish",
                    callback_data=cancel_support_callback.new(
                        user_id=user_id
                    )
                )
            ]
        ]
    )
    
    
    
    
    
    
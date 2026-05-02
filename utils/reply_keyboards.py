"""Reply keyboard builders for role-aware bottom menu."""

from telebot import types

from constants.menu_labels import (
    BTN_CONTACT_OWNER,
    BTN_COMMANDS,
    BTN_GUIDE,
    BTN_GET_VIP,
    BTN_HIDE,
    BTN_MY_STATS,
    BTN_OWNER_PANEL,
    BTN_PING,
    BTN_REDEEM,
    BTN_SUDO_PANEL,
    BTN_SUPPORT,
)

PLACEHOLDER = "Choose an option or type a command..."


def _base(placeholder=PLACEHOLDER):
    kb = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False,
        is_persistent=True,
        input_field_placeholder=placeholder,
    )
    return kb


def get_main_menu_keyboard(role="PREMIUM"):
    """Help-domain compact layout."""
    kb = _base()
    kb.row(
        types.KeyboardButton(BTN_GET_VIP),
        types.KeyboardButton(BTN_SUPPORT),
    )
    kb.row(
        types.KeyboardButton(BTN_PING),
        types.KeyboardButton(BTN_MY_STATS),
    )
    kb.row(types.KeyboardButton(BTN_GUIDE))
    kb.row(types.KeyboardButton(BTN_HIDE))
    if role == "OWNER":
        kb.row(types.KeyboardButton(BTN_OWNER_PANEL))
    elif role == "SUDO":
        kb.row(types.KeyboardButton(BTN_SUDO_PANEL))
    return kb


def get_guest_keyboard():
    kb = _base("Redeem a code or contact owner...")
    kb.row(types.KeyboardButton(BTN_REDEEM))
    kb.row(
        types.KeyboardButton(BTN_CONTACT_OWNER),
        types.KeyboardButton(BTN_GUIDE),
    )
    kb.row(types.KeyboardButton(BTN_HIDE))
    return kb


def resolve_keyboard_for_role(role):
    if role == "GUEST":
        return get_guest_keyboard()
    return get_main_menu_keyboard(role)


def hide_keyboard():
    return types.ReplyKeyboardRemove()

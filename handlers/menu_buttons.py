"""Exact-text routing for persistent reply keyboard buttons."""

from constants.menu_labels import (
    BTN_CONTACT_OWNER,
    BTN_GET_VIP,
    BTN_GUIDE,
    BTN_HIDE,
    BTN_MY_STATS,
    BTN_OWNER_PANEL,
    BTN_PING,
    BTN_REDEEM,
    BTN_SUDO_PANEL,
    BTN_SUPPORT,
)


def register_menu_button_handlers(bot, routes):
    """Wire button text -> existing route callback (no business logic duplication)."""

    bot.register_message_handler(
        routes["get_vip"],
        func=lambda m: (getattr(m, "text", "") == BTN_GET_VIP),
    )
    bot.register_message_handler(
        routes["support"],
        func=lambda m: (getattr(m, "text", "") == BTN_SUPPORT),
    )
    bot.register_message_handler(
        routes["ping"],
        func=lambda m: (getattr(m, "text", "") == BTN_PING),
    )
    bot.register_message_handler(
        routes["my_stats"],
        func=lambda m: (getattr(m, "text", "") == BTN_MY_STATS),
    )
    bot.register_message_handler(
        routes["guide"],
        func=lambda m: (getattr(m, "text", "") == BTN_GUIDE),
    )
    bot.register_message_handler(
        routes["hide"],
        func=lambda m: (getattr(m, "text", "") == BTN_HIDE),
    )
    bot.register_message_handler(
        routes["owner_panel"],
        func=lambda m: (getattr(m, "text", "") == BTN_OWNER_PANEL),
    )
    bot.register_message_handler(
        routes["sudo_panel"],
        func=lambda m: (getattr(m, "text", "") == BTN_SUDO_PANEL),
    )
    bot.register_message_handler(
        routes["redeem"],
        func=lambda m: (getattr(m, "text", "") == BTN_REDEEM),
    )
    bot.register_message_handler(
        routes["contact_owner"],
        func=lambda m: (getattr(m, "text", "") == BTN_CONTACT_OWNER),
    )

"""Reply-keyboard labels (single source of truth)."""

# ==== Help-domain primary menu ====
BTN_GET_VIP = "🚀 Get VIP"
BTN_SUPPORT = "💬 Support"
BTN_PING = "⚡ Ping"
BTN_MY_STATS = "📊 My Stats"
BTN_GUIDE = "📖 Guide"
BTN_HIDE = "🙈 Hide"

# Optional extra action for compact help menu
BTN_COMMANDS = "📋 Commands"

# ==== Role-specific ====
BTN_OWNER_PANEL = "👑 Owner Panel"
BTN_SUDO_PANEL = "🛡 SUDO Panel"
BTN_REDEEM = "🎟 Redeem Code"
BTN_CONTACT_OWNER = "💬 Contact Owner"

# ==== Legacy aliases (kept for backwards compatibility) ====
BTN_PLACE_ORDER = BTN_GET_VIP
BTN_TOPUP = BTN_SUPPORT
BTN_BALANCE = BTN_PING
BTN_REFER = BTN_MY_STATS
BTN_HISTORY = BTN_COMMANDS

# Aggregate sets for quick membership checks
ALL_PRIMARY = {
    BTN_GET_VIP,
    BTN_SUPPORT,
    BTN_PING,
    BTN_MY_STATS,
    BTN_COMMANDS,
    BTN_GUIDE,
    BTN_HIDE,
}
ALL_ADMIN = {BTN_OWNER_PANEL, BTN_SUDO_PANEL}
ALL_GUEST = {BTN_REDEEM, BTN_CONTACT_OWNER, BTN_GUIDE, BTN_HIDE}

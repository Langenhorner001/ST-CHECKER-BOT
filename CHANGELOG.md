# Changelog

## feat(ui): persistent bottom reply keyboard (ENH-REPLY-KB-001)

- Added centralized button labels in `constants/menu_labels.py`.
- Added role-aware persistent reply keyboard factory in `utils/reply_keyboards.py`.
- Added exact-text menu routing module in `handlers/menu_buttons.py`.
- Integrated persistent menu into `/start`, `/menu`, and `/cmds` flow in `file1.py`.
- Wired button taps to existing features (help, history, support, redeem, status/stats panels).
- Added role-aware keyboard refresh on redeem success and VIP grant/remove notifications.
- Registered menu handlers at startup and exposed `/menu` in bot command list.

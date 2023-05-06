# =============================================================================
# Margatsni Public CLI Action
# =============================================================================
#
# Logic of the `pub` action.
#
from minet.cli.argparse import command, ConfigAction
from minet.cli.instagram import (
    INSTAGRAM_COMMENTS_SUBCOMMAND,
    INSTAGRAM_HASHTAG_SUBCOMMAND,
    INSTAGRAM_POST_INFOS_SUBCOMMAND,
    INSTAGRAM_USER_FOLLOWERS_SUBCOMMAND,
    INSTAGRAM_USER_FOLLOWING_SUBCOMMAND,
    INSTAGRAM_USER_INFOS_SUBCOMMAND,
    INSTAGRAM_USER_POSTS_SUBCOMMAND
)

PUBLIC_COMMAND = command(
    "public",
    "margatsni.cli.public",
    aliases=["pub"],
    title="Margatsni Public Command",
    description="""
        Gather public data from Instagram.
    """,
    common_arguments=[
        {
            "flags": ["-c", "--cookie"],
            "help": 'Authenticated cookie to use or browser from which to extract it (supports "firefox", "chrome", "chromium", "opera" and "edge").',
            "default": "firefox",
            "rc_key": ["instagram", "cookie"],
            "action": ConfigAction,
        }
    ],
    subcommands=[
        INSTAGRAM_COMMENTS_SUBCOMMAND,
        INSTAGRAM_HASHTAG_SUBCOMMAND,
        INSTAGRAM_POST_INFOS_SUBCOMMAND,
        INSTAGRAM_USER_FOLLOWERS_SUBCOMMAND,
        INSTAGRAM_USER_FOLLOWING_SUBCOMMAND,
        INSTAGRAM_USER_INFOS_SUBCOMMAND,
        INSTAGRAM_USER_POSTS_SUBCOMMAND
    ],
)

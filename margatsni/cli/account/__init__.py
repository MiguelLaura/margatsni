# =============================================================================
# Margatsni Account CLI Action
# =============================================================================
#
# Logic of the `account` action.
#
from minet.cli.argparse import command, subcommand, ConfigAction


ACCOUNT_EXPLORE_SUBCOMMAND = subcommand(
    "explore",
    "margatsni.cli.account.explore",
    title="Account explore",
    description="""
        Scrape Instagram explore feed.

        This requires to be logged in to an Instagram account, so
        by default this command will attempt to grab the relevant
        authentication cookies from a local Firefox browser.

        If you want to grab cookies from another browser or want
        to directly pass the cookie as a string, check out the
        -c/--cookie flag.

        Beware, instagram only provides temporary links, not permalinks,
        for profile picture urls retrieved as the "profile_pic_url" in
        the result. Be sure to download them fast if you need them (you can
        use the `minet fetch` command for that, and won't need to use cookies).
    """,
    epilog="""
        example:
            $ margatsni account explore 5 > explore.csv
    """,
    variadic_input={"dummy_column": "limit"},
)

ACCOUNT_COMMAND = command(
    "account",
    "margatsni.cli.account",
    title="Margatsni Account Command",
    description="""
        Gather account-specific data from Instagram.
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
        ACCOUNT_EXPLORE_SUBCOMMAND,
    ],
)

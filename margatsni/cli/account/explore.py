# =============================================================================
# Margatsni Instagram Hashtag CLI Action
# =============================================================================
#
# Logic of the `account hashtag` action.
#
from itertools import islice
from minet.cli.instagram.utils import with_instagram_fatal_errors
from minet.instagram.constants import INSTAGRAM_POST_CSV_HEADERS
from minet.cli.utils import with_enricher_and_loading_bar

from margatsni.cli.utils import with_enricher_and_loading_bar_no_file
from margatsni.account.api_scraper import AccountInstagramAPIScraper


@with_instagram_fatal_errors
@with_enricher_and_loading_bar(
    headers=INSTAGRAM_POST_CSV_HEADERS,
    title="Scraping posts",
    unit="limit",
    nested=True,
    sub_unit="posts",
)
def action(cli_args, enricher, loading_bar):
    client = AccountInstagramAPIScraper(cookie=cli_args.cookie)

    for _, row, limit in enricher.enumerate_cells(
        cli_args.column, with_rows=True, start=1
    ):
        with loading_bar.step(limit):
            generator = client.get_explore_feed()

            generator = islice(generator, int(limit))

            for post in generator:
                enricher.writerow(row, post.as_csv_row())
                loading_bar.nested_advance()

# =============================================================================
# Margatsni Instagram Hashtag CLI Action
# =============================================================================
#
# Logic of the `account hashtag` action.
#
from casanova.utils import CsvCellIO
from itertools import islice
from minet.cli.instagram.utils import with_instagram_fatal_errors
from minet.instagram.constants import INSTAGRAM_POST_CSV_HEADERS

from margatsni.cli.utils import with_enricher_and_loading_bar
from margatsni.account.api_scraper import AccountInstagramAPIScraper


@with_instagram_fatal_errors
@with_enricher_and_loading_bar(
    headers=INSTAGRAM_POST_CSV_HEADERS,
    title="Scraping posts",
    unit="posts",
    get_input=lambda cli_args: CsvCellIO(cli_args.limit, column="limit"),
    total=lambda cli_args: cli_args.limit
)
def action(cli_args, enricher, loading_bar):

    client = AccountInstagramAPIScraper(cookie=cli_args.cookie)

    for _, row, limit in enricher.enumerate_cells(
        "limit", with_rows=True, start=1
    ):
        generator = client.get_explore_feed()

        generator = islice(generator, int(limit))

        for post in generator:
            with loading_bar.step():
                enricher.writerow(row, post.as_csv_row())

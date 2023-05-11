# =============================================================================
# Margtsni Instagram API Scraper
# =============================================================================
#
# Instagram public API "scraper" (only account-specific data).
#
from ebbe import getpath
from minet.instagram.api_scraper import (
    InstagramAPIScraper,
)
from minet.instagram.exceptions import (
    InstagramInvalidTargetError
)
from minet.instagram.formatters import (
    format_post,
)

def forge_explore_feed_url(max_id=None):
    url = "https://www.instagram.com/api/v1/discover/web/explore_grid/"

    if max_id:
        url += "?max_id=%s" % max_id

    return url

class AccountInstagramAPIScraper(InstagramAPIScraper):

    def get_explore_feed(self):
        max_id = None

        while True:
            url = forge_explore_feed_url(max_id=max_id)

            data = self.request_json(url)

            if not data:
                break

            sections = getpath(data, ["sectional_items"])

            if not sections:
                raise InstagramInvalidTargetError

            for section in sections:

                subsection_1 = getpath(section, ["layout_content", "one_by_two_item", "clips", "items"])

                if not subsection_1:
                    raise InstagramInvalidTargetError

                for item in subsection_1:
                    yield format_post(item["media"])

                subsection_2 = getpath(section, ["layout_content", "fill_items"])

                if not subsection_2:
                    raise InstagramInvalidTargetError

                for item in subsection_2:
                    yield format_post(item["media"])

            more_available = data["more_available"]

            if not more_available:
                break

            max_id = data["next_max_id"]

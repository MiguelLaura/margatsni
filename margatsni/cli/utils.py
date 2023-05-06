# =============================================================================
# Margatsni CLI Utils
# =============================================================================
#
# Miscellaneous helpers used by the CLI tools.
#
from typing import Optional, Iterable

import casanova
from casanova.namedrecord import is_tabular_record_class
from functools import wraps
from contextlib import nullcontext
from minet.cli.loading_bar import LoadingBar, StatsItem

def with_enricher_and_loading_bar(
    headers,
    enricher_type=None,
    get_input=None,
    total=None,
    index_column: Optional[str] = None,
    #
    title=None,
    unit: Optional[str] = None,
    sub_unit: Optional[str] = None,
    stats: Optional[Iterable[StatsItem]] = None,
    stats_sort_key=None,
    nested: bool = False,
    show_label: bool = False,
):
    def decorate(action):
        @wraps(action)
        def wrapper(cli_args, *args, **kwargs):
            enricher_context = nullcontext()

            completed = 0

            # Do we need to display a transient resume progress?
            if (
                hasattr(cli_args, "resume")
                and cli_args.resume
                and isinstance(
                    cli_args.output,
                    (casanova.RowCountResumer, casanova.ThreadSafeResumer),
                )
                and cli_args.output.can_resume()
            ):

                resume_loading_bar = LoadingBar(
                    title="Reading output to resume", unit="lines", transient=True
                )
                enricher_context = resume_loading_bar

                def listener(event, _):
                    nonlocal completed

                    if event == "output.row.read":
                        resume_loading_bar.advance()
                        completed += 1

                cli_args.output.set_listener(listener)

            enricher_fn = casanova.enricher

            if enricher_type == "threadsafe":
                enricher_fn = casanova.threadsafe_enricher

            elif enricher_type == "batch":
                enricher_fn = casanova.batch_enricher

            elif enricher_type is not None:
                raise TypeError("wrong enricher type")

            enricher_kwargs = {}

            if index_column is not None:
                enricher_kwargs["index_column"] = index_column

            multiplex = None

            if getattr(cli_args, "explode", None) is not None:
                multiplex = casanova.Multiplexer(cli_args.column, cli_args.explode)

            try:
                select = cli_args.select
            except AttributeError:
                select = []

            with enricher_context:
                enricher = enricher_fn(
                    cli_args.input if not callable(get_input) else get_input(cli_args),
                    cli_args.output,
                    add=headers(cli_args)
                    if callable(headers) and not is_tabular_record_class(headers)
                    else headers,
                    select=select,
                    total=getattr(cli_args, "total", None) if not callable(total) else total(cli_args),
                    multiplex=multiplex,
                    **enricher_kwargs
                )

            with LoadingBar(
                title=title(cli_args) if callable(title) else title,
                total=enricher.total,
                unit=unit(cli_args) if callable(unit) else unit,
                sub_unit=sub_unit(cli_args) if callable(sub_unit) else sub_unit,
                nested=nested,
                stats=stats,
                stats_sort_key=stats_sort_key,
                show_label=show_label,
                completed=completed,
            ) as loading_bar:

                additional_kwargs = {
                    "enricher": enricher,
                    "loading_bar": loading_bar,
                }

                return action(cli_args, *args, **additional_kwargs, **kwargs)

        return wrapper

    return decorate

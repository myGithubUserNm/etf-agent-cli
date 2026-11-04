"""Command-line entry point.

Only the standard library is used. Exit codes follow the project contract:

    0  the run finished and produced everything it promised
    1  the run finished but something it promised is missing or failed
    2  the invocation itself was rejected before any work started

``main`` returns the code instead of calling ``sys.exit`` so tests can call it
directly; the console script and the ``__main__`` guard turn it into a process
exit code.
"""

from __future__ import annotations

import sys
from collections.abc import Sequence

from . import __version__

USAGE = """\
usage: etf-agent [--case CASE] [--output DIR]

Bounded research run over the fixed fixture material.

options:
  --help     show this message and exit
  --version  show the program version and exit
"""

# Slice 1 replaces this message with the real options. Until then the CLI is
# honest about having no run capability rather than pretending to run.
SKELETON_ONLY = "INVALID_ARGUMENT: this build has no run capability yet"


def _force_utf8() -> None:
    """Pin stdout and stderr to UTF-8.

    On Windows a captured (piped) stdout defaults to the ANSI code page, which
    here is cp936. Writing non-ASCII text then degrades to replacement
    characters silently instead of raising, so the JSON we print would be
    corrupted in a way no test notices.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="strict")


def _parse(argv: Sequence[str]) -> tuple[str, list[str]]:
    """Return the selected mode and the remaining arguments."""
    args = list(argv)
    if args in (["--help"], ["-h"]):
        return "help", []
    if args == ["--version"]:
        return "version", []
    return "unknown", args


def main(argv: Sequence[str] | None = None) -> int:
    _force_utf8()
    mode, rest = _parse(sys.argv[1:] if argv is None else argv)
    if mode == "help":
        sys.stdout.write(USAGE)
        return 0
    if mode == "version":
        sys.stdout.write(f"etf-agent-cli {__version__}\n")
        return 0
    detail = f": {' '.join(rest)}" if rest else ""
    sys.stderr.write(f"{SKELETON_ONLY}{detail}\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# encoding: utf-8
from __future__ import annotations

import os
import sys

# setup access to the local .site-packages
sys.path.insert(0, os.path.dirname(__file__) + "/.site-packages")  # noqa


from workflow import Workflow3


def main(wf: Workflow3):
    try:
        wf.add_item("check it out", "cool!")
        wf.send_feedback()
    except Exception as e:
        wf.logger.exception(e)
        raise


if __name__ == "__main__":
    # Create a global `Workflow3` object
    wf = Workflow3()
    wf.logger.info(__name__)
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    wf.run(main)

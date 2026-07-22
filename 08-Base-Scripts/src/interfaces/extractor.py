#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS: Extractor Interface
Defines the abstract contract for codebase parser/extractor utilities.

DATA FLOW:
None (Abstract Base)
"""

from abc import ABC, abstractmethod
from typing import Any

class Extractor(ABC):
    """
    Abstract base class representing a codebase AST or info extractor.
    """

    @abstractmethod
    def extract(self, *args, **kwargs) -> Any:
        """
        Runs the extraction process and returns extracted data.
        """
        pass

#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS: Command Interface
Defines the abstract contract for all executable CLI commands in the base scripts.

DATA FLOW:
None (Abstract Base)
"""

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class representing an executable CLI command.
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> None:
        """
        Executes the command logic with optional arguments.
        """
        pass

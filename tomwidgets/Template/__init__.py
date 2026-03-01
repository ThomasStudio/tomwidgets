"""
Template module for tomwidgets library.
"""

from .Template_back import Template, Templates, GetVariables, LoadModule, TemplateJ2
from .Template import Template
from .TemplateGroup import TemplateGroup, ConfigFolder, ConfigFileName

__all__ = ['Template_back', 'Templates', 'GetVariables',
           'LoadModule', 'TemplateJ2', 'Template_back']

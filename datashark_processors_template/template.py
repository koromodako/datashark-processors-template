"""Datashark Template Plugin
"""
from typing import Dict
from datashark_core.meta import ProcessorMeta
from datashark_core.logging import LOGGING_MANAGER
from datashark_core.processor import ProcessorInterface, ProcessorError
from datashark_core.model.api import Kind, System, ProcessorArgument

NAME = 'template'
LOGGER = LOGGING_MANAGER.get_logger(NAME)


class TemplateProcessor(ProcessorInterface, metaclass=ProcessorMeta):
    """Template of a processor"""

    NAME = NAME
    SYSTEM = System.INDEPENDENT
    ARGUMENTS = [
        {
            'name': 'template_arg',
            'kind': Kind.STR,
            'value': 'default_val',
            'required': False,
            'description': """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
                qui officia deserunt mollit anim id est laborum
            """
        },
    ]
    DESCRIPTION = """
    Template of a processor, not meant for use, meant for dev
    """

    async def _run(self, arguments: Dict[str, ProcessorArgument]):
        """Process a file using tskape"""
        # TODO: perform processor work here
        raise ProcessorError("not implemented!")
        # commit data added by plugin (if needed)
        #self.session.commit()

"""Datashark Template Plugin
"""
from ds_core.api import Artifact, Result, Status
from ds_core.meta import PluginMeta
from ds_core.config import DSConfiguration
from ds_core.plugin import Plugin, generic_plugin_test_app
from ds_core.database import Format
from . import NAME, LOGGER


class TemplatePlugin(Plugin, metaclass=PluginMeta):
    """Process template"""

    NAME = NAME
    DEPENDS_ON = []
    DESCRIPTION = """
    Extract artifacts from template
    """
    YARA_RULE_BODY = """
    strings:
        $sig = "template"
    condition:
        $sig at 0
    """

    def process(self, artifact: Artifact) -> Result:
        """Process a VHD disk image"""
        try:
            # TODO: perform artifact processing here
            # commit data added by plugin
            self.session.commit()
            # finally set overall processing status to SUCCESS
            status = Status.SUCCESS
        except:
            LOGGER.exception(
                "an exception occured while processing artifact: %s", artifact
            )
            status = Status.FAILURE
        return Result(self, status, artifact)


def instanciate(config: DSConfiguration):
    """Instanciate plugin"""
    return TemplatePlugin(config)


def test():
    """Test plugin"""
    generic_plugin_test_app(instanciate, Format.DATA)

from templer.core.base import BaseTemplate

class PloneBuildout(BaseTemplate):
    _template_dir = 'templates/plone_buildout'
    summary = "A basic buildout skeleton for plone 4.3"
    help = """
This creates a basic skeleton for a buildout.
"""
    category = "Buildout"
    required_templates = []
    default_required_structures = ['bootstrap',]
    use_cheetah = True

    

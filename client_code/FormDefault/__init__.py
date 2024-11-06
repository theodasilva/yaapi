from ._anvil_designer import FormDefaultTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class FormDefault(FormDefaultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def reset_links(self, **event_args):
    self.create_property_link.role = ''
    self.update_property_link.role = ''

  def create_property_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('GA4CreateProperty')

  def update_property_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('GA4UpdateProperty')

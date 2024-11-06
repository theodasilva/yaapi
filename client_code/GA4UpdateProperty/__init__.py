from ._anvil_designer import GA4UpdatePropertyTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class GA4UpdateProperty(GA4UpdatePropertyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.layout.reset_links()
    self.layout.update_property_link.role = "selected"

    # Any code you write here will run before the form opens.

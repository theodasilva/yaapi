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
    anvil.google.auth.login(["https://www.googleapis.com/auth/analytics.edit"])
    access_token = anvil.google.auth.get_user_access_token()
    print(access_token)

    # Any code you write here will run before the form opens.

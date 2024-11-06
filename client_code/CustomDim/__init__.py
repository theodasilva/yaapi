from ._anvil_designer import CustomDimTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CustomDim(CustomDimTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.base_property_id = properties["base_property_id"]
    self.refresh_custom_dim_grid()


  def get_custom_dim(self):
    res = anvil.server.call('get_custom_dimension', self.base_property_id.text)
    return res


  def refresh_custom_dim_grid(self):
    data = self.get_custom_dim()
    for item in data:
        self.custom_dim_data_grid.add_component(DataRowPanel(item=item))
    
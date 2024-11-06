from ._anvil_designer import ChannelGroupTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ChannelGroup(ChannelGroupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_channel_group_grid()

  def get_channel_groups(self):
    res = anvil.server.call("get_channel_groups", "463584828")
    return res

  def refresh_channel_group_grid(self):
    data = self.get_channel_groups()
    for item in data:
      self.channel_group_data_grid.add_component(DataRowPanel(item=item))

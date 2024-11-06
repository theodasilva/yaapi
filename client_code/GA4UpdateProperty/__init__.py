from ._anvil_designer import GA4UpdatePropertyTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..CustomDim import CustomDim
from ..ChannelGroup import ChannelGroup
import time


class GA4UpdateProperty(GA4UpdatePropertyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.layout.reset_links()
    self.layout.update_property_link.role = "selected"
    anvil.google.auth.login(["https://www.googleapis.com/auth/analytics.edit"])

    # Any code you write here will run before the form opens.

  def open_custom_dim_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.base_property_id.text:
      alert(title="Select a Base Property.")
      return
      
    alert(
      content=CustomDim(base_property_id=self.base_property_id),
      title="Custom Dimensions",
      large=True,
    )

  def open_custom_group_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.base_property_id.text:
      alert(title="Set a Base Property.")
      return
      
    alert(
      content=ChannelGroup(base_property_id=self.base_property_id),
      title="Channel Groups",
      large=True,
    )

  def update_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.base_property_id.text:
      alert(title="Set a Base Property.")
      return
    if not self.property_ids.text:
      alert(title="Set at least on destination Property.")
      return
      
    if confirm("Are you sure you want to update, this action cannot be canceled?"):
      self.update_properties()


  def update_properties(self):
    base_property_id = self.base_property_id.text
    property_ids = self.property_ids.text.split("\n")
    for property_id in property_ids:
      if self.custom_dim_check.checked:
        anvil.server.call("copy_custom_dim", base_property_id, property_id)
        time.sleep(1)
      if self.custom_group_check.checked:
        anvil.server.call("copy_channel_groups", base_property_id, property_id)
        time.sleep(1)
      time.sleep(2)

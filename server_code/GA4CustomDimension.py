import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.http
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time
import requests



# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#

@anvil.server.callable
def get_custom_dimension(property_id, retry=0):
  data = []
  access_token = anvil.google.auth.get_user_access_token()
  url = f"https://analyticsadmin.googleapis.com/v1beta/properties/{property_id}/customDimensions"

  if (retry == 3):
    return None

  res = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})

  for item in res.json()["customDimensions"]:
    data.append({
      "display_name": item["displayName"],
      "description": item["description"],
      "parameter_name": item["parameterName"],
      "scope": item["scope"],
    })
    
  return data


@anvil.server.callable
def get_channel_groups(property_id, retry=0):
  data = []
  access_token = anvil.google.auth.get_user_access_token()
  url = f"https://analyticsadmin.googleapis.com/v1alpha/properties/{property_id}/channelGroups"

  if (retry == 3):
    return None

  res = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
  for item in res.json()["channelGroups"]:
    if "displayName" not in item:
      print("Except item\n\n")
      continue
      
    print(f"Append item: {item['displayName']}")
    data.append({
      "display_name": item["displayName"],
      "description": item["description"],
      "grouping_rule": item["groupingRule"],
    })
    
  print(f"FINAL data: {data}")
  return data


@anvil.server.callable
def copy_channel_groups(property_id_from, property_id_to, retry=0):
  access_token = anvil.google.auth.get_user_access_token()
  channel_groups = get_channel_groups(property_id_from)
  print(f"Chan g {channel_groups}")
  url = f"https://analyticsadmin.googleapis.com/v1alpha/properties/{property_id_to}/channelGroups"
  
  for channel_group in channel_groups:
    res = requests.post(url, headers={"Authorization": f"Bearer {access_token}"}, json={
      "displayName": channel_group["display_name"],
      "description": channel_group["description"],
      "groupingRule": channel_group["grouping_rule"],
    })
    print("Channel group: ", res)
    time.sleep(2)
    
  return channel_groups


@anvil.server.callable
def copy_custom_dim(property_id_from, property_id_to, retry=0):
  access_token = anvil.google.auth.get_user_access_token()
  custom_dimensions = get_custom_dimension(property_id_from)
  url = f"https://analyticsadmin.googleapis.com/v1beta/properties/{property_id_to}/customDimensions"

  for custom_dimension in custom_dimensions:
    res = requests.post(url, headers={"Authorization": f"Bearer {access_token}"}, json=custom_dimension)
    print("Custom Dim: ", res)
    time.sleep(2)
    
  return True


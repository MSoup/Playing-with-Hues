import json
import requests
import time

# Caution: store your base_url in a PRIVATE location for security. 

class Hue:
  def __init__(self):
    self.setting = ["dim", "bright"]
    # Change location of philips hues endpoint uri here
    with open('C:\\Users\\charm\\OneDrive\\Desktop\\Christmas Turkey') as f:
      self.base_url = f.read().strip()

  def getInstructions(self):
    print("Welcome to MSoup's Philips Hues App")
    print("-----------------------------------")
    print("Commands:")
    print("Left / Right arrow: switch between light settings")
    print("Q / quit / exit: Exit script")
    print("Help: get instructions again")
    print("-----------------------------------")
    print("By default, your lights will turn on. ")

  def turnOn(self):
    response = requests.put(self.base_url + 'lights/1/state', json.dumps({'on': True}))
    print(response.content)
  
  def turnOff(self):
    response = requests.put(self.base_url + 'lights/1/state', json.dumps({'on': False}))
    print(response.content)

  def run(self):
    self.getInstructions()
    self.turnOn()

if __name__ == "__main__":
    hue = Hue()
    hue.run()

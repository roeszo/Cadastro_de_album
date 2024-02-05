responses = {}

polling_active = True

while polling_active:
  name = input("\nWhats your name? ")
  response = input("\nWhats your favorite mountain? ")
  responses[name] = response
  repeat  = input("Would u like to respond again? (yes or no)")
  if repeat == 'no':
    polling_active = False

print("\n-----Pool results-----")
for name, response in responses.items():
  print(name.title() + " like's the mountain  " + response.title() + ".")

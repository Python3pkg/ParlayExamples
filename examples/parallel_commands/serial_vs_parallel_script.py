from parlay.utils import setup, discover, get_item_by_name

setup()
discover()

item1 = get_item_by_name("Item1")
item2 = get_item_by_name("Item2")


print("\nSending blocking commands")

print("  Slow Command 1...")
response1 = item1.slow_command_1()
print(response1)
print("  Slow Command 2...")
response2 = item2.slow_command_2()
print(response2)

print("\nSending parallel commands")

print("  Slow Command 1...")
cmd1 = item1.send_parlay_command("slow_command_1")
print("  Slow Command 2...")
cmd2 = item2.send_parlay_command("slow_command_2")

print("  Waiting for responses...")
response1 = cmd1.wait_for_complete()["CONTENTS"]["RESULT"]
response2 = cmd2.wait_for_complete()["CONTENTS"]["RESULT"]

print(response1)
print(response2)


from parlay.utils import setup, discover, get_item_by_name

setup()
discover()
e = get_item_by_name("Adder")
e.x = 10
e.y = 12
handle = e.send_parlay_command("add", x=1, y=2)
handle.wait_for_ack()
print("ack1")
handle.wait_for_ack()
print("ack2")

st = e.get_datastream_handle("st")
print(st.get())
e.send_parlay_command("poll_stream")

while st.get() < 100:
    print(st.wait_for_value())
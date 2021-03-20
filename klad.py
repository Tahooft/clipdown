import youtube_dl

print(youtube_dl.YoutubeDL.values)


# import time

# def executeSomething():
#     #code here
#     print('hallo')
#     time.sleep(10)

# while True:
#     executeSomething()


# ###
# from threading import Event, Thread

# def call_repeatedly(interval, func, *args):
#     stopped = Event()
#     def loop():
#         while not stopped.wait(interval): # 1st call is in `interval` secs
#             func(*args)
#     Thread(target=loop).start()
#     return stopped.set

# cancel_future_calls = call_repeatedly(10, print, "Hello, World")

# ###
# import asyncio
# import datetime


# def display_date(end_time, loop):
#     print(datetime.datetime.now())
#     if (loop.time() + 1.0) < end_time:
#         loop.call_later(1, display_date, end_time, loop)
#     else:
#         loop.stop()


# loop = asyncio.get_event_loop()

# # Schedule the first call to display_date()
# end_time = loop.time() + 5.0
# loop.call_soon(display_date, end_time, loop)

# # Blocking call interrupted by loop.stop()
# try:
#     loop.run_forever()
# finally:
#     loop.close()

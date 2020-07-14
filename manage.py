#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MTAHackathon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# # !/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys
# from sshtunnel import SSHTunnelForwarder
# from time import sleep

# # 52.149.162.104
# # 10.0.0.37
# def main():
#     with SSHTunnelForwarder(
#     ('52.147.195.220'), 
#     ssh_username="hackserveradmin",
#     ssh_password="Welc0me@123456789",
#     local_bind_address=('127.0.0.1', 5432),
#     remote_bind_address=('127.0.0.1', 5432)) as server:
#         print(server.local_bind_port)
#         # press Ctrl-C for stopping
#         os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MTAHackathon.settings')
#         try:
#             from django.core.management import execute_from_command_line
#         except ImportError as exc:
#             raise ImportError(
#                 "Couldn't import Django. Are you sure it's installed and "
#                 "available on your PYTHONPATH environment variable? Did you "
#                 "forget to activate a virtual environment?"
#             ) from exc
#         execute_from_command_line(sys.argv)
#         # sleep(1)
#     print('Connection Terminated')

# if __name__ == '__main__':
#     main()

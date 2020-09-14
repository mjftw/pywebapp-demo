FROM python:3.7

COPY src /root/src
COPY setup.py /root

RUN python3 -m pip install /root
FROM python:3.7

COPY src /root/src
COPY setup.py /root

RUN python3 -m pip install /root
RUN python3 -m pip install uvicorn

CMD ["python3", "-m", "uvicorn", "brewinv.__main__:app", "--host", "0.0.0.0", "--port", "8080"]

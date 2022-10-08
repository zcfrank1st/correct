FROM shibing624/pycorrector:0.0.2

RUN ["pip3", "install", "--upgrade", "pip", "-i",  "https://pypi.tuna.tsinghua.edu.cn/simple"]
RUN ["pip3", "install", "fastapi[all]", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"]

WORKDIR  /opt

COPY ./server.py /opt
CMD ["uvicorn", "server:app", "--workers", "3"]

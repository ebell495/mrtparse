FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /mrtparse
WORKDIR /mrtparse
RUN python3 -m pip install . && chmod +x fuzz/mrt_fuzz.py

ENTRYPOINT [ ]
CMD ["/mrtparse/fuzz/mrt_fuzz.py"]
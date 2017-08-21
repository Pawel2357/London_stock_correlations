FROM python
RUN pip3 install jupyter \
    numpy \
    matplotlib \
    python-igraph \
    pandas

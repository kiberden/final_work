FROM python:3.10-slim-buster

ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get -qq update && apt install --no-install-recommends -y curl vim python-psycopg2
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && \
    poetry self update

ARG GID=1000
ARG UID=1000

RUN mkdir /var/app

RUN groupadd -g $GID www
RUN useradd -l -u $UID -ms /bin/bash -g www www  && chown -R www:www /var/app

WORKDIR /var/app/

COPY --chown=www:www ../poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY --chown=www:www .. .

RUN mkdir media static

CMD ["/bin/bash", ".docker/start.sh"]

USER www

FROM ghcr.io/astral-sh/uv:python3.13-alpine

# timezone:
ENV TZ=Europe/London
# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

######### MAIN FILES ##########
WORKDIR /main
COPY .env .env
COPY app app
COPY configs/gunicorn.conf.py gunicorn.conf.py
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
###############################

# Install the project's dependencies using the lockfile and settings
RUN uv sync --no-dev
# Place executables in the environment at the front of the path
ENV PATH="/main/.venv/bin:$PATH"

ENTRYPOINT ["gunicorn"]

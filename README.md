# tap-learndash

`tap-learndash` is a Singer tap for [LearnDash](https://www.learndash.com/), a learning management system for Wordpress.
It uses the [REST API](https://developers.learndash.com/) to extract information about courses and user progress.

Built with the Meltano [SDK](https://gitlab.com/meltano/sdk) for Singer Taps.

## Installation

To install this tap, use the latest version on PyPi:

```bash
pipx install tap-learndash
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-learndash --about
```

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `tap-learndash` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-learndash --version
tap-learndash --help
tap-learndash --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_learndash/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-learndash` CLI interface directly using `poetry run`:

```bash
poetry run tap-learndash --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

The project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml`, configure the credntials and install the desired loader.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-learndash
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-learndash --version
# OR run a test `elt` pipeline:
meltano elt tap-learndash target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

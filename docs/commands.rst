Commands
========

The Makefile contains central entry points for common tasks related to this project.

**Syncing data to S3**

- `make sync_data_to_s3`: Uses `aws s3 sync` to recursively sync files in `data/` up to `s3://your-bucket-for-syncing-data/data/`.
- `make sync_data_from_s3`: Uses `aws s3 sync` to recursively sync files from `s3://your-bucket-for-syncing-data/data/` to `data/`.

**Local Development**

- `make install`: Installs the project package in editable mode with its dependencies.
- `make test`: Runs the test suite.

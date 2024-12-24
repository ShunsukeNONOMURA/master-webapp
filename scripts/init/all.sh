#!/bin/bash

set -e

echo "Running all init tasks..."

./scripts/init/00_migrate.sh

echo "All init tasks completed successfully!"

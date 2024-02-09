# Installation Guide

## Installation

1. Install the Purchase Validation app using pip:

    ```bash
    ./your_venv/bin/pip install -q -U -e ./apps/purchase_validation
    ```

2. Alternatively, you can use Bench to install the app:

    ```bash
    bench --site <site_name> install-app purchase_validation
    ```

## Migration and Build

After installation, run the following commands to migrate and build:

```bash
bench migrate
bench build

In this Markdown, `[Video Tutorial]` will appear as the clickable text. When someone clicks on it, it will open the provided URL (`https://drive.google.com/file/d/1CzkLW9_iJJhIj89urjVjnRkQBlf22mgd/view?usp=sharing`). Make sure to replace `<your_venv>` and `<site_name>` with actual values

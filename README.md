# Instructions

1. Create virtual environment.

    ```shell
    python3 -m venv .venv 
    ```

2. Activate virtual environment.

    ```shell
    source ./.venv/bin/activate
    ```

3. Install dependencies.

    ```shell
    pip install -r requirements.txt 
    ```
    
4. To convert notebooks to HTML. 

    ```
    jupyter nbconvert classpert_hw_1.ipynb --to html
    ```

4. To purge and cleanup, delete the virtual environment.

    ```shell
    rm -rf .venv 
    ```


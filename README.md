<p align="center">
	<img src="./assets/ecothaili_api.png" alt="homescreen" width="650" height="auto">
</p>

<p align="center">
🚀 Empowering seamless e-commerce experiences with Django's robust backend infrastructure.
</p>

## Comprehensive Guide to Setup the Project in Our Local Machine

### Prerequisites

> [!NOTE]
> Please use LTS version of following tools.

- [Docker](https://docs.docker.com/engine/)
- [Docker Compose](https://docs.docker.com/compose/)

> [!NOTE]
> Only after creating virtual environment, step foward to next step. If you have any issue building our project plz send your query/problem in [discussion](https://github.com/Team-Inventrix/ecothaili-api/discussions/categories/q-a)

### It's time to play 🎲

0. **Clone the Repository**: 
   - Open your terminal or command prompt. (If you are comming from step 0 you don't need to reopen terminal)

   - Navigate to the directory where you want to clone the repository.

   - Run the following command:
     ```bash
     git clone https://github.com/Team-Inventrix/ecothaili-api.git
     ```
   Here `https://github.com/Team-Inventrix/ecothaili-api.git` is the URL of the GitHub repository from where we will be cloning the project to our local machine.

1. **Virtual Env. setup**:
    - For [Linux users](https://virtualenv.pypa.io/en/latest/user_guide.html), go through this guide to setup virtual env. in your local machine.
    - For [windows user](https://docs.python.org/3/library/venv.html), go through this guide to setup virtual env. in your local machine.

2. **Install Project Dependencies**:
   - After the cloning is completed! you will get a folder and you have to navigate into that project directory:
     ```bash
     cd ecothaili-api
     ```
   - Run the following command to install project dependencies specified in `requirements.txt`:
     ```bash
     pip install --no-cache-dir -r requirements.txt
     ```

3. **Time to use Docker🐋**
    - Simply, run the following either of the mentioned command as per your need.
        ```bash
        docker compose up --build
        ```
        > This commans starts containers after rebuilding all images specified.

        or,

        ```bash
        docker compose up
        ```
        > This command starts containers with existing images, rebuilding only if necessary.


   	> if your wanna stop the container, use `Ctrl + C`

4. **For stopping and clearing the containers**
   - Use the following commands.
     ```bash
     docker compose down
     ```
     > stop and delete the containers

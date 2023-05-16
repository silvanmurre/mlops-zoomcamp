# MLOps Zoomcamp - My setup

I might not follow the toolset of the course exactly and sometimes use tools that I find friendlier to work with. I will document my setup and findings here.

## Workflow

Fork https://github.com/DataTalksClub/mlops-zoomcamp and clone it locally:

```shell
git clone <forked_repository>
```

Add https://github.com/DataTalksClub/mlops-zoomcamp as a new remote called *upstream*:

```shell
git remote add upstream https://github.com/DataTalksClub/mlops-zoomcamp
```

Use `git fetch upstream` to check for updates from the original repository. Use `git pull upstream main` to merge the changes from the original repository's main branch into your fork's main branch. Be sure to commit any changes to your fork's main branch before running this command. Be ready to resolve any merge conflicts that may arise.

Verify that the upstream remote has been added successfully by running `git remote -v`. You should now see the original repository's remote URL under the name `upstream`.

## Tools

- The course is taught in Linux and mainly uses the command line to install docker and other tools. As long as Windows permits, I will use it. If I run into issues, I will switch to WSL2.
- IDE: VSCode has a neat Jupyter Notebook integration, Pycharm only provides this in the professional version.
  - GitLens extension for VSCode to keep the workflow clean. Also, I prefer using a visual interface rather than the command line sometimes.
- Python 3.11.2

## Virtual Environments

I recommend to create a separate virtual environment for each module and create requirements.txt for each module. This way, you can install all the required packages for the module without worrying about conflicts with other modules.

Move into a module folder:

```shell
cd cohorts/2023/01-intro
```

Create a virtual environment:

```shell
python -m venv .venv --upgrade-deps
```

Activate:

```shell
source .venv/Scripts/activate
```

Add the virtual environment as a Jupyter kernel:

```shell
pip install ipykernel
python -m ipykernel install --user --name=01-intro-homework
```

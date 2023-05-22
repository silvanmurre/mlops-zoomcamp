# Setup and Workflow

I might not follow the toolset of the course exactly and sometimes use or want to experiment with tools that I might find friendlier to work with. I will document my setup and workflow here, occasinally diving deeper into subjects I find interesting. I might tweak some things in my setup over the duration of this course, so expect this document to change.

## Tools

- The course is taught in Linux and mainly uses the command line to install Docker and other tools. I am following it on a Windows 11 machine and used WSL 2 with Ubuntu 22.04.2 LTS to install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/).
- The course also shows how to setup and run your code and other services on a remote EC2 instance by setting up a `t2.xlarge` instance. I think a reasonably modern laptop suffices to run the code and services locally, we'll see as the course progresses.
- IDE: VSCode, version 1.78.2
  - Has a neat Jupyter Notebook integration, Pycharm only provides this in the professional version.
  - GitLens extension to keep the workflow clean. Also, I prefer using a visual interface rather than the command line sometimes.
- Python 3.11.2

## Repository setup

Fork [https://github.com/DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) and clone it locally:

```shell
git clone <forked_repository>
```

Add [https://github.com/DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) as a new remote called *upstream*:

```shell
git remote add upstream https://github.com/DataTalksClub/mlops-zoomcamp
```

Use `git fetch upstream` to check for updates from the original repository. Use `git pull upstream main` to merge the changes from the original repository's main branch into your fork's main branch. Be sure to commit any changes to your fork's main branch before running this command. Be ready to resolve any merge conflicts that may arise.

Verify that the upstream remote has been added successfully by running `git remote -v`. You should now see the original repository's remote URL under the name `upstream`.

## Virtual Environments

I recommend to create a separate `virtual environment` and `requirements.txt` for each module. This way, you can install all the required packages for the module without worrying about conflicts with dependencies in other modules. [`Jupyter Notebooks`](https://jupyter.org/) will be used in this course, you will need to (at least) add `ipykernel` to your `requirements.txt` to be able to run Python code in Jupyter Notebooks.

Unfortunately for the GUI mains or terminal dislikers using VSCode, to my knowledge, there is no graphical option to create a virtual environment outside the root folder. So the first command line steps I do before diving into a module are:

```shell
cd <module_folder>
```

Or right click the module folder in VSCode and select `Open in Integrated Terminal`, then:

```shell
python -m venv .venv --upgrade-deps
source .venv/Scripts/activate
pip install -r requirements.txt
```

I add `--upgrade-deps` when creating the virtual environment to ensure that the latest version of `pip` and `setuptools` is installed, otherwise it will use the versions that came with your Python installation. This is not necessary, but I like to keep my tools up to date and it can help avoid issues caused by bugs in older versions.

## Jupyter Notebooks and Kernels

This course and many alike often uses Jupyter Notebooks to teach the subject matter. The interactive nature of writing, executing, documenting and visualizing code make them a great tool for education. The [Jupyter Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) provides notebooks in the VSCode environment, such that you don't have to switch back and forth, plus all VSCode features are available.

Kernels are needed to execute code contained in notebooks. Each kernel that is created saves it details as a `Kernel Specification (kernel spec)` in the [`kernels`](https://jupyter-client.readthedocs.io/en/stable/kernels.html#kernel-specs) folder in the respective Jupyter configuration directory. At a minimum, you need to have `ipykernel` installed, which automatically installs a (*default*) kernel spec for the current Python environment (`python3`: `.venv/share/jupyter/kernels/python3/kernel.json`).

In VSCode, there are multiple ways you can set up and select your kernel:

- `Python Environments` - [lists the Python environments that VS Code detects from the compute system it's operating in](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management#_python-environments). Uses the default `python3` kernel spec. **Note that it cannot automatically detect virtual environments that are not in the root folder of the project. It will be able to detect it if you set up the Python Interpreter first**:  
  
  `Help` > `Show all commands (Ctrl+Shift+P)` > `Python: Select Interpreter`.
  
  Click `Enter interpreter path...`, either paste the path to your Python Executable or use `Find...` to locate it (executable can be found under `.venv/Scripts/python.exe` in Windows or `.venv/bin/python.exe` in Unix).

  The added benefit of selecting the Python Interpreter is that you now also are able to run regular Python scripts in VSCode using the same virtual environment.

- `Jupyter Kernel` - Supports multiple languages and useful if you want to set up custom kernel specifications. In your virtual environment, you can make the kernel detectable using `ipykernel`. There are multiple places you can install the kernel spec into:

  - Locally, in your virtual environment: `python -m ipykernel install --sys-prefix`
  - User profile: `python -m ipykernel install --user`
  - System-wide: `python -m ipykernel install`
  
- `Existing Jupyter Server` - connect to an existing Jupyter server running remotely or locally. You need to set up the server manually.

I prefer to use the `Python Environments` option, as you will have a Kernel Specification that is specific to your virtual environment, always under `.venv/share/jupyter/python3`. Thus, you don't have to worry about knowing `ipykernel` CLI commands to install the kernel spec into the correct folder and selecting the correct kernel spec when you open a notebook in VSCode.

Sources used to learn about kernels:

- [Kernels (Architecture)](https://github.com/microsoft/vscode-jupyter/wiki/Kernels-(Architecture))
- [IPython kernel docs](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)

# Codes for the lecture "Compuational Methods in Many-Body Physics"

This repository will be updated to contain the example codes for the exercises.

Course website: <https://www.groups.ph.tum.de/cmt/teaching/computational-methods/>

Moodle: <https://www.moodle.tum.de/course/view.php?id=85197>

Git repository: <https://gitlab.lrz.de/cmt-computational-physics/tutorials_2023>

Scipy lectures: <http://www.scipy-lectures.org/>

## Setup for laptops and PC

You can choose one option below:
1. Download ancaonda from <https://www.anaconda.com/download>
2. Download miniconda from <https://docs.conda.io/en/latest/miniconda.html> and install necessary packages with
```
conda install numpy scipy matplotlib numba
```
3. Google colab <https://colab.research.google.com/> from web brower without
   any installation

## Starting a python notebook
1. Open a terminal
2. Go to the directy where you keep your scripts/notebooks using `cd some/directory`
3. Enter `jupyter notebook`
   This should start a local server, where you can create python notbooks etc.
   If you close the web page, open the page http://localhost:8888/ 
4. Do your calculations :-)

   Ipython magic for including the plots into the notebooks:
   ``` 
   %matplotlib inline
   ```
5. Once you're done, stop the server in the terminal by pressing Ctrl-C and confirm with 'y'

## Git 

- open a terminal
- Get a local copy of the remote repoistory with `git clone https://gitlab.lrz.de/cmt-computational-physics/tutorials_2023.git`
  Alternatively, initialize a new repository in an exisiting folder with `git init`.
- write code and modify local files
- `git status` shows which files have been changed.
- `git diff changed_script.py` shows what you have changed in the given file.
- `git add changed_script.py` marks the file `changed_script.py` to be added to the next git snapshot
- `git commit -m "helpful message to describe changes"` to create a new "snapshot"
- `git log` to show a list of all snapshots. 

  The first line of each "snapshot" contains a hash value (like `0d4e77a6ef3224a51f6a39c8e41a9cbd5778ca92`)
  which can be used as reference for the snapshot (the first 8 characters of the hash are usually enough).
  For example to view changes of this README.md file since the first commit inside this repository,
  use `git diff 0d4e77a6 README.md`.
- `git pull` to fetch changes from the remote repository (if you initialized it with `git clone`) and merge them into
  your version of the code.
  `git push` is the opposite, it uploads to a remote repository.

For a 10-minute introduction, see for example <https://guides.github.com/introduction/git-handbook/>.

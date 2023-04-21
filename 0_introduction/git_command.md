## Git global setup
```
git config --global user.name [my_username]
git config --global user.email [my_email]
```

------

## Create a new repository
```
git clone git@gitlab.lrz.de:[my_username/[project_name].git
cd [directory]
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```
------

## Push an existing folder
```
cd existing_folder
git init
git remote add origin git@gitlab.lrz.de:[my_username/[project_name].git
git add .
git commit -m "Initial commit"
git push -u origin master
```
------

## Push an existing Git repository

```
cd existing_repo
git remote rename origin old-origin
git remote add origin git@gitlab.lrz.de:[my_username/[project_name].git
git push -u origin --all
git push -u origin --tags
```

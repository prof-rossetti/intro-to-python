
# "Hello World" Version Control Exercise Solutions

Here are some of the commands you might use during the course of the version control exercise:

```sh
# create a GitHub repo and obtain its remote address, ideally the SSH version, then...

cd ~/Desktop
git clone REMOTE_ADDRESS # where REMOTE_ADDRESS is the remote address of your GitHub repo
cd my-first-repo/

code . # opens the project in the text editor

touch my_script.py # (or create the file via the text editor)

# edit and save the files, then...

git add .
git commit -m "My first commit"
git push origin main

# edit and save the files, then...

git add .
git commit -m "My second commit"
git push origin main

# edit and save the files, then...

git add .
git commit -m "My third commit"
git push origin main
```

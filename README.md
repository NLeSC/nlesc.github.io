# THIS REPO IS OBSOLETE
Please add your info to the RSD at https://research-software-directory.org/
For more information, ask your programme manager at the teams channel, in person, or send them an email at programme@esciencecenter.nl

Original Readme follows below


# NLeSC Github projects website

Overview of Github organizations of all NLeSC projects.

## Adding an Github organization

### Automatically

Run following script to generate a Markdown file in `_organizations/` directory.
```
# (requires Python 3)
# run from the project root
pip install -r requirements.txt
python generate.py <github organization name>
```
The `<github organization name>` should already exist on GitHub.

### Manually

1. Create new Markdown file (.md) in `_organizations/` directory.
2. Fill following FrontMatter properties

    * title: Human readable name of project
    * homepage: Url of project software website or Github organization website
    * avatar: Url of profile image

3. Fill main body with short description of project.

## Preview website

The website uses Jekyll powered Github pages.

To preview locally use docker:
```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t -p 127.0.0.1:4000:4000 jekyll/jekyll:pages jekyll serve
```
The website can be viewed on http://localhost:4000

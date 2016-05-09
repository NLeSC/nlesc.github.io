# NLeSC GitHub projects website

Overview of GitHub organizations of all NLeSC projects.

## Adding an GitHub organization

1. Run following script to generate a Markdown file in `_organization/` directory.
```
pip install -r requirements.txt
python generate.py <github organization name>
```

2. Fill following FrontMatter properties

    * name: Human readable name of project
    * website: Human-friendly url of project software website (preferably
      http://organization.github.io)
    * logo: Url of profile image
    * usedIn: http://software.esciencecenter.nl project URLs where the
      GitHub organization is used in. If the project is not registered
      there, give an object with name and nlescWebsite properties.

    The name, website and logo properties are mandatory.

3. Optionally fill main body with a description of the purpose of the GitHub organization.

## Preview website

The website uses Jekyll powered GitHub pages.

To preview locally use docker:
```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t -p 127.0.0.1:8080:80 jekyll/jekyll:pages
```
The website can be viewed on http://localhost:8080

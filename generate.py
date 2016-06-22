#!/usr/bin/env python

# Copyright 2016 Netherlands eScience Center
#
# Licensed under the Apache License, Version 2.0 (the 'License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import github3
import requests


def generate_organization(organization):
    gh = github3.GitHub()
    org = gh.organization(organization)
    fn = '_organization/{0}.md'.format(org.login.lower())

    website = 'http://{0}.github.io/'.format(org.login.lower())
    req = requests.get(website)
    if req.status_code >= 400:
       website = org.html_url

    title = org.name
    if not title:
        title = org.login
    description = org._json_data.get('description', '')
    template = """---
name: {name}
website: {website}
logo: {avatar}
involvedProject:
- name: {name}
  website: http://publicwebsite.nl/
  nlescWebsite: https://www.esciencecenter.nl/project/myprojectname
  estepId: http://software.esciencecenter.nl/project/myprojectname
---
{description}
    """
    with open(fn, 'w') as f:
        f.write(template.format(name=title,
                                website=website,
                                avatar=org.avatar_url,
                                description=description))


def main():
    parser = argparse.ArgumentParser(description='Generate Jekyll files')
    parser.add_argument('organization', nargs='+', help='GitHub organization '
                                                        'or user name')
    args = parser.parse_args()
    for organization in args.organization:
        generate_organization(organization)

if __name__ == "__main__":
    main()

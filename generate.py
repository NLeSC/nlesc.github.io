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
from github3.null import NullObject


def generate_organization(organization):
    gh = github3.GitHub()
    org = gh.organization(organization)
    if isinstance(org, NullObject):
        raise KeyError('GitHub organization "{0}" could not be found'.format(organization))
    fn = '_organizations/' + org.login.lower() + '.md'
    title = org.name
    if not title:
        title = org.login
    body = org._json_data.get('description', '')
    if not body:
        body = ''
    template = """---
title: {title}
homepage: {homepage}
avatar: {avatar}
---
{body}
    """
    with open(fn, 'w') as f:
        f.write(template.format(title=title,
                                homepage=org.html_url,
                                avatar=org.avatar_url,
                                body=body))


def main():
    parser = argparse.ArgumentParser(description='Generate Jekyll files')
    parser.add_argument('organization', nargs='+', help='Github organization or user name')
    args = parser.parse_args()
    for organization in args.organization:
        generate_organization(organization)

if __name__ == "__main__":
    main()

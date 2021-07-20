#!/bin/bash

# source github parameters environment variables:
# GH_REPOS_URL  = https://api.github.com/user/repos
# GH_USER       = <username>
# GH_REPO_TOKEN = <github token>
. $(dirname ${BASH_SOURCE[0]})/.api.github.source

# call githubapi
#   with authentication: -u user:token
#   100 items per page
#   private repos
# extract clone_url elements
#
# ref: https://programminghistorian.org/en/lessons/json-and-jq#core-jq-filters
#    .  gets everything: 
#            [{},{},{},...]
#
#    .[] get all objects out of the array: 
#            {},{},{},...
#    for instance .[0] extracts the first object {}
#
#	..[].clone_url extracts the value of each "clone_url" key
#    same as .[]| .clone_url 
curl -s -u ${GH_USER}:${GH_REPO_TOKEN} -s "${GH_PRIVATE_REPOS_URL}?per_page=100&visibility=private" | jq -r ".[].clone_url"

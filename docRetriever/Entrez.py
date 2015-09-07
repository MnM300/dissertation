import re
from Utilities import get_url_response

baseURL = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils"


# create url to fetch the abstracts from the ids retrieved
def efetch_url(uid_list):
    return "/efetch.fcgi?db=pmc&id=" + uid_list + "&rettype=MEDLINE&retmode=text"


# get the abstracts fro the list of uids
def get_abstracts(search_criteria):
    fetch_url = efetch_url(get_pmc_ids_as_string(search_criteria))
    return get_url_response(baseURL, fetch_url)


# create url to fetch the IDS from the descriptions given
def e_search_url(search_criteria):
    search_criteria = search_criteria.strip()
    search_criteria = search_criteria.replace(" ", "+")
    return '/esearch.fcgi?db=pmc&term=%22' + search_criteria + '%22+AND+open+access[filter]&retmax=14'


# get the ids of papers based on search criteria
def get_pmc_ids(search_criteria):
    search_url = e_search_url(search_criteria)
    response = get_url_response(baseURL, search_url)
    return parse_uids(response)


# get the ids of papers based on search criteria as list
def get_pmc_ids_as_string(search_criteria):
    search_url = e_search_url(search_criteria)
    uids = parse_uids(get_url_response(baseURL, search_url))
    uid_list = ""
    for UID in uids:
        uid_list += unicode(UID) + ","

    uid_list = uid_list.rstrip(",")
    return uid_list


# Parse retrieved UIDS from xml format
def parse_uids(url_response):
    uids = re.findall('<Id>(.*?)</Id>', url_response, re.DOTALL)
    return map(int, uids)

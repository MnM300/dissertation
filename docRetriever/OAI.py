from Utilities import get_url_response
from Entrez import get_pmc_ids

base_url = "http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi"


# create url to fetch the papers from the ids retrieved
def fulltext_fetch_url(uid):
    return "?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:" + unicode(uid) + "&metadataPrefix=pmc"


# get the full text based on ids given
def get_fulltext_by_uids(uid_list):
    full_texts = []
    for UID in uid_list:
        fetch_url = fulltext_fetch_url(UID)
        full_texts.append(get_url_response(base_url, fetch_url))

    return full_texts


# get full texts based on search criteria
def get_fulltext(search_criteria):
    uid_list = get_pmc_ids(search_criteria)
    return get_fulltext_by_uids(uid_list)

"""
http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:4084583&metadataPrefix=pmc
http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:4079914&metadataPrefix=pmc
http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:4164026&metadataPrefix=pmc


http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=24141372&rettype=MEDLINE&retmode=text


http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:24141372&metadataPrefix=pmc
http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:21684626&metadataPrefix=pmc
http://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:23788751&metadataPrefix=pmc
"""

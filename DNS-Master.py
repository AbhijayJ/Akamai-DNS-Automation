import requests
from urllib.parse import urljoin
from akamai.edgegrid import EdgeGridAuth
import json

baseurl = "https://xxxxxxxxxxxxxxxxx.luna.akamaiapis.net"
s = requests.Session()
s.auth = EdgeGridAuth(
    client_token='xxxxxxxxxxxxxxxxx',
    client_secret='xxxxxxxxxxxxxxxxx',
    access_token='xxxxxxxxxxxxxxxxx'
)

def get_all_dns_records(domain_name):

    result = s.get(urljoin(baseurl, '/config-dns/v2/zones/{}/recordsets?sortBy=name&types=A%2CCNAME&showAll=true'.format(domain_name))) #Gets CNAME & A Records
    result_json = json.loads(result.text)

    if not result.ok:
        raise Exception(result_json)

    return result_json





def get_dns_record(domain_name, record_name, record_type):


    endpoint = "/config-dns/v2/zones/{}/names/{}/types/{}".format(domain_name, record_name, record_type)
    result = s.get(urljoin(baseurl, endpoint))
    result_json = json.loads(result.text)

    if not result.ok:
        raise Exception(result_json)

    return result_json




def create_dns_record(domain_name, record_name, record_type, ttl_value, rdata):

    endpoint = "/config-dns/v2/zones/{}/names/{}/types/{}".format(domain_name, record_name, record_type)
    payload = json.dumps({
    "name": record_name,
    "type": record_type,
    "ttl": ttl_value,
    "rdata": rdata
    })

    result = s.post(urljoin(baseurl, endpoint), headers={'Content-Type': 'application/json'}, data=payload)
    result_json = json.loads(result.text)

    if not result.ok:
        raise Exception(result_json)

    return result_json




def modify_dns_record(domain_name, record_name, record_type, ttl_value, rdata):

    endpoint = "/config-dns/v2/zones/{}/names/{}/types/{}".format(domain_name, record_name, record_type)
    payload = json.dumps({
    "name": record_name,
    "type": record_type,
    "ttl": ttl_value,
    "rdata": rdata
    })

    result = s.put(urljoin(baseurl, endpoint), headers={'Content-Type': 'application/json'}, data=payload)
    result_json = json.loads(result.text)

    if not result.ok:
        raise Exception(result_json)
        
    return result_json



def delete_dns_record(domain_name, record_name, record_type):

    endpoint = "/config-dns/v2/zones/{}/names/{}/types/{}".format(domain_name, record_name, record_type)

    result = s.delete(urljoin(baseurl, endpoint))

    if not result.ok:
        result_json = json.loads(result.text)
        raise Exception(result_json)

    return result.status_code


if __name__ == "__main__":

    domain_name = "labcorp.google.com"
    record_name = "example55.labcorp.google.com"
    record_type = "A"
    ttl_value = 300
    rdata = ["10.0.0.29", "10.0.0.39"]

    result1 = create_dns_record(domain_name, record_name, record_type, ttl_value, rdata)
    print("Create DNS - ", result1)
    print("------------------------------------------------------")
    print()

    result2 = get_all_dns_records(domain_name)
    print("get DNS records", result2)
    print("------------------------------------------------------")
    print()

    result5 = get_dns_record(domain_name, record_name, record_type)
    print("Get DNS - ", result5)
    print("------------------------------------------------------")
    print()

    rdata = ["10.0.1.29", "10.0.1.39"]
    result3 = modify_dns_record(domain_name, record_name, record_type, ttl_value, rdata)
    print("Modify DNS - ", result3)
    print("------------------------------------------------------")
    print()

    result4 = delete_dns_record(domain_name, record_name, record_type)
    print("Delete DNS - ", result4)

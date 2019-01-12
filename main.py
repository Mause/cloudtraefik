from CloudFlare import CloudFlare
import ipdb

with open('cloudflare_key.txt') as fh:
    cloudflare = CloudFlare(email='me@mause.me', token=fh.read().strip())

zone = cloudflare.zones.get(params={'name': 'mause.me'})[0]['id']

prefix = 'novell.mause.me'
IP = '192.168.1.8'


def main():
    dns_records = cloudflare.zones.dns_records

    records = dns_records.get(zone)

    for record in records:
        print(record['name'])

    ipdb.set_trace()
    dns_records.post(
        zone,
        data={
            'name': 'transmission.novell',
            'type': 'A',
            "content":IP,
            "ttl":120,
            'proxied': False
        }
    )


if __name__ == '__main__':
    main()


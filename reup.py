import socket
from main import zone, dns_records, PREFIX, confirm


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def main():
    new = get_ip()

    for record in dns_records.get(zone):
        if record["name"].endswith('.' + PREFIX):
            current = record["content"]

            if current != new:
                print(f'updating {current} to {new} for {record["name"]}')

                if confirm('ok?'):
                    dns_records.patch(zone, record["id"], data={'content': new})


if __name__ == "__main__":
    main()

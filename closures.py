import random
from time import sleep

import influxdb
from pprint import pprint


# Factory Pattern using local functions/closures
def influx_client_factory(host='localhost', port=8086):
    def create_client(db=None):
        _client = influxdb.InfluxDBClient(host=host, port=port, database=db if db else None)
        return _client
    return create_client


if __name__ == '__main__':
    get_influx_client = influx_client_factory()

    pprint(f"Closure: {get_influx_client.__closure__}\n")

    for i, cell in enumerate(get_influx_client.__closure__):
        print()
        print(f"Cell {i+1}: {cell}")
        print(f"Cell Type: {cell.__class__}")
        print(f"Cell Size: {cell.__sizeof__()}")
        print(f"Cell Contents: {cell.cell_contents}")
        print(f"Cell Contents Type: {cell.cell_contents.__class__}")
        print(f"Cell Attributes: {cell.__dir__()}")

    dbs = [f'db{i}' for i in range(5)]
    print("\nGenerating 5 clients:")
    for i in range(5):
        client = get_influx_client(db=dbs[i])
        print(f"Client {i+1}: {client}")
        client.close()

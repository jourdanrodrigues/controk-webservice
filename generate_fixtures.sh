#!/usr/bin/env bash
source venv/bin/activate

FIXTURES_PATH=assets/fixtures/
INDENT="--indent 2"

function dump () {
    echo "Dumping $1 to ${FIXTURES_PATH}$2.json"
    python manage.py dumpdata ${INDENT} $1 > ${FIXTURES_PATH}$2.json
}

if [ "$1" != "" ] && [ "$2" != "" ]; then
    dump $1 $2
else
    dump addresses.address addresses
    dump clients.client clients
    dump employees.employee employees
    dump users.user users
    dump suppliers.supplier suppliers
    dump stock.product products
    dump stock.shipment shipments
fi
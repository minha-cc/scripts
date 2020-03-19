from google.cloud import firestore
import csv

def read_csv(csv_file):
  rows = []
  line_count = 0
  with open(csv_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
      line_count += 1
      if line_count == 1:
        continue
      else:
        rows.append(row)
  return rows

def generate_transaction_types(rows):
  transaction_types = []
  for row in rows:
    transaction_types.append({ "description": row[0], "group": row[1], "type": row[2] })
  return transaction_types

def export_to_firestore(transaction_types):
  db = firestore.Client()
  for transaction_type in transaction_types:
    doc_ref = db.collection(u'transactionTypes')
    doc_ref.add({
        u'description': transaction_type['description'],
        u'group': transaction_type['group'],
        u'type': transaction_type['type']
    })

csv_file = '../docs/transactionTypes.csv'
rows = read_csv(csv_file)
transaction_types = generate_transaction_types(rows)
export_to_firestore(transaction_types)

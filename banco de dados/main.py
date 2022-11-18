import psycopg2
from faker import Faker

# conecta no banco de dados
con = psycopg2.connect(
    host='localhost',
    database='caio',
    user='postgres',
    password='14101995'
)
cur = con.cursor()

# carrega lib faker em pt-br
fake = Faker(locale='pt-br')

base_sql = '''
    INSERT INTO seguidores
        (nome, email, usuario)
    VALUES
        ('{}','{}','{}')
    '''

# cria 1000 de registros fakes no banco de dados
for i in range(1000):
    nome = fake.name()
    email = fake.email()
    usuario = fake.user_name()
    sql = base_sql.format(nome, email, usuario)
    cur.execute(sql)

# faz commit no banco de dados e encerra a conexão
con.commit()
con.close()
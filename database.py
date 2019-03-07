from peewee import *

pg_db = PostgresqlDatabase('d2s19l9ch6ocv9', user='twqrxchrmkuhgq', password='057ffeabf4b1063fe6894263ff23578a3dd9cd3df931410dbee2f5fe8a581c33',
                           host='ec2-107-20-185-27.compute-1.amazonaws.com', port=5432)


class Water(Model):
    id = UUIDField(primary_key=True)
    type = CharField(max_length=15)
    owner = CharField(max_length=30)
    start_coordinate_x = FloatField()
    start_coordinate_y = FloatField()
    end_coordinate_x = FloatField()
    end_coordinate_y = FloatField()
    work_info = TextField()
    work_date = DateTimeField()

    class Meta:
        database = pg_db
        db_table = 'water_communication'


class Electricity(Model):
    id = UUIDField(primary_key=True)
    power = IntegerField()
    owner = CharField(max_length=30)
    start_coordinate_x = FloatField()
    start_coordinate_y = FloatField()
    end_coordinate_x = FloatField()
    end_coordinate_y = FloatField()
    work_info = TextField()
    work_date = DateTimeField()
    class Meta:
        database = pg_db
        db_table = 'electricity_communication'


class Data(Model):
    id = UUIDField(primary_key=True)
    owner = CharField(max_length=30)
    start_coordinate_x = FloatField()
    start_coordinate_y = FloatField()
    end_coordinate_x = FloatField()
    end_coordinate_y = FloatField()
    work_info = TextField()
    work_date = DateTimeField()
    class Meta:
        database = pg_db
        db_table = 'data_communication'


class Gas(Model):
    id = UUIDField(primary_key=True)
    owner = CharField(max_length=30)
    start_coordinate_x = FloatField()
    start_coordinate_y = FloatField()
    end_coordinate_x = FloatField()
    end_coordinate_y = FloatField()
    work_info = TextField()
    work_date = DateTimeField()
    class Meta:
        database = pg_db
        db_table = 'gas_communication'
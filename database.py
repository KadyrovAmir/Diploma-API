from peewee import *

pg_db = PostgresqlDatabase('df3bto0r70h9c4', user='vejxbjebcbrbej', password='c88adeedb2d969719c4fb650726c8a72c5b149ea50e77b0eb78c70ab94bf216b',
                           host='ec2-54-247-178-166.eu-west-1.compute.amazonaws.com', port=5432)


class Water(Model):
    id = UUIDField(primary_key=True)
    type = CharField(max_length=15)
    owner = CharField(max_length=30)
    start_coordinate_x = FloatField()
    start_coordinate_y = FloatField()
    end_coordinate_x = FloatField()
    end_coordinate_y = FloatField()
    depth = FloatField()
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
    depth = FloatField()
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
    depth = FloatField()
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
    depth = FloatField()
    work_info = TextField()
    work_date = DateTimeField()
    class Meta:
        database = pg_db
        db_table = 'gas_communication'

class Marker(Model):
    id = UUIDField(primary_key=True)
    coordinate_x = FloatField()
    coordinate_y = FloatField()
    height = FloatField()
    description = CharField()
    class Meta:
        database = pg_db
        db_table = 'marker'


if __name__ == '__main__':
    Water.create_table()
    Electricity.create_table()
    Data.create_table()
    Gas.create_table()
    Marker.create_table()
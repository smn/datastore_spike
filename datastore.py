class BaseRecord(object):
    uuid = AutoField()
    created_at = AutoField()
    updated_at = AutoField()

class BaseEntity(BaseRecord):
    fields = ListField()
    
    def add_field(self, field_name, constraints):


# these types of classes would be generated automatically based
# off the schema
class ClinicEntity(BaseRecord):
    fields

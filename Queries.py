from Database import DataBase


database = DataBase.connection_database()
cursor = database.cursor(buffered=None)


class Queries:
    @staticmethod
    def add(first_name, last_name, mobile_no, email_id, location, state):
        '''
        Performing the Create Operation
        :return: Will return the user which has been added successfully
        '''
        user_add = (
                "insert into details""(first_name,last_name,mobile_no,email_id,location,state)""values(%("
                "first_name)s,%(last_name)s,%(mobile_no)s,%(email_id)s,%(location)s,%(state)s)")
        info = {
                'first_name': first_name,
                'last_name': last_name,
                'mobile_no': mobile_no,
                'email_id': email_id,
                'location': location,
                'state': state
        }
        cursor.execute(user_add, info)
        database.commit()
        return "User Added Successfully"

    @staticmethod
    def retrieve():
        '''
        Preforming the Retrieve Operation
        :return: will return the retrieved database
        '''
        user_retrieve = "select * from details"
        data = cursor.execute(user_retrieve)
        return data

    @staticmethod
    def update(first_name, last_name, mobile_no, email_id, location, state):
        '''
        Performing the Update Operation
        :return: Will return the updated database
        '''
        user_update = "update details set first_name = '%s' where last_name = '%s' where email_id = '%s' where " \
                      "location = '%s' where state = '%s'" %(first_name, last_name, mobile_no, location, state,
                                                             email_id)
        cursor.execute(user_update)
        database.commit()
        return "User Details Updated Successfully"

    @staticmethod
    def delete(first_name):
        '''
        Performing the Delete Operation
        :return: Will Delete The User from the database
        '''
        user_delete = "delete from details set first_name = '%s' where first_name = %d" % (first_name)
        cursor.execute(user_delete)
        database.commit()
        return "User Deleted Successfully"


ss = Queries.retrieve()
print(ss)

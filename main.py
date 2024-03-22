import pymongo


class DbManager:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.client["mydatabase"]
        self.advisor_collection = self.mydb["advisor"]
        self.student_collection = self.mydb["students"]
        self.advisor_student_collection = self.mydb["advisor_student"]

    @classmethod
    def drop_database(cls):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydatabase"]
        client.drop_database(mydb)

    def create_advisor(self, advisor_names):
        self.advisor_collection.insert_many(advisor_names)

    def create_students(self, student_names):
        self.student_collection.insert_many(student_names)

    def create_advisor_student_relationship(self, advisor_id, student_id):
        self.advisor_student_collection.insert_one({"advisor_id": advisor_id, "student_id": student_id})

    def read_advisor_student_relationship(self):
        student_count_by_advisor = []
        for item in self.advisor_student_collection.find({}):
            student_count_by_advisor.append(item['advisor_id'])

        print('სტუდენტების რაოდენობა მრჩეველის მიხედვით')
        for item in range(1, len(list(self.advisor_collection.find({})))+1):
            print(self.advisor_collection.find_one({"_id": item})['name'], '  ', student_count_by_advisor.count(item))


advisor_data = [
    {'_id': 2, 'name': 'adv_luiza'},
    {'_id': 1, 'name': 'adv_kaxa'},
    {'_id': 3, 'name': 'adv_klara'},
    {'_id': 4, 'name': 'adv_kiki'},
    {'_id': 5, 'name': 'adv_zezva'}
]

student_data = [
    {'_id': 1, 'name': 'st_mzia'},
    {'_id': 2, 'name': 'st_mzago'},
    {'_id': 3, 'name': 'st_lamzira'},
    {'_id': 4, 'name': 'st_zenaida'},
    {'_id': 5, 'name': 'st_zoraide'},
    {'_id': 6, 'name': 'st_mariami'},
    {'_id': 7, 'name': 'st_tsira'},
    {'_id': 8, 'name': 'st_tornike'},
    {'_id': 9, 'name': 'st_irakli'},
    {'_id': 10, 'name': 'st_tamari'},
    {'_id': 11, 'name': 'st_levani'},
    {'_id': 12, 'name': 'st_niko'}
]

DbManager.drop_database()
data = DbManager()
data.create_advisor(advisor_data)
data.create_students(student_data)

data.create_advisor_student_relationship(advisor_id=1, student_id=1)
data.create_advisor_student_relationship(advisor_id=1, student_id=2)
data.create_advisor_student_relationship(advisor_id=2, student_id=3)
data.create_advisor_student_relationship(advisor_id=2, student_id=4)
data.create_advisor_student_relationship(advisor_id=2, student_id=5)
data.create_advisor_student_relationship(advisor_id=3, student_id=3)
data.create_advisor_student_relationship(advisor_id=3, student_id=2)
data.create_advisor_student_relationship(advisor_id=3, student_id=10)
data.create_advisor_student_relationship(advisor_id=5, student_id=12)
data.create_advisor_student_relationship(advisor_id=5, student_id=11)
data.create_advisor_student_relationship(advisor_id=5, student_id=8)

data.read_advisor_student_relationship()

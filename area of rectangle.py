class Room:
    len1=0
    bread=0
    def calculate_area_of_rectangle(self):
        len1=int(input("len1: "))
        bread=int(input("bread: "))
        print("area",len1*bread)
study_Room=Room()
study_Room.calculate_area_of_rectangle()

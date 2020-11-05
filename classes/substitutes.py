from classes.pur_beurre import Db


class Substitute:
    def __init__(self, idbarcode, idsubstitute):
        self.idbarcode = idbarcode
        self.idsubstitute = idsubstitute

    def toTuple(self):
        return (self.idbarcode, self.idsubstitute)

    def save(self):
        Db().storeSub([self.toTuple()])

    @staticmethod
    def saveMany(many_sub):
        values = [elem.toTuple() for elem in many_sub]
        Db().storeSub(values)

    @staticmethod
    def getAllSubstitute():
        return Db().getAllSubs()

    @staticmethod
    def deleteSub(idboth):
        Db().delSub(idboth)
        print("Deleted.")

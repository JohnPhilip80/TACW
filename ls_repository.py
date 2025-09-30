class MobileRepository:
    def __init__(self):
        self.mobileList = [
            {
                "id":"1001","brand":"Samsung","owner":"John","price":"45000"
             },
             {
                 "id":"1002","brand":"Apple", "owner":"Lakshmi","price":"65000"
             },
             {
                 "id":"1003","brand":"Redmi", "owner":"Saraswathi","price":"34500"
             }
        ]
        self.nextMobileId = 1004
    def readMobiles(self):
        return self.mobileList
    def insertMobile(self,br,ow,pr):
        mob={
            "id":str(self.nextMobileId),
            "brand":br,
            "owner":ow,
            "price":pr
        }
        self.mobileList.append(mob)
        self.nextMobileId = self.nextMobileId + 1
        return {"message":"Mobile Successfully Inserted"}

    def modifyMobile(self,id,br,ow,pr):
        mobileFound = False
        for mob in self.mobileList:
            if mob["id"]== str(id):
                mobileFound = True
                mob["brand"] = br
                mob["owner"] = ow
                mob["price"] = pr
                break
        if mobileFound:
            return {"message":"Mobile Successfully Updated"}
        else: 
            return {"message":"Mobile not found!"}    
    
    def removeMobile(self,id):
        mobileFound = False
        for mob in self.mobileList:
            if mob["id"] == str(id):
                mobileFound=True
                self.mobileList.remove(mob)
                break
        if mobileFound:
            return {"message":"Mobile Successfully Deleted"}
        else:
            return {"message":"Mobile not found!"}
            
    def displayMobile(self,id):
        mobileFound = False
        mobile = None
        for mob in self.mobileList:
            if mob["id"] == str(id):
                mobileFound = True
                mobile = mob
                break
        if mobileFound:
            return mobile
        else:
            return {"message":"Mobile Not Found"}
                
    
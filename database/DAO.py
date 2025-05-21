from database.DB_connect import DBConnect
from model.airport import Airport


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnectedAirportsID():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """Select distinct a.id
                    from airports a, flights f
                    where a.ID = f.ORIGIN_AIRPORT_ID or a.ID or a.ID = f.DESTiNATION_AIrport_ID
                    order by a.ID ASC """
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnectedAirportsID():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """Select distinct a.id
                        from airports a, flights f
                        where a.ID = f.ORIGIN_AIRPORT_ID or a.ID or a.ID = f.DESTiNATION_AIrport_ID
                        order by a.ID ASC """
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.ORIGIN_AIRPORT_ID, t1.DESTINATION_AIRPORT_ID, coalesce(t1.tot_voli,0)+coalesce(t2.tot_voli,0) as tot_voli, 
                    coalesce(t1.tot_distance,0)+coalesce(t2.tot_distance,0) as tot_distance
                    from 
	                        (select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, sum(f.distance) as tot_distance, count(*) as tot_voli
	                        from flights f
	                        group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) t1
                            left join (select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, sum(distance) as tot_distance, count(*) as tot_voli
                            from flights f
                            group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) t2
                            on t1.ORIGIN_AIRPORT_ID = t2.DESTINATION_AIRPORT_ID and t1.DESTINATION_AIRPORT_ID = t2.ORIGIN_AIRPORT_ID """
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result



    if __name__== '__main__':
        print(getAllAirports())
        print(getConnectedAirportsID())



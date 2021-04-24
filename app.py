from flask import Flask, render_template, json, request, jsonify
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"localhost": "*"}})

# # MySQL configurations
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Hasanbasak'
# app.config['MYSQL_DB'] = 'DBtify'
# app.config['MYSQL_HOST'] = 'localhost'
# mysql = MySQL(app)


# #IMPLEMENT DATA TABLES
# @app.route("/implementDataTables")
# def implementDataTables():
#     cur = mysql.connection.cursor()
    
#     query1 = "CREATE TABLE `albumLikes` (`listenerUsername` varchar(45) DEFAULT NULL,`albumID` varchar(45) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
#     query2 = "CREATE TABLE `albums` (`id` int NOT NULL AUTO_INCREMENT,`genre` varchar(45) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL,`title` varchar(45) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL,`artistNameSurname1` varchar(45) DEFAULT NULL,`artistNameSurname2` varchar(45) DEFAULT NULL,`artistNameSurname3` varchar(45) DEFAULT NULL,`artistNameSurname4` varchar(45) DEFAULT NULL,PRIMARY KEY (`id`),UNIQUE KEY `id_UNIQUE` (`id`)) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
#     query3 = "CREATE TABLE `artists` (`name` varchar(45) DEFAULT NULL,`surname` varchar(45) DEFAULT NULL,`totalLikes` int DEFAULT '0') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
#     query4 = "CREATE TABLE `listeners` (`username` varchar(45) NOT NULL,`e-mail` varchar(45) NOT NULL,PRIMARY KEY (`username`),UNIQUE KEY `username_UNIQUE` (`username`),UNIQUE KEY `e-mail_UNIQUE` (`e-mail`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
#     query5 = "CREATE TABLE `songLikes` (`likeID` int NOT NULL AUTO_INCREMENT,`listenerUsername` varchar(45) NOT NULL,`songID` varchar(45) NOT NULL,PRIMARY KEY (`likeID`)) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
#     query6 = "CREATE TABLE `songs` (`id` int NOT NULL AUTO_INCREMENT,`title` varchar(45) DEFAULT NULL,`albumID` int DEFAULT NULL,`artistNameSurname1` varchar(45) DEFAULT NULL,`artistNameSurname2` varchar(45) DEFAULT NULL,`artistNameSurname3` varchar(45) DEFAULT NULL,`artistNameSurname4` varchar(45) DEFAULT NULL,`totalLikes` int DEFAULT '0',PRIMARY KEY (`id`),UNIQUE KEY `ID_UNIQUE` (`id`)) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
#     cur.execute(query1)
#     cur.execute(query2)
#     cur.execute(query3)
#     cur.execute(query4)
#     cur.execute(query5)
#     cur.execute(query6)



# #STORAGE PROCEDURE
# @app.route("/startStorageProcedure")
# def startStorageProcedure():
#     cur = mysql.connection.cursor()
#     query = "CREATE DEFINER=`root`@`localhost` PROCEDURE `example`(artistName nvarchar(40), artistSurname nvarchar(40)) BEGIN SELECT artistNameSurname1,artistNameSurname2,artistNameSurname3,artistNameSurname4 FROM songs WHERE songs.artistNameSurname1 = CONCAT( artistName, artistSurname) ; END"
#     cur.execute(query)


# #TRIGGER
# @app.route("/deletesongsafteralbumdelete")
# def deletesongsafteralbumdelete():
#     cur = mysql.connection.cursor()
#     query = "CREATE TRIGGER delete_songs AFTER DELETE ON albums FOR EACH ROW BEGIN DELETE FROM songs WHERE songs.albumID = OLD.albumID ; END "
#     cur.execute(query)


# #TRIGGER
# @app.route("/deletelikesafterdeletesong")
# def startTrigger2():
#     cur = mysql.connection.cursor()
#     query = "CREATE TRIGGER delete_likes AFTER DELETE ON songs FOR EACH ROW BEGIN DELETE FROM songLikes WHERE songLikes.songID = OLD.id ; END"
#     cur.execute(query)


# #TRIGGER
# @app.route("/likealbumlikesongs")
# def likealbumlikesongs():
#     cur = mysql.connection.cursor()
#     query = "CREATE TRIGGER like_songs AFTER INSERT ON albumLikes FOR EACH ROW BEGIN INSERT INTO songLikes(listenerUsername, songID) SELECT NEW.listenerUsername, songID FROM songs WHERE songs.albumID = NEW.albumID AND (NEW.listenerUsername, songID) NOT IN (SELECT * FROM songLikes); END"
#     cur.execute(query)
   


@app.route("/findCoworkers")
def main():
    artists = []
    artistName = request.form.get('name')
    artistSurname = request.form.get('surname')

    try:
        cur = mysql.connection.cursor()
        control = cur.callproc('example', [artistName, artistSurname])


        if control > 0:
            datas = cur.fetchall()
            for data in datas:
                obj = {  "artistName1": data[0], "artistName2": data[1], "artistName3": data[2], "artistName4": data[3] }
                artists.append(obj)
        else:
            print("Kayit bulunamadi")

        return jsonify({'data': artists})
    except Exception as e:
        return False



@app.route("/updateAlbum", methods=["PUT"])
def updateAlbum():
    try:
        albumID = request.form.get('id')
        newGenre = request.form.get('newAlbumGenre')
        newTitle = request.form.get('newAlbumTitle')

        cursor = mysql.connection.cursor()
        query = "UPDATE albums SET genre = %s, title = %s WHERE id = %s"
        control = cursor.execute(query,(newGenre, newTitle, albumID))
        mysql.connection.commit()
        return jsonify({'result': True})
    except Exception as e:
        return jsonify({'result': False})
    



@app.route("/deleteAlbum/<id>", methods=["DELETE"])
def deleteAlbum(id):
    try:
        cursor = mysql.connection.cursor()
        sorgu = "DELETE FROM albums WHERE id = %s"
        kontrol = cursor.execute(sorgu,(id,))
        mysql.connection.commit()
        return jsonify({'result': True})
    except Exception as e:
        return jsonify({'result': False})



@app.route("/listAlbumsbyArtistNameSurname", methods=["GET"])
def listAlbumsbyArtistNameSurname():
    albums = []
    try:
        name = request.args.get('inputName')
        surname = request.args.get('inputSurname')
        artistNameSurname = name+surname
        cur = mysql.connection.cursor()
        query = "SELECT * FROM albums WHERE artistNameSurname1 = %s "
        control = cur.execute(query,(artistNameSurname,))

        if control > 0:
            datas = cur.fetchall()

            for data in datas:
                obj = { "id": data[0], "genre": data[1], "title": data[2], "artistName1": data[3], "artistName2": data[4], "artistName3": data[5], "artistName4": data[6] }
                albums.append(obj)
        else:
            print("Kayit bulunamadi")

        return jsonify({'data': albums})
    except Exception as e:
        return False



@app.route("/likeSong", methods=["POST"])
def likeSong():
    try:
        listenerUsername = request.form.get('listenerUsername')
        songID = request.form.get('songID')
        artistID = request.form.get('artistID')

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO `DBtify`.`songLikes` (`listenerUsername`, `songID`) VALUES (%s, %s)", (listenerUsername, songID))
        mysql.connection.commit()

        query = "UPDATE songs SET totalLikes = totalLikes + 1 WHERE id = %s"
        control = cur.execute(query,(songID,))


        query = "UPDATE artists SET totalLikes = totalLikes + 1 WHERE id = %s"
        control = cur.execute(query,(artistID,))

        cur.close()

        return jsonify({'result': True})
    except Exception as e:
        return jsonify({'result': False})



if __name__ == "__main__":
    app.run()



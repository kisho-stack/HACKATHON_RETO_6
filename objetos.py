from connection.conn import Connection
class Alumno:
    def __init__(self,nombre_alumno,edad_alumno):
        self.nombre_alumno = nombre_alumno
        self.edad_alumno = edad_alumno
        self.create_table_alumno()
        
    def create_table_alumno(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumno(
                    Id SERIAL PRIMARY KEY NOT NULL,
                    nombre varchar(50) NOT NULL,
                    edad REAL
            );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
        
    def insert_alumno(self):
        try:
            #[model, price] => model,price
            conn = Connection()
            query = f'''
                INSERT INTO alumno (nombre, edad) 
                VALUES('{self.nombre_alumno}', {self.edad_alumno})
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego alumno -> {self.nombre_alumno}')
        except Exception as e:
            print(f'{str(e)}')
            
    def update_alumno(self, id):
        try:
            
            conn = Connection()
            query = f'''
                UPDATE alumno SET nombre = '{self.nombre_alumno}', edad = {self.edad_alumno} WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo informacion de alumno {id} por -> {self.nombre_alumno} - {self.edad_alumno}')
        except Exception as e:
            print(f'{str(e)}')
            
    def delete_alumno(self, id):
        try:
            
            conn = Connection()
            query = f'''
                DELETE FROM alumno esor WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino registro con ID {id}')
        except Exception as e:
            print(f'{str(e)}')
            
    def fetchall_alumno(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM alumno;
            '''

            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'ID = {row[0]}' )
                print(f'Nombre = {row[1]}')
                print(f'Edad = {row[2]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')
            
        
  
class Profesor:
    def __init__(self,nombre_profesor,edad_profesor):
        self.nombre_profesor = nombre_profesor
        self.edad_profesor = edad_profesor
        self.create_table_profesor()
        
    def create_table_profesor(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS profesor(
                    Id SERIAL PRIMARY KEY NOT NULL,
                    nombre varchar(50) NOT NULL,
                    edad REAL
            );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
        
    def insert_profesor(self):
        try:
            
            conn = Connection()
            query = f'''
                INSERT INTO profesor (nombre, edad) 
                VALUES('{self.nombre_profesor}', {self.edad_profesor})
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego profesor -> {self.nombre_profesor}')
        except Exception as e:
            print(f'{str(e)}')
            
    def update_profesor(self, id):
        try:
            
            conn = Connection()
            query = f'''
                UPDATE profesor SET nombre = '{self.nombre_profesor}', edad = {self.edad_profesor} WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo informacion del profesor {id} por -> {self.nombre_profesor} - {self.edad_profesor}')
        except Exception as e:
            print(f'{str(e)}')
    
    def delete_profesor(self, id):
        try:
            
            conn = Connection()
            query = f'''
                DELETE FROM profesor WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino registro con ID {id}')
        except Exception as e:
            print(f'{str(e)}')
            
    def fetchall_profesor(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM profesor;
            '''

            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'ID = {row[0]}')
                print(f'Nombre = {row[1]}')
                print(f'Edad = {row[2]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')
            
class Salones:
    def __init__(self):
        pass
    def create_table_salones(self):
            
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS salones(
                    id SERIAL PRIMARY KEY NOT NULL,
                    Seccion varchar(50) NOT NULL
                );
                    
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            print(f'{str(e)}')
            
    def fetchall_salones(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM salones;
            '''

            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'ID = {row[0]}')
                print(f'Seccion = {row[1]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')



class Notas:
    def __init__(self,notas):
        self.notas = notas
        self.create_table_notas()
        
    def create_table_notas(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS notas(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nota REAL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
        
    def insert_notas(self):
        try:
            
            conn = Connection()
            query = f'''
                INSERT INTO notas (nota) 
                VALUES('{self.notas}')
            '''
            cursor = conn.execute_query(query)
            conn.commit()         
            print(f'Se agrego nota -> {self.notas}')
        except Exception as e:
            print(f'{str(e)}')
    
    def fetchall_notas(self):
        try:
            conn = Connection()
            query = '''
                SELECT * FROM notas
                ORDER by nota DESC;
            '''

            cursor = conn.execute_query(query)
            rows = cursor.fetchall()
            
            for row in rows:
                print(f'ID = {row[0]}')
                print(f'Notas = {row[1]}')
                print('=====================')
        except Exception as e:
            print(f'{str(e)}')

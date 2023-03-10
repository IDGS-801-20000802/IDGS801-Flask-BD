from db import get_connection

try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call consulta_alumnos()')
        resultset=curso.fetchall()
        for row in resultset:
            print(row)
    connection.close()
    pass
except Exception as ex:
    print('error')
    pass


try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call consulta_alumnos(%s)',(2,))
        row=curso.fetchall()
       # for row in resultset:
        print(type(row))
    connection.close()
    pass
except Exception as ex:
    print('error')
    pass



try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call agrega_alumno(%s, %s, %s)',('xxx', '222', 'sss'))
        #row=curso.fetchall()
        #for row in resultset:
        #print(type(row))
    connection.commit()
    connection.close()
    pass
except Exception as ex:
    print('error')
    pass
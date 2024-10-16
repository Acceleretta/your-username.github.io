from src.database.db_mysql import get_connection


def insertar_cliente(nombreCliente, apellidoPatCliente, apellidoMatCliente, nacimientoCliente, telefonoCliente,
                     correoCliente):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.callproc('sp_insertar_cliente',
                        (nombreCliente, apellidoPatCliente, apellidoMatCliente, nacimientoCliente, telefonoCliente,
                         correoCliente))
    conn.commit()
    conn.close()


def obtener_cliente():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.callproc('sp_obtener_cliente')
            clientes = cursor.fetchall()
    finally:
        conn.close()

    return clientes


def borrar_cliente(id_cliente):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.callproc('sp_borrar_cliente', id_cliente)
    conn.commit()
    conn.close()

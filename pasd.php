<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COVID-19</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
            background-color: #f4f4f4;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            margin: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #007BFF;
            color: white;
        }
        button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 20px;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Resumen Nacional COVID-19</h1>

        <?php
        // Conexión a MySQL
        $conexion = new mysqli("localhost", "root", "", "hola");

        // Verificar conexión
        if ($conexion->connect_error) {
            die("<p style='color: red;'>Error de conexión: " . $conexion->connect_error . "</p>");
        }

        // Primera consulta SQL
        $sql1 = "
        SELECT 
            'OOAD' AS Entidades, 
            COUNT(DISTINCT CASE WHEN del <= '40' THEN del END) AS 'No.', 
            COUNT(DISTINCT CASE WHEN del <= '40' THEN clp END) AS 'Totales',
            COUNT(DISTINCT CASE WHEN status = 0 AND delegoumae NOT LIKE '%umae%' THEN clp END) AS 'Con carga de pacientes',
            (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE 'SUMAE%' AND del <= '40') AS Cargados,
            (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%UMAE%' AND STATUS = 1) AS 'Validados',
            (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%UMAE%' AND STATUS = 5) AS 'Sin registro de Atencion',
            (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%UMAE%' AND STATUS = 6) AS 'MARSS',
            (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%UMAE%' AND STATUS = 0) AS 'Pendientes por Validar'
        FROM registro
        WHERE delegoumae NOT LIKE 'SUMAE%' AND del <= '40'
        UNION ALL
        SELECT 
            'UMAE' AS Entidades,
            COUNT(DISTINCT CASE WHEN del > '40' THEN del END) AS 'No.',
            COUNT(DISTINCT CASE WHEN del > '40' THEN clp END) AS 'Totales',
            COUNT(DISTINCT CASE WHEN status = 0 AND delegoumae LIKE '%umae%' THEN clp END) AS 'Con carga de pacientes',
            (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE 'SUMAE%' AND del > '40') AS Cargados,
            (SELECT COUNT(*) FROM registro WHERE delegoumae LIKE '%UMAE%' AND STATUS = 1) AS 'Validados',
            (SELECT COUNT(*) FROM registro WHERE delegoumae LIKE '%UMAE%' AND STATUS = 5) AS 'Sin registro de Atencion',
            (SELECT COUNT(*) FROM registro WHERE delegoumae LIKE '%UMAE%' AND STATUS = 6) AS 'MARSS',
            (SELECT COUNT(*) FROM registro WHERE delegoumae LIKE '%UMAE%' AND STATUS = 0) AS 'Pendientes por Validar'
        FROM registro
        WHERE delegoumae NOT LIKE 'SUMAE%'
        UNION ALL
SELECT 
    'Nacional' AS Entidades, 
    COUNT(DISTINCT del) AS 'No.',
    COUNT(DISTINCT clp) AS 'Totales',
    COUNT(DISTINCT CASE WHEN status = 0 THEN clp END) AS 'Con carga de pacientes',
    (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE 'SUMAE%') AS Cargados,
    (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%OOAD%' AND STATUS = 1) AS 'Validados',
    (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%OOAD%' AND STATUS = 5) AS 'Sin registro de Atencion',
    (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%OOAD%' AND STATUS = 6) AS 'MARSS',
    (SELECT COUNT(*) FROM registro WHERE delegoumae NOT LIKE '%OOAD%' AND STATUS = 0) AS 'Pendientes por Validar'
FROM registro
WHERE delegoumae NOT LIKE 'SUMAE%'";

        $resultado1 = $conexion->query($sql1);

        if ($resultado1->num_rows > 0) {
            echo "<h2>Tabla 1</h2>";
            echo "<table>";
            echo "<tr><th>Entidades</th><th>No.</th><th>Totales</th><th>Con Carga</th><th>Cargados</th><th>Validados</th><th>Sin Registro</th><th>MARSS</th><th>Pendientes</th></tr>";
            
            while ($fila = $resultado1->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $fila["Entidades"] . "</td>";
                echo "<td>" . $fila["No."] . "</td>";
                echo "<td>" . $fila["Totales"] . "</td>";
                echo "<td>" . $fila["Con carga de pacientes"] . "</td>";
                echo "<td>" . $fila["Cargados"] . "</td>";
                echo "<td>" . $fila["Validados"] . "</td>";
                echo "<td>" . $fila["Sin registro de Atencion"] . "</td>";
                echo "<td>" . $fila["MARSS"] . "</td>";
                echo "<td>" . $fila["Pendientes por Validar"] . "</td>";
                echo "</tr>";
            }
            echo "</table>";
        }

        // Segunda consulta SQL
        $sql2 = "
        SELECT 
            ROW_NUMBER() OVER (ORDER BY delegoumae ASC) AS `No.`,
            delegoumae AS `OOAD/UMAE`,
            (SELECT COUNT(*) FROM unidades u WHERE u.delegoumae = r.delegoumae) AS Total,
            COUNT(*) AS Carga_Inicial,  
            SUM(CASE WHEN STATUS = 1 THEN 1 ELSE 0 END) AS Registros_Validados,
            SUM(CASE WHEN STATUS = 5 THEN 1 ELSE 0 END) AS Sin_Registro_de_Atencion,
            SUM(CASE WHEN STATUS = 6 THEN 1 ELSE 0 END) AS MARSS,
            SUM(CASE WHEN STATUS = 0 THEN 1 ELSE 0 END) AS Registros_Por_Validar_En_La_Unidad
        FROM registro r
        WHERE r.delegoumae NOT LIKE '%UMAE%'
        GROUP BY r.delegoumae
        ORDER BY `OOAD/UMAE` ASC";

        $resultado2 = $conexion->query($sql2);

        if ($resultado2->num_rows > 0) {
            echo "<h2>Tabla 2</h2>";
            echo "<table>";
            echo "<tr><th>No.</th><th>OOAD/UMAE</th><th>Total</th><th>Carga Inicial</th><th>Validados</th><th>Sin Registro</th><th>MARSS</th><th>Por Validar</th></tr>";
            
            while ($fila = $resultado2->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $fila["No."] . "</td>";
                echo "<td>" . $fila["OOAD/UMAE"] . "</td>";
                echo "<td>" . $fila["Total"] . "</td>";
                echo "<td>" . $fila["Carga_Inicial"] . "</td>";
                echo "<td>" . $fila["Registros_Validados"] . "</td>";
                echo "<td>" . $fila["Sin_Registro_de_Atencion"] . "</td>";
                echo "<td>" . $fila["MARSS"] . "</td>";
                echo "<td>" . $fila["Registros_Por_Validar_En_La_Unidad"] . "</td>";
                echo "</tr>";
            }
            echo "</table>";
        }

        $conexion->close();
        ?>
    </div>

</body>
</html>

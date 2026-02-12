"""
Script de Procesamiento de Datos - Prueba 3
Desarrollado por: Desarrollador Senior Python Alejandro Reyes
Fecha: 12 de febrero de 2026

Descripción: 
Este script procesa un archivo CSV con información de empleados,
calcula estadísticas básicas y filtra registros según criterios específicos.
"""

import pandas as pd
import json
from pathlib import Path 


def cargar_datos(ruta_archivo):
    """
    Cargo el archivo CSV en un DataFrame de pandas.
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV
    
    Returns:
        DataFrame: Datos cargados desde el CSV
    """
    print(f"Cargando datos desde: {ruta_archivo}")
    df = pd.read_csv(ruta_archivo)
    print(f"Archivo cargado exitosamente\n")
    return df


def contar_registros(df):
    """
    Cuento el número total de registros en el DataFrame.
    
    Args:
        df (DataFrame): DataFrame con los datos
    
    Returns:
        int: Número total de registros
    """
    conteo = len(df)
    print(f"Total de registros: {conteo}")
    return conteo


def calcular_promedios(df):
    """
    Calculo los promedios de las columnas numéricas Age y Salary.
    
    Args:
        df (DataFrame): DataFrame con los datos
    
    Returns:
        dict: Diccionario con los promedios calculados
    """
    promedio_edad = df['Age'].mean()
    promedio_salario = df['Salary'].mean()
    
    print(f"Promedio de Edad: {promedio_edad:.2f} años")
    print(f"Promedio de Salario: ${promedio_salario:,.2f}\n")
    
    return {
        'promedio_edad': round(promedio_edad, 2),
        'promedio_salario': round(promedio_salario, 2)
    }


def filtrar_salarios_superiores(df, promedio_salario):
    """
    Filtro los registros donde el salario es mayor al promedio.
    
    Args:
        df (DataFrame): DataFrame con los datos
        promedio_salario (float): Salario promedio calculado
    
    Returns:
        list: Lista de registros que cumplen el criterio
    """
    # Aplicar el filtro
    df_filtrado = df[df['Salary'] > promedio_salario]
    
    print(f"Registros con salario superior al promedio: {len(df_filtrado)}")
    print("=" * 60)
    
    # Convertir el DataFrame filtrado a lista de diccionarios
    registros_filtrados = df_filtrado.to_dict('records')
    
    # Mostrar los registros filtrados en la terminal
    if registros_filtrados:
        print("\nEmpleados con salario superior al promedio:")
        print("-" * 60)
        for registro in registros_filtrados:
            print(f"  • {registro['Name']} - Edad: {registro['Age']} - "
                  f"Salario: ${registro['Salary']:,} - Dept: {registro['Department']}")
        print()
    
    return registros_filtrados


def guardar_resultados(conteo, promedios, registros_filtrados, archivo_salida):
    """
    Guardo los resultados en un archivo JSON con formato solicitado.
    
    Args:
        conteo (int): Total de registros
        promedios (dict): Diccionario con los promedios
        registros_filtrados (list): Lista de registros filtrados
        archivo_salida (str): Nombre del archivo de salida
    """
    # Estructura del JSON con información detallada del filtro
    resultados = {
        'estadisticas': {
            'total_registros': conteo,
            'promedio_edad': promedios['promedio_edad'],
            'promedio_salario': promedios['promedio_salario']
        },
        'filtro': {
            'criterio': f"Salario mayor a {promedios['promedio_salario']}",
            'cantidad_encontrada': len(registros_filtrados),
            'registros': registros_filtrados
        }
    }
    
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    
    print(f"Resultados guardados en: {archivo_salida}")


def mostrar_resumen_final(conteo, promedios, registros_filtrados):
    """
    Muestro un resumen final de los resultados en la terminal.
    
    Args:
        conteo (int): Total de registros
        promedios (dict): Diccionario con los promedios
        registros_filtrados (list): Lista de registros filtrados
    """
    print("\n" + "=" * 60)
    print("RESUMEN DE ESTADÍSTICAS FINALES")
    print("=" * 60)
    print(f"Total de empleados procesados: {conteo}")
    print(f"Promedio de edad: {promedios['promedio_edad']} años")
    print(f"Promedio de salario: ${promedios['promedio_salario']:,}")
    print(f"Empleados con salario superior al promedio: {len(registros_filtrados)}")
    print("=" * 60)
    print("Proceso completado exitosamente\n")


def main():
    """
    Función principal que coordina la ejecución del script.
    """
    try:
        # Configuración de rutas
        archivo_entrada = "Seccion 3_Desarrollo en Python - Script de Procesamiento de Datos.csv"
        archivo_salida = "resultados_estadisticas.json"
        
        print("\n" + "=" * 60)
        print("INICIO DEL PROCESAMIENTO DE DATOS")
        print("=" * 60 + "\n")
        
        # 1. Cargar datos
        df = cargar_datos(archivo_entrada)
        
        # 2. Contar registros
        conteo = contar_registros(df)
        print()
        
        # 3. Calcular promedios
        promedios = calcular_promedios(df)
        
        # 4. Filtrar registros con salario superior al promedio
        registros_filtrados = filtrar_salarios_superiores(
            df, 
            promedios['promedio_salario']
        )
        
        # 5. Guardar resultados en JSON
        guardar_resultados(conteo, promedios, registros_filtrados, archivo_salida)
        
        # 6. Mostrar resumen final
        mostrar_resumen_final(conteo, promedios, registros_filtrados)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
        print("   Verifica que el archivo esté en el directorio correcto.")
    
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío.")
    
    except KeyError as e:
        print(f"Error: Columna no encontrada en el CSV: {e}")
        print("   Verifica que el archivo tenga las columnas: ID, Name, Age, Salary, Department")
    
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}")
        print(f"   Detalle: {str(e)}")


if __name__ == "__main__":
    main()

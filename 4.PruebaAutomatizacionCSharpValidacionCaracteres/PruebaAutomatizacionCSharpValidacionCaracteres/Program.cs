Console.WriteLine("═══════════════════════════════════════════════════════════════");
Console.WriteLine("  APLICACIÓN DE VALIDACIÓN DE CADENAS");
Console.WriteLine("═══════════════════════════════════════════════════════════════\n");

// Solicitar entrada de cadenas
Console.Write("Ingrese una lista de cadenas separadas por comas: ");
string? entradaCadenas = Console.ReadLine();

// Validar que la entrada no esté vacía
if (string.IsNullOrWhiteSpace(entradaCadenas))
{
    Console.WriteLine("\n❌ Error: La entrada no puede estar vacía.");
    return;
}

// Dividir las cadenas y limpiar espacios
string[] listaCadenas = entradaCadenas
    .Split(',')
    .Select(c => c.Trim())
    .Where(c => !string.IsNullOrEmpty(c))
    .ToArray();

if (listaCadenas.Length == 0)
{
    Console.WriteLine("\n❌ Error: No se encontraron cadenas válidas.");
    return;
}

// Solicitar el carácter a contar
Console.Write("Ingrese el carácter que desea contar en cada cadena: ");
string? entradaCaracter = Console.ReadLine();

if (string.IsNullOrEmpty(entradaCaracter) || entradaCaracter.Length != 1)
{
    Console.WriteLine("\n❌ Error: Debe ingresar exactamente un carácter.");
    return;
}

char caracterBuscado = entradaCaracter[0];

// Procesar cada cadena
Console.WriteLine("\n═══════════════════════════════════════════════════════════════");
Console.WriteLine("  RESULTADOS DE VALIDACIÓN");
Console.WriteLine("═══════════════════════════════════════════════════════════════\n");

for (int i = 0; i < listaCadenas.Length; i++)
{
    string cadenaActual = listaCadenas[i];
    
    Console.WriteLine($"───────────────────────────────────────────────────────────────");
    Console.WriteLine($"Cadena #{i + 1}: \"{cadenaActual}\"");
    Console.WriteLine($"───────────────────────────────────────────────────────────────");
    
    // Aplicar validaciones
    bool esAlfabetico = EsAlfabetico(cadenaActual);
    bool rangoLongitudValido = RangoLongitud(cadenaActual);
    int cantidadCaracter = ContarCaracter(cadenaActual, caracterBuscado);
    
    // Mostrar resultados
    Console.WriteLine($"  ✓ Es Alfabético: {(esAlfabetico ? "SÍ" : "NO")}");
    Console.WriteLine($"  ✓ Longitud ({cadenaActual.Length} caracteres): {(rangoLongitudValido ? "VÁLIDA (5-10)" : "INVÁLIDA (fuera del rango 5-10)")}");
    Console.WriteLine($"  ✓ Ocurrencias del carácter '{caracterBuscado}': {cantidadCaracter}");
    Console.WriteLine();
}

Console.WriteLine("═══════════════════════════════════════════════════════════════");
Console.WriteLine("  PROCESO COMPLETADO");
Console.WriteLine("═══════════════════════════════════════════════════════════════");

// ═══════════════════════════════════════════════════════════════
// FUNCIONES DE VALIDACIÓN
// ═══════════════════════════════════════════════════════════════

/// <summary>
/// Verifica si una cadena contiene únicamente letras (sin números ni símbolos).
/// </summary>
/// <param name="cadena">Cadena a validar</param>
/// <returns>True si la cadena contiene solo letras, False en caso contrario</returns>
static bool EsAlfabetico(string cadena)
{
    if (string.IsNullOrEmpty(cadena))
        return false;
    
    return cadena.All(char.IsLetter);
}

/// <summary>
/// Valida si la longitud de una cadena está entre 5 y 10 caracteres inclusive.
/// </summary>
/// <param name="cadena">Cadena a validar</param>
/// <returns>True si la longitud está en el rango válido, False en caso contrario</returns>
static bool RangoLongitud(string cadena)
{
    if (string.IsNullOrEmpty(cadena))
        return false;
    
    int longitud = cadena.Length;
    return longitud >= 5 && longitud <= 10;
}

/// <summary>
/// Cuenta cuántas veces aparece un carácter específico en una cadena (sin distinguir mayúsculas/minúsculas).
/// </summary>
/// <param name="cadena">Cadena donde buscar</param>
/// <param name="caracterBuscado">Carácter a contar</param>
/// <returns>Número de ocurrencias del carácter en la cadena</returns>
static int ContarCaracter(string cadena, char caracterBuscado)
{
    if (string.IsNullOrEmpty(cadena))
        return 0;
    
    return cadena.Count(c => char.ToLowerInvariant(c) == char.ToLowerInvariant(caracterBuscado));
}

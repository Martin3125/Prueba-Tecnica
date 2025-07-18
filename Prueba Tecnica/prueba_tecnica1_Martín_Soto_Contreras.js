//Debe ser realizada solo con algoritmia, sin librerías asociadas más que las propiedades del lenguaje.
//Dado un horario en formato de 12 horas con AM o PM (ej: hh:mm:ssAM o hh:mm:ssPM), escribe una función que convierta ese horario al formato de 24 horas (militar).
function convertirHora12a24(s) {
    // Validar largo
    if (s.length !== 10) {
        return "Formato incorrecto. Usa hh:mm:ssAM o hh:mm:ssPM";
    }

    // Validar sufijo AM o PM
    const periodo = s.slice(8);
    if (periodo !== "AM" && periodo !== "PM") {
        return "Falta el indicador AM o PM al final.";
    }

    // Validar separadores de tiempo
    if (s[2] !== ':' || s[5] !== ':') {
        return "Formato incorrecto. Usa ':' como separadores de hora, minutos y segundos.";
    }

    // Extraer partes
    const horaStr = s.slice(0, 2);
    const minutosStr = s.slice(3, 5);
    const segundosStr = s.slice(6, 8);

    // Convertir a números
    const hora = parseInt(horaStr);
    const minutos = parseInt(minutosStr);
    const segundos = parseInt(segundosStr);

    if (isNaN(hora) || isNaN(minutos) || isNaN(segundos)) {
        return "Los valores de hora, minutos o segundos no son números válidos.";
    }

    if (hora < 1 || hora > 12) {
        return "La hora debe estar entre 01 y 12.";
    }
    if (minutos < 0 || minutos >= 60) {
        return "Los minutos deben estar entre 00 y 59.";
    }
    if (segundos < 0 || segundos >= 60) {
        return "Los segundos deben estar entre 00 y 59.";
    }

    // Convertir hora
    let hora24 = hora;
    if (periodo === "AM") {
        if (hora === 12) {
            hora24 = 0;
        }
    } else { // PM
        if (hora !== 12) {
            hora24 = hora + 12;
        }
    }

    const horaFinal = hora24 < 10 ? "0" + hora24 : "" + hora24;

    return `${horaFinal}:${minutosStr}:${segundosStr}`;
}
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Ingresa la hora en formato 12h (ej: 07:05:45PM): ", function (entrada) {
    const resultado = convertirHora12a24(entrada);
    console.log("Resultado:", resultado);
    rl.close();
});
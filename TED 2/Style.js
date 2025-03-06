function coletarDados() {
    let alturas = [];
    let generos = [];
    
    for (let i = 0; i < 15; i++) {  // Altere de 2 para 15 aqui
        let altura = parseFloat(prompt(`Digite a altura da pessoa ${i + 1}:`));
        let genero = prompt(`Digite o gênero da pessoa ${i + 1} (Masculino ou Feminino):`).toLowerCase().trim();
        
        // Verificação para garantir que o gênero seja válido
        while (genero !== 'masculino' && genero !== 'feminino') {
            alert("Gênero inválido. Por favor, digite 'Masculino' ou 'Feminino'.");
            genero = prompt(`Digite o gênero da pessoa ${i + 1} (Masculino ou Feminino):`).toLowerCase().trim();
        }
        
        alturas.push(altura);
        generos.push(genero);
    }
    
    return { alturas, generos };
}

function calcularMaiorMenorAltura(alturas) {
    let maiorAltura = Math.max(...alturas);
    let menorAltura = Math.min(...alturas);
    return { maiorAltura, menorAltura };
}

function calcularMediaMasculino(alturas, generos) {
    let masculinoAlturas = [];
    
    for (let i = 0; i < generos.length; i++) {
        if (generos[i] === 'masculino') {
            masculinoAlturas.push(alturas[i]);
        }
    }
    
    let mediaMasculino = masculinoAlturas.length > 0 
        ? masculinoAlturas.reduce((acc, curr) => acc + curr, 0) / masculinoAlturas.length 
        : 0;
    
    return mediaMasculino;
}

function contarFeminino(generos) {
    return generos.filter(genero => genero === 'feminino').length;
}

function main() {
    const { alturas, generos } = coletarDados();
    
    const { maiorAltura, menorAltura } = calcularMaiorMenorAltura(alturas);
    const mediaMasculino = calcularMediaMasculino(alturas, generos);
    const numeroFeminino = contarFeminino(generos);
    
    alert(`\nMaior altura do grupo: ${maiorAltura} metros`);
    alert(`Menor altura do grupo: ${menorAltura} metros`);
    alert(`Média de altura do gênero Masculino: ${mediaMasculino.toFixed(2)} metros`);
    alert(`Número de pessoas do gênero Feminino: ${numeroFeminino}`);
}

// Chama a função principal
main();

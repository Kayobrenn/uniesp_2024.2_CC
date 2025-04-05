//Crie um array com 5 nomes e exiba o terceiro nome no console.
//•Adicione um nome ao final e um no início do array.
//•Remova o último nome e exiba o array atualizado.
//•Use map() para criar um novo array dobrando os valores de [2, 4, 6, 8].
//•Use filter() para criar um novo array apenas com números maiores que 5 em [1, 3, 5, 7, 9]

let nomes = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo"];

console.log("Terceiro nome:", nomes[2]);

nomes.push("Fernanda");  
nomes.unshift("Gabriel"); 

nomes.pop();
console.log("Array atualizado:", nomes);

const numeros = [2, 4, 6, 8];
const dobrados = numeros.map(num => num * 2);
console.log("Valores dobrados:", dobrados);

const numeros2 = [1, 3, 5, 7, 9];
const maioresQue5 = numeros2.filter(num => num > 5);
console.log("Números maiores que 5:", maioresQue5);

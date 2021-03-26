fn unpackVector(vetor: Vec<char>) -> Vec<char>{
    let mut pilha: Vec<char> = vec![];
    for c in vetor.iter(){
        if *c == '#'{
            if pilha.len() != 0{
                pilha.pop();
            }
        } else if *c == '@'{
            if pilha.len() != 0 {
                pilha = vec![];
            }
        } else {
            pilha.push(*c);
        }
    }
    return pilha;
}

fn main() {
    let vetorTeste1 = vec!['A','B','R','A','C','O','B','R','#','#','#','A','D','A','B','R','A'];
    let vetorTeste2 = vec!['A','B','R','A','C','A','@','A','L','A','K','A','S','#','Z','A','M'];
    let resultado1 = unpackVector(vetorTeste1);
    let resultado2 = unpackVector(vetorTeste2);
    println!(" teste 1: {:?}", resultado1);
    println!(" teste 2: {:?}", resultado2);
}

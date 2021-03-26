fn unpack_vector(vetor: Vec<char>) -> Vec<char>{
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
    let vetor_teste_1 = vec!['A','B','R','A','C','O','B','R','#','#','#','A','D','A','B','R','A'];
    let vetor_teste_2 = vec!['A','B','R','A','C','A','@','A','L','A','K','A','S','#','Z','A','M'];
    let resultado_1 = unpack_vector(vetor_teste_1);
    let resultado_2 = unpack_vector(vetor_teste_2);
    println!(" teste 1: {:?}", resultado_1);
    println!(" teste 2: {:?}", resultado_2);
}

const lis = document.querySelector('#filmes');

function carregarFilmes() {
    fetch('http://localhost:8000/get_lista')
        .then((res) => res.json())
        .then((data) => {
            data.map((lista) => {
                lis.innerHTML += `
                    <li>
                        <img src="${lista.capa}" width="100"/> <br>
                        <strong>Nome do filme:</strong> ${lista.nome} <br>
                        <strong>Atores:</strong> ${lista.atores} <br>
                        <strong>Diretor(a):</strong> ${lista.diretor} <br>
                        <strong>Data:</strong> ${lista.data} <br>
                        <strong>Gênero:</strong> ${lista.gênero} <br>
                        <strong>Produtora:</strong> ${lista.produtora} <br>
                        <strong>Sinopse:</strong> ${lista.sinopse} <br>
                        <hr>
                    </li>
                `;
            });
        });
}

function deletar_filme() {
    const nome = document.getElementById("deletarFilme").value;

    fetch("http://localhost:8000/deletar_filmes", {
        method: "DELETE",
        headers: { "Content-Type": "text/html" },
        body: `nome_filme=${encodeURIComponent(nome)}`
    })
    .then(res => res.text())
    .then(msg => {
        alert(msg);
        carregarFilmes();
    });
}

function editar_filme() {
    const nome = document.getElementById("tituloFilme").value;
    const novoNome = document.getElementById("novoNome").value;
    const novoAtores = document.getElementById("novoAtores").value;
    const novoDiretor = document.getElementById("novoDiretor").value;
    const novoAno = document.getElementById("novoAno").value;
    const novoGenero = document.getElementById("novoGenero").value;
    const novoProdutora = document.getElementById("novoProdutora").value;
    const novaSinopse = document.getElementById("novaSinopse").value;
    const novaCapa = document.getElementById("novaCapa").value;

    const dados = `nome_filme=${encodeURIComponent(nomeOriginal)}&nome=${encodeURIComponent(novoNome)}&atores=${encodeURIComponent(novoAtores)}&diretor=${encodeURIComponent(novoDiretor)}&data=${encodeURIComponent(novoAno)}&gênero=${encodeURIComponent(novoGenero)}&produtora=${encodeURIComponent(novoProdutora)}&sinopse=${encodeURIComponent(novaSinopse)}&capa=${encodeURIComponent(novaCapa)}`;

    fetch("http://localhost:8000/editar_filme", {
        method: "PUT",
        headers: { "Content-Type": "text/html" },
        body: dados
    })
    .then(res => res.text())
    .then(msg => {
        alert(msg);
        carregarFilmes(); 
    });
}

carregarFilmes();

from django.shortcuts import render

def inicio(requisicao):
    return render(requisicao, "tarefas/inicio.html")

def listaTarefas(requisicao):
    tarefas = [
        {
            "titulo": "Estudar rotas no Django",
            "prioridade": "Alta",
            "situacao": "Pendente",
        },
        {
            "titulo": "Criar modelo de listagem",
            "prioridade": "Media",
            "situacao": "Concluida",
        },
        {
            "titulo": "Registrar aplicacao no projeto",
            "prioridade": "Alta",
            "situacao": "Concluida",
        },
    ]
    return render(requisicao, "tarefas/lista.html", {"tarefas": tarefas})

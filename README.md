# alf-webservice
Para utilizar a aplicação e realizar os testes você deverá ter instalado em sua máquina o IDE PyCharme Community Edition, utilizei a versão 2020.3.2, e também o PostMan para testar os métodos;
Baixe o projeto no repositório e abra o projeto no PyCharme;
Execute o projeto clicando no ícone de Play;
Para cadastrar os gabaritos siga as instruções abaixo:
   Entre no PostMan, escolha o método Post, e coloque o seguinte caminho: localhost/cadastra_gabarito
   Escolha a opção Body e coloque os dados para cadastro em formato JSON. Ex:
      {"Prova 1":[{"Questao":1,"Resposta":"F","Peso":3},{"Questao":2,"Resposta":"D","Peso":1},{"Questao":3,"Resposta":"D","Peso":1}]}
   Lembre-se de escolher o formato JSON;
   Depois clique em Send;
   As respostas aparecerão na tela logo abaixo da tela onde você colocou os dados;
   Cadastre os gabaritos que desejar seguindo esses mesmos passos.
Para cadastrar as respostas dos alunos siga as instruções a seguir:
   Entre no PostMan, escolha o método Post, e coloque o seguinte caminho: localhost/cadastra_respostas_aluno
   Escolha a opção Body e coloque os dados para cadastro em formato JSON. Ex:
     {
   "Aluno": [
      {
        "Prova1": [
         {
           "Questao": 1,
            "Resposta": "F"
         },
          {
           "Questao": 2,
            "Resposta": "D"
         },
         {
            "Questao": 3,
            "Resposta": "D"
          }
       ]
     },
     {
       "Prova2": [
          {
           "Questao": 1,
           "Resposta": "F"
          },
         {
            "Questao": 2,
           "Resposta": "D"
         },
          {
            "Questao": 3,
            "Resposta": "D"
         }
       ]
      }
   ]
  }
   Lembre-se de escolher o formato JSON;
   Depois clique em Send;
   Cadastre as respostas que desejar seguindo esses mesmos passos.
 Para visualizar as respostas do aluno siga os passos a seguir:
     Entre no PostMan, escolha o método GET, e coloque o seguinte caminho: localhost/valida_respostas_aluno;
     Em Params coloque o valor aluno como KEY e o nome do aluno como VALUE;
      Depois clique em Send;
  

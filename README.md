# Boas-vindas ao Tandembot!

Um chatbot de conversação por voz que utiliza reconhecimento de fala, síntese de fala e inteligência artificial via API do Google Gemini para interagir com os usuários.

- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplo de uso](#exemplo-de-uso)
- [Futuras melhorias](#futuras-melhorias)
- [Agradecimentos](#agradecimentos)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Funcionalidades

- Gravação de áudio da entrada do usuário.
- Reconhecimento de fala para converter a entrada do usuário em texto.
- Interação com um modelo de inteligência artificial para gerar respostas.
- Síntese de fala para transformar as respostas do chatbot em áudio.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python listadas em `requirements.txt`
- Credenciais válidas para API do Gemini

## Instalação

1. Clone o repositório: 
```bash
git clone https://github.com/anacletu/virtual_tandem
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API, endpoint e preferências de áudio:
```env
API_KEY=sua_chave_api
API_URL=https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent
FS=44100
DURATION=15
```

## Uso
Execute o script principal:

```
python main.py
```

Siga as instruções no terminal para interagir com o chatbot.
O script irá fazer uma solicitação para a API, converter a resposta em fala e reproduzir o áudio.

## Exemplo de uso
<video width="640" height="360" controls>
  <source src="https://youtu.be/8vUDbbJG6x4">
  Your browser does not support the video tag.
</video>

![Video Title](https://youtu.be/8vUDbbJG6x4)

## Futuras Melhorias
- Adição de suporte para mais idiomas.
- Implementação de uma interface gráfica para facilitar a interação.
- Melhoria da robustez do reconhecimento de fala e da síntese de fala.
- Mair possibilidades de configuração, como nível do idioma e complexidade de resposta.

## Agradecimentos
Este projeto foi desenvolvido como parte da Imersão de Inteligência Artificial promovida pela Alura e Google. Agradeço às instituições por proporcionarem uma experiência educacional valiosa e prática.

## Contribuições
Contribuições são bem-vindas! Para sugestões, correções de bugs e outras alterações, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo de [licença](LICENSE) para mais detalhes.


# Editor de Imagens com Filtros
## Descrição
Este projeto é um editor de imagens que permite aplicar uma variedade de filtros em imagens. Ele utiliza a biblioteca Streamlit para criar uma interface interativa onde os usuários podem carregar imagens, selecionar filtros e visualizar os resultados em tempo real. Os filtros implementados incluem:
- **Grayscale (Escala de Cinza)**
- **Blur (Desfoque)**
- **Edge Detection (Detecção de Bordas)**
- **Sharpen (Aumento de Nitidez)**
- **Sobel (Filtro Sobel)**
## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **OpenCV**: Biblioteca para manipulação de imagens.
- **NumPy**: Biblioteca para operações numéricas.
- **Streamlit**: Framework para a criação de aplicações web interativas.
## Instalação
### Requisitos
Certifique-se de que você possui Python 3.x instalado em seu sistema. Você pode verificar a versão do Python com:
```bash
python --version
```
### Clonando o Repositório
Clone este repositório para sua máquina local:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
### Criando um Ambiente Virtual
É recomendável criar um ambiente virtual para gerenciar as dependências do projeto:
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scriptsctivate
```
### Instalando Dependências
Instale as dependências necessárias usando pip:
```bash
pip install -r requirements.txt
```
**Nota:** Certifique-se de que um arquivo `requirements.txt` está incluído no repositório, contendo as bibliotecas necessárias, como `opencv-python`, `numpy`, `streamlit`.
## Uso
### Executando a Aplicação
Para iniciar a aplicação, execute o seguinte comando:
```bash
streamlit run app.py
```
Isso abrirá a aplicação em seu navegador padrão. A partir daí, você poderá:
- Carregar uma imagem no formato JPG ou PNG.
- Selecionar um filtro a ser aplicado.
- Visualizar a imagem original e a imagem editada lado a lado ou usar um controle deslizante para ver a transformação.
### Interface do Usuário
A interface do aplicativo é dividida em:
- **Área de Carregamento**: Permite ao usuário carregar uma imagem do sistema.
- **Menu de Seleção de Filtros**: Permite ao usuário escolher entre os filtros disponíveis.
- **Visualização**: Permite ao usuário escolher entre visualizar a imagem editada completa ou usar um controle deslizante para comparar a imagem original e editada.
## Exemplos
Visualização da Interface
## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou um pull request.
## Licença
Este projeto está licenciado sob a Licença MIT.
## Observações Finais
- Substitua `https://github.com/seu-usuario/nome-do-repositorio.git` pelo link real do seu repositório.
- Atualize o caminho da imagem de exemplo, se necessário.
- Se você tiver mais informações específicas ou funcionalidades adicionais que gostaria de incluir, sinta-se à vontade para adicioná-las ao README.
Depois de criar ou atualizar o README, você pode adicioná-lo ao seu repositório GitHub e fazer o commit:
```bash
git add README.md
git commit -m "Adiciona README detalhado"
git push
```
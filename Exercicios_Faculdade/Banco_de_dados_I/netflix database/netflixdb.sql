--
-- File generated with SQLiteStudio v3.3.3 on qua jun 29 02:48:38 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: assinaturas
CREATE TABLE assinaturas (id_assinatura INTEGER PRIMARY KEY AUTOINCREMENT, id_usuario INTEGER REFERENCES usuarios (id_usuario), id_plano INTEGER REFERENCES planos (id_plano), validade DATE NOT NULL, inicio_assinatura DATE NOT NULL);
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (1, 9, 3, '2022-01-25', '2021-12-25');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (2, 3, 1, '2022-04-01', '2022-03-01');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (3, 2, 2, '2022-03-05', '2021-06-25');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (4, 1, 3, '2022-04-05', '2022-01-05');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (5, 4, 3, '2022-08-01', '2021-03-20');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (6, 5, 2, '2022-02-20', '2021-12-25');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (7, 6, 2, '2021-12-15', '2021-09-15');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (8, 7, 2, '2022-04-20', '2022-03-20');
INSERT INTO assinaturas (id_assinatura, id_usuario, id_plano, validade, inicio_assinatura) VALUES (9, 8, 3, '2022-02-15', '2022-01-15');

-- Table: atores
CREATE TABLE atores (id_ator INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (80) NOT NULL);
INSERT INTO atores (id_ator, nome) VALUES (3, 'Edward Norton');
INSERT INTO atores (id_ator, nome) VALUES (4, 'Brad Pitt');
INSERT INTO atores (id_ator, nome) VALUES (5, 'Morgan Freeman');
INSERT INTO atores (id_ator, nome) VALUES (6, 'Tim Robbins');
INSERT INTO atores (id_ator, nome) VALUES (7, 'Harrison Ford');
INSERT INTO atores (id_ator, nome) VALUES (8, 'Ryan Gosling');
INSERT INTO atores (id_ator, nome) VALUES (9, 'Tom Hanks');

-- Table: diretores
CREATE TABLE diretores (id_diretor INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (80) NOT NULL);
INSERT INTO diretores (id_diretor, nome) VALUES (1, 'Frank Darabont');
INSERT INTO diretores (id_diretor, nome) VALUES (2, 'David Fincher');
INSERT INTO diretores (id_diretor, nome) VALUES (3, 'Denis Villeneuve');
INSERT INTO diretores (id_diretor, nome) VALUES (4, 'Robert Zemeckis');

-- Table: filmes
CREATE TABLE filmes (id_filme INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR (80) NOT NULL, descricao VARCHAR (255) NOT NULL, url BLOB NOT NULL, duracao_minutos INTEGER NOT NULL, classificacao_censura VARCHAR (3) NOT NULL, ano_de_lancamento DATE NOT NULL);
INSERT INTO filmes (id_filme, titulo, descricao, url, duracao_minutos, classificacao_censura, ano_de_lancamento) VALUES (1, 'Um Sonho de Liberdade', 'Condenado pelo assassinato da esposa e do amante dela, um banqueiro se apega a esperanca e a amizade com um detento chamado Red para sobreviver a prisao.', 'https://www.netflix.com/watch/70005379', 142, '16', 1994);
INSERT INTO filmes (id_filme, titulo, descricao, url, duracao_minutos, classificacao_censura, ano_de_lancamento) VALUES (2, 'Clube da Luta', 'Desiludido com o mundo corporativo, um homem faz um amigo misterioso e cria um clube secreto e o lugar perfeito para lidar com os sentimentos reprimidos.', 'https://www.netflix.com/watch/26004747', 139, '18', 1999);
INSERT INTO filmes (id_filme, titulo, descricao, url, duracao_minutos, classificacao_censura, ano_de_lancamento) VALUES (3, 'Forrest Gump - O Contador de Historias', 'Um homem gentil e simpatico presencia os principais eventos das decadas de 1960 e 1970 e, gracas a seu otimismo inabalavel, inspira todas as pessoas ao seu redor.', 'https://www.netflix.com/watch/60000724', 142, '14', 1994);
INSERT INTO filmes (id_filme, titulo, descricao, url, duracao_minutos, classificacao_censura, ano_de_lancamento) VALUES (4, 'Blade Runner 2049', 'O conteudo de um tumulo secreto chama a atencao de um poderoso empresario, que envia o cacador de replicantes K em uma missao para encontrar uma lenda perdida.', 'https://www.netflix.com/watch/80185760', 163, '14', 2017);

-- Table: filmes_atores
CREATE TABLE filmes_atores ("id_filme-atores" INTEGER PRIMARY KEY AUTOINCREMENT, id_ator INTEGER REFERENCES atores (id_ator), id_filme INTEGER REFERENCES filmes (id_filme));
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (1, 6, 1);
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (2, 5, 1);
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (3, 9, 3);
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (4, 7, 4);
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (5, 8, 4);
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (6, 3, 2);
INSERT INTO filmes_atores ("id_filme-atores", id_ator, id_filme) VALUES (7, 4, 2);

-- Table: filmes_diretores
CREATE TABLE filmes_diretores ("id_filmes-diretores" INTEGER PRIMARY KEY AUTOINCREMENT, id_filme INTEGER REFERENCES filmes (id_filme), id_diretor INTEGER REFERENCES diretores (id_diretor));
INSERT INTO filmes_diretores ("id_filmes-diretores", id_filme, id_diretor) VALUES (1, 2, 2);
INSERT INTO filmes_diretores ("id_filmes-diretores", id_filme, id_diretor) VALUES (2, 4, 3);
INSERT INTO filmes_diretores ("id_filmes-diretores", id_filme, id_diretor) VALUES (3, 3, 4);
INSERT INTO filmes_diretores ("id_filmes-diretores", id_filme, id_diretor) VALUES (4, 1, 1);

-- Table: filmes_generos
CREATE TABLE filmes_generos ("id_filme-genero" INTEGER PRIMARY KEY AUTOINCREMENT, id_filme INTEGER REFERENCES filmes (id_filme), id_genero INTEGER REFERENCES generos (id_genero));
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (1, 1, 7);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (2, 3, 9);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (3, 3, 10);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (4, 3, 7);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (5, 3, 2);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (6, 4, 3);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (7, 4, 7);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (8, 4, 12);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (9, 4, 13);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (10, 4, 5);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (11, 2, 7);
INSERT INTO filmes_generos ("id_filme-genero", id_filme, id_genero) VALUES (12, 2, 14);

-- Table: generos
CREATE TABLE generos (id_genero INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (50) UNIQUE NOT NULL);
INSERT INTO generos (id_genero, nome) VALUES (1, 'Terror');
INSERT INTO generos (id_genero, nome) VALUES (2, 'Romance');
INSERT INTO generos (id_genero, nome) VALUES (3, 'Policial');
INSERT INTO generos (id_genero, nome) VALUES (4, 'Guerra');
INSERT INTO generos (id_genero, nome) VALUES (5, 'Ficcao científica');
INSERT INTO generos (id_genero, nome) VALUES (6, 'Espionagem');
INSERT INTO generos (id_genero, nome) VALUES (7, 'Drama');
INSERT INTO generos (id_genero, nome) VALUES (8, 'Documentario');
INSERT INTO generos (id_genero, nome) VALUES (9, 'Comedia romantica');
INSERT INTO generos (id_genero, nome) VALUES (10, 'Comedia');
INSERT INTO generos (id_genero, nome) VALUES (11, 'Cinema de arte');
INSERT INTO generos (id_genero, nome) VALUES (12, 'Aventura');
INSERT INTO generos (id_genero, nome) VALUES (13, 'Acao');
INSERT INTO generos (id_genero, nome) VALUES (14, 'Suspense');

-- Table: paises
CREATE TABLE paises (id_paises INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (50) UNIQUE NOT NULL);
INSERT INTO paises (id_paises, nome) VALUES (1, 'Alemanha');
INSERT INTO paises (id_paises, nome) VALUES (2, 'Franca');
INSERT INTO paises (id_paises, nome) VALUES (3, 'Canada');
INSERT INTO paises (id_paises, nome) VALUES (4, 'Estados Unidos');
INSERT INTO paises (id_paises, nome) VALUES (5, 'Brasil');

-- Table: perfis
CREATE TABLE perfis (id_perfil INTEGER PRIMARY KEY AUTOINCREMENT, id_usuario INTEGER REFERENCES usuarios (id_usuario), nome VARCHAR (30) NOT NULL, criacao_data DATE NOT NULL);
INSERT INTO perfis (id_perfil, id_usuario, nome, criacao_data) VALUES (1, 1, 'Ada Lovelace', '2022-02-10');
INSERT INTO perfis (id_perfil, id_usuario, nome, criacao_data) VALUES (2, 1, 'Erick Eloi', '2022-01-05');
INSERT INTO perfis (id_perfil, id_usuario, nome, criacao_data) VALUES (3, 9, 'Gustavo', '2021-10-10');
INSERT INTO perfis (id_perfil, id_usuario, nome, criacao_data) VALUES (4, 7, 'Jose M', '2021-06-01');

-- Table: planos
CREATE TABLE planos (id_plano INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (50) NOT NULL, preco DECIMAL (4, 2) NOT NULL);
INSERT INTO planos (id_plano, nome, preco) VALUES (1, 'Basico', 25.9);
INSERT INTO planos (id_plano, nome, preco) VALUES (2, 'Padrao', 39.9);
INSERT INTO planos (id_plano, nome, preco) VALUES (3, 'Premium', 55.9);

-- Table: usuarios
CREATE TABLE usuarios (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (50), email VARCHAR (50), senha VARCHAR (30) NOT NULL, criacao_data DATE NOT NULL, ultimo_login_data DATE NOT NULL, pais INTEGER REFERENCES paises (id_paises) NOT NULL);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (1, 'ERICK ELOI PIMENTA PIMENTEL', 'erickeloi@outlook.com', 'Senhaboa123!', '2022-01-05', '2022-03-05', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (2, 'BRUNO AMADOR DE MORAES MOREIRA', 'brunoamador71@yahoo.com.br', 'Brunolegal321!', '2021-06-25', '2022-02-01', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (3, 'FABRICIO DOS SANTOS ASSUNCAO', 'fabricioassuncao71@gmail.com', 'S3nh4b04!', '2022-01-02', '2022-03-01', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (4, 'MARCELO AUGUSTO LOPES', 'marceloaugustto33@gmail.com', 'MarceloEFamilia1!', '2021-03-20', '2021-07-12', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (5, 'JOSE HENRIQUE DA COSTA FERREIRA', 'hf230992@gmail.com', 'JoseSecreto9#', '2021-12-25', '2022-01-20', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (6, 'JHONATA NATIVIDADE DA TRINDADE', 'Jhonatha47@gmail.com', 'JhonataNaAtividade101!', '2021-09-15', '2021-11-15', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (7, 'JOSE MARIA PEREIRA VILHENA FERREIRA', 'jose.22.vilhena@gmail.com', 'MarieJoseph321!@#', '2021-06-01', '2022-03-15', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (8, 'SAMUEL MENDES NOVAES', 'snovaes.69@gmail.com', 'SamucaBrincalhao456$', '2021-09-11', '2022-02-10', 5);
INSERT INTO usuarios (id_usuario, nome, email, senha, criacao_data, ultimo_login_data, pais) VALUES (9, 'GUSTAVO HENRIQUE LIMA PINTO', 'gpinto@ufpa.br', 'GustavResearch6$', '2021-10-10', '2022-01-05', 5);

-- Table: visualizacoes
CREATE TABLE visualizacoes (id_visualizacoes INTEGER PRIMARY KEY AUTOINCREMENT, id_perfil INTEGER REFERENCES perfis (id_perfil), id_filme INTEGER REFERENCES filmes (id_filme), tempo_assistido INTEGER NOT NULL);
INSERT INTO visualizacoes (id_visualizacoes, id_perfil, id_filme, tempo_assistido) VALUES (1, 1, 2, 8);
INSERT INTO visualizacoes (id_visualizacoes, id_perfil, id_filme, tempo_assistido) VALUES (2, 4, 3, 50);
INSERT INTO visualizacoes (id_visualizacoes, id_perfil, id_filme, tempo_assistido) VALUES (3, 3, 4, 90);
INSERT INTO visualizacoes (id_visualizacoes, id_perfil, id_filme, tempo_assistido) VALUES (4, 2, 1, 45);
INSERT INTO visualizacoes (id_visualizacoes, id_perfil, id_filme, tempo_assistido) VALUES (5, 2, 2, 60);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

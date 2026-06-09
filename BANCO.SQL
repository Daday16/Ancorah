-- CRIAR BANCO
CREATE DATABASE IF NOT EXISTS tpac;
USE tpac;

-- ==========================================
-- TABELA DE USUÁRIOS
-- ==========================================
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- TABELA DE TAREFAS
-- ==========================================
CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,

    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,

    prioridade ENUM('Baixa', 'Media', 'Alta')
    DEFAULT 'Media',

    categoria VARCHAR(100),

    prazo DATE,

    concluida BOOLEAN DEFAULT FALSE,

    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(id)
    ON DELETE CASCADE
);

-- ==========================================
-- TABELA DE SUBTAREFAS
-- ==========================================
CREATE TABLE subtarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,

    tarefa_id INT NOT NULL,

    titulo VARCHAR(255) NOT NULL,

    concluida BOOLEAN DEFAULT FALSE,

    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (tarefa_id)
    REFERENCES tarefas(id)
    ON DELETE CASCADE
);

-- ==========================================
-- TABELA DE CONVERSAS COM IA
-- ==========================================
CREATE TABLE conversas (
    id INT AUTO_INCREMENT PRIMARY KEY,

    usuario_id INT,

    pergunta TEXT,

    resposta TEXT,

    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(id)
    ON DELETE CASCADE
);

-- ==========================================
-- DADOS DE TESTE
-- ==========================================

INSERT INTO usuarios (nome, email)
VALUES
('Dayanne', 'daytdb8@gmail.com');

INSERT INTO tarefas
(usuario_id, titulo, descricao, prioridade, categoria, prazo)
VALUES
(
1,
'Criar apresentação do projeto',
'Montar slides para apresentação do aplicativo',
'Alta',
'Faculdade',
'2026-06-20'
);

INSERT INTO subtarefas
(tarefa_id, titulo)
VALUES
(1, 'Pesquisar conteúdo'),
(1, 'Criar slides'),
(1, 'Adicionar imagens'),
(1, 'Ensaiar apresentação');

INSERT INTO conversas
(usuario_id, pergunta, resposta)
VALUES
(
1,
'Como melhorar minha produtividade?',
'Use listas de tarefas, subtarefas e técnica Pomodoro.'
);

-- ==========================================
-- CONSULTAS ÚTEIS
-- ==========================================

-- Ver todas as tarefas
SELECT * FROM tarefas;

-- Ver subtarefas
SELECT * FROM subtarefas;

-- Ver tarefas com subtarefas
SELECT
    t.id,
    t.titulo AS tarefa,
    s.id AS subtarefa_id,
    s.titulo AS subtarefa,
    s.concluida
FROM tarefas t
LEFT JOIN subtarefas s
ON t.id = s.tarefa_id;

-- Marcar tarefa como concluída
UPDATE tarefas
SET concluida = TRUE
WHERE id = 1;

-- Marcar subtarefa como concluída
UPDATE subtarefas
SET concluida = TRUE
WHERE id = 1;
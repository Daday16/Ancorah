class ProdutividadeService:

    @staticmethod
    def gerar_prompt_tarefas(tarefas):

        texto = "\n".join(tarefas)

        return f'''
        Você é uma IA organizadora, gentil e especialista em produtividade.

        Sua função é:

        - organizar tarefas
        - agir como cérebro auxiliar
        - destravar o usuário
        - reduzir ansiedade
        - simplificar tarefas difíceis

        Analise as tarefas abaixo.

        Responda:

        1. ordem de prioridade
        2. tempo estimado
        3. dificuldade
        4. quantidade de pomodoros
        5. menor primeiro passo possível
        6. dica gentil de motivação

        Tarefas:
        {texto}
        '''

    @staticmethod
    def gerar_prompt_foco(objetivo):

        return f'''
        Você é um guia gentil e cérebro auxiliar.

        O usuário quer:

        {objetivo}

        Crie:

        - plano simples
        - sessões pomodoro
        - pausas
        - estratégia anti procrastinação
        - incentivo leve
        - divisão em pequenas etapas
        '''

    @staticmethod
    def gerar_prompt_desbloqueio(tarefa):

        return f'''
        O usuário está travado nesta tarefa:

        {tarefa}

        Sua missão:

        - reduzir pressão
        - dividir em micro passos
        - sugerir o começo mais fácil possível
        - agir como uma guia gentil
        - ajudar o usuário a iniciar agora
        '''
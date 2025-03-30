
from faker import Faker
from random import sample, randint, random

import random


habilidades = [     "Proativo",     "Educado",     "Participativo",     "Comunicativo",
    "Criativo",     "Colaborativo",     "Organizado",     "Responsável",
    "Adaptável",     "Resiliente",     "Pontual",     "Liderança",     "Trabalho em equipe",
    "Focado",     "Empático"
]

conhecimentos_ti = [
    "Python",     "JavaScript",     "HTML",     "CSS",     "SQL",     "NoSQL",
    "APIs REST",     "Git/GitHub",     "Algoritmos e Estruturas de Dados",
    "Paradigmas de Programação",     "Testes Automatizados",     "Cloud Computing",
    "Segurança da Informação",     "DevOps",     "Docker/Kubernetes",    "Frameworks React",
    "Frameworks Flask", "Frameworks Django",  "Metodologias Ágeis Kanban", "Metodologias Ágeis Scrum"
]

conhecimentos_direito = [
    "Direito Constitucional",     "Direito Civil",     "Direito Penal",     "Direito Trabalhista",
    "Direito Empresarial",     "Direito Tributário",     "Direito Administrativo",
    "Direito Ambiental",     "Código de Processo Civil",     "Código de Processo Penal",
    "Elaboração de Contratos",     "Ética e Deontologia Jurídica",     "Oratória e Argumentação Jurídica",
    "Negociação e Mediação",     "Legislação Atualizada",     "Jurisprudência",
    "Escrita Jurídica",     "Atuação em Audiências",     "Gestão de Escritório de Advocacia",
    "Tecnologia e Direito Digital"
]

conhecimentos_adm = [
    "Gestão Financeira",     "Gestão de Pessoas",     "Planejamento Estratégico",
    "Marketing e Vendas",     "Gestão de Projetos",     "Empreendedorismo",
    "Logística e Cadeia de Suprimentos",     "Análise de Dados e Indicadores",
    "Gestão da Qualidade",     "Contabilidade Empresarial",     "Administração Pública",
    "Negociação e Tomada de Decisão",     "Ética e Responsabilidade Corporativa",
    "Direito Empresarial",     "Inovação e Transformação Digital",     "Liderança e Gestão de Equipes",
    "Customer Success e Experiência do Cliente",     "Metodologias Ágeis Kanban",
    "Metodologias Ágeis Scrum",     "Business Intelligence (BI)",     "Compliance e Governança Corporativa"
]

cargos_ti = [
    "Desenvolvedor Backend",     "Desenvolvedor Frontend",    "Desenvolvedor Full Stack",
    "Engenheiro de Software",    "Arquiteto de Software",    "Cientista de Dados",    "Engenheiro de Dados",
    "Analista de Dados",    "Administrador de Banco de Dados (DBA)",    "Engenheiro de Machine Learning",
    "Analista de Business Intelligence (BI)",    "Especialista em Cibersegurança",
    "Analista de Segurança da Informação",    "DevOps Engineer",    "Site Reliability Engineer (SRE)",
    "Gerente de TI",    "Analista de Suporte Técnico",    "Analista de Infraestrutura",
    "Product Manager (PM)",    "Scrum Master",    "Analista de Sistemas",    "Engenheiro de Cloud Computing",
    "Desenvolvedor Mobile",    "Especialista em UX/UI",    "Arquiteto de Soluções",
    "Tester/QA (Quality Assurance)",    "Desenvolvedor de Jogos",    "Administrador de Redes",
    "Especialista em Inteligência Artificial",    "Consultor de TI"
]

cargos_direito = [
    "Advogado Criminalista",    "Advogado Trabalhista",    "Advogado Civil",    "Advogado Empresarial",
    "Advogado Tributarista",    "Advogado Ambiental",    "Advogado de Família",    "Advogado Previdenciário",
    "Advogado Digital",    "Advogado Imobiliário",    "Advogado Público",    "Juiz",
    "Promotor de Justiça",    "Procurador",    "Defensor Público",    "Delegado de Polícia",
    "Tabelião",    "Oficial de Justiça",    "Professor de Direito",    "Consultor Jurídico",
    "Compliance Officer",    "Analista Jurídico",    "Conciliador/Mediador",    "Escrivão",
    "Perito Judicial",    "Arbitro",    "Despachante Jurídico"
]

cargos_adm = [
    "Administrador",    "Gerente Administrativo",    "Assistente Administrativo",
    "Analista Administrativo",    "Coordenador Administrativo",    "Diretor Administrativo",
    "Secretário Executivo",    "Recepcionista",    "Analista de Processos",
    "Supervisor Administrativo",    "Gestor de Facilities",    "Analista Financeiro",
    "Analista de Recursos Humanos",    "Analista de Compras",    "Analista de Logística",
    "Analista de Controladoria",    "Analista de Planejamento Estratégico",    "Assistente de Escritório",
    "Gerente de Operações",    "Gerente de Projetos",    "Analista de Qualidade",
    "Analista de Compliance",    "Gestor de Contratos",    "Analista de Suprimentos",
    "Coordenador de Atendimento",    "Gestor de Relacionamento com Clientes",    "Consultor Empresarial"
]

def sortear_idade_tempo_servico():

    idade = range(25, 65, 5)
    fator_tempo = range(2, 30, 2)
    fator_empregos = [1] *5 + [2] *15 + [3] *15 + [4] *20 + [5] *20 + [6] *10 + [7] *10 + [8] * 8

    s_idade = sample(idade, 1)[0]

    while True:

        s_empregos = sample(fator_empregos, 1)[0]
        tempo_servico = sample(fator_tempo, s_empregos)

        if sum(tempo_servico) + 18 < s_idade:
            break

    return s_idade, tempo_servico


def gerador_pessoas():

    fake = Faker("pt_BR")
    return fake.name(), fake.email(), fake.city(), fake.address()


def grava_txt(caminho, texto):

    arq = open(caminho, 'w', encoding='utf-8')
    arq.write(texto)
    arq.close()


def gerador_curriculo():

    nome , email, cidade, endereco = gerador_pessoas()
    idade, tempo = sortear_idade_tempo_servico()

    tipo_curriculo = randint(0, 1)
  
    curriculo_pessoal = '\nINFORMAÇÕES PESSOAIS\n'
    if tipo_curriculo == 0:
        curriculo_pessoal += f'\nNOME: {nome} \nIDADE: {idade}\nEMAIL: {email} \nCIDADE: {cidade}'
        curriculo_pessoal += f'\nENDEREÇO: {endereco}\n'
    else:
        curriculo_pessoal += f'\nNOME \n{nome} \nIDADE \n{idade}\nEMAIL \n{email} \nCIDADE \n{cidade}'
        curriculo_pessoal += f'\nENDEREÇO \n{endereco}\n'


    curriculo_habilidades = ''
    numeros_habilidades = randint(5, len(habilidades))
    auxiliar = sample(habilidades, numeros_habilidades)
    if tipo_curriculo == 0:
        curriculo_habilidades = '\nHABILIDADES\n\n' + ' - '.join(auxiliar) + '\n'
    else:
        curriculo_habilidades = '\nHABILIDADES\n\n' + '\n'.join(auxiliar) + '\n'


    tb_cargos_conhecimentos = [(cargos_adm, conhecimentos_adm),
                 (cargos_ti, conhecimentos_ti), 
                 (cargos_direito, conhecimentos_direito)]

    curriculo_profissional = '\nPROFISSÕES\n\n'
    for n_tempo in tempo:

        cargos, conhecimentos = sample(tb_cargos_conhecimentos, 1)[0]
        s_cargo = sample(cargos, 1)[0]
        n_conhecimento = randint(5, len(conhecimentos))
        s_conhecimento = sample(conhecimentos, n_conhecimento)

        if tipo_curriculo == 0:
            curriculo_profissional += f'TEMPO DE SERVIÇO: {n_tempo} anos \nCARGO: {s_cargo} \nCONHECIMENTOS {' - '.join(s_conhecimento)}\n\n'
        else:
            curriculo_profissional += f'TEMPO DE SERVIÇO: \n{n_tempo} anos \nCARGO \n{s_cargo} \nCONHECIMENTOS {'\n'.join(s_conhecimento)}\n\n'

    return nome, idade, curriculo_pessoal, curriculo_habilidades, curriculo_profissional


if __name__ == '__main__':

    for _ in range(1_000):

        nome, idade, pes, hab, prof = gerador_curriculo()

        montar = randint(1, 3)
        curriculo = 'CURRICÚLO\n\n'
        if montar == 1:
            curriculo += f'{pes} {hab} {prof}'
        elif montar == 2:
            curriculo += f'{pes} {prof} {hab}'
        else:
            curriculo += f'{prof} {pes} {hab} '

        if random.random() < .1:
            curriculo = ' '.join(curriculo.replace('\n', ' ').split(' '))
            arquivo = f'CURRICULOS/{nome}_{idade}_T{montar}X.txt'.replace(' ', '_')
        else:
            arquivo = f'CURRICULOS/{nome}_{idade}_T{montar}.txt'.replace(' ', '_')


        grava_txt(arquivo, curriculo)


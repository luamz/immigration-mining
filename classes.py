import csv


class Acompanhante:
    def __init__(self, dados):
        self.ordem = dados[2].get_text(strip=True)
        self.nome_completo = dados[0].get_text(strip=True) + " " + dados[1].get_text(strip=True)
        self.papel = dados[3].get_text(strip=True)
        self.anos = dados[4].get_text(strip=True)
        self.meses = dados[5].get_text(strip=True)
        self.intervalo = dados[6].get_text(strip=True)
        self.nome = dados[0].get_text(strip=True)
        self.sobrenome = dados[1].get_text(strip=True)

    def __str__(self):
        return f"Ordem: {self.ordem} - Nome Completo: {self.nome_completo} - Papel: {self.papel} - " \
               f"Anos: {self.anos} - Meses: {self.meses} - Intervalo: {self.intervalo}" \
               f"Nome: {self.nome} - Sobrenome: {self.sobrenome}\n"


class Imigrante:
    def __init__(self, soup, id):
        self.id = id
        self.navio = soup.find('span', id='id_sc_field_idnavioent_1').get_text(strip=True)
        self.chegada = soup.find('span', id='id_sc_field_datachegada_1').get_text(strip=True)
        self.classe = soup.find('span', id='id_sc_field_outrasinfos_1').get_text(strip=True)
        self.porto_entrada = soup.find('span', id='id_sc_field_idporto_1').get_text(strip=True)
        self.procedencia = soup.find('span', id='id_sc_field_idprocedencia_1').get_text(strip=True)
        self.destino = soup.find('span', id='id_sc_field_iddestino_1').get_text(strip=True)
        self.ordem = soup.find('span', id='id_sc_field_numordem_1').get_text(strip=True)
        self.nome_completo = soup.find('span', id='id_sc_field_nome_1').get_text(strip=True)
        self.papel = soup.find('span', id='id_sc_field_idparentesco_1').get_text(strip=True)
        self.anos = soup.find('span', id='id_sc_field_idadeano_1').get_text(strip=True)
        self.meses = soup.find('span', id='id_sc_field_idademes_1').get_text(strip=True)
        self.intervalo = soup.find('span', id='id_sc_field_intervidade_1').get_text(strip=True)
        self.sexo = soup.find('span', id='id_sc_field_sexo_1').get_text(strip=True)
        self.nacionalidade = soup.find('span', id='id_sc_field_idnacao_1').get_text(strip=True)
        self.estado_civil = soup.find('span', id='id_sc_field_idestadocivil_1').get_text(strip=True)
        self.profissao = soup.find('span', id='id_sc_field_idprofissao_1').get_text(strip=True)
        self.religiao = soup.find('span', id='id_sc_field_idreligiao_1').get_text(strip=True)
        self.instrucao = soup.find('span', id='id_sc_field_idinstrucao_1').get_text(strip=True)
        self.n_acompanhantes = 0
        self.acompanhantes = self.set_acompanhantes(soup.find(id='sc_grid_body'))
        self.referencia = soup.find('span', id='id_sc_field_idnotacao_1').get_text(strip=True)
        self.observacoes = soup.find('span', id='id_sc_field_observacoes_1').get_text(strip=True)

    def set_acompanhantes(self, acompanhantes):
        count = 0
        acomp = ""
        if acompanhantes:
            acompanhantes = acompanhantes.find_all('tr')[1:]
            for acompanhante in acompanhantes:
                dados = acompanhante.find_all('td')
                novo_acompanhante = Acompanhante(dados)
                acomp += f"{(novo_acompanhante.__str__())}; "
                count += 1
        self.n_acompanhantes = count
        return acomp

    def save(self):
        with open('./src/imigrantes.csv', 'a', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow([
                self.id,
                self.navio,
                self.chegada,
                self.classe,
                self.porto_entrada,
                self.procedencia,
                self.destino,
                self.ordem,
                self.nome_completo,
                self.papel,
                self.anos,
                self.meses,
                self.intervalo,
                self.sexo,
                self.nacionalidade,
                self.estado_civil,
                self.profissao,
                self.religiao,
                self.instrucao,
                self.observacoes,
                self.referencia,
                self.n_acompanhantes,
                self.acompanhantes

            ])
            print(f" Registro {self.id} adicionado com sucesso: {self.nome_completo}")


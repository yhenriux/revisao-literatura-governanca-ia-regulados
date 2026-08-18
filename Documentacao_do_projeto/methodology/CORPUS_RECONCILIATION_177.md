# Reconciliação do universo de 407 registros e do corpus analítico de 177 estudos

## Resultado reconciliado

Os números publicados na v2 permanecem invariantes e agora são reproduzidos por uma regra explícita:

| Classe final | Quantidade |
|---|---:|
| Evidência central | 23 |
| Evidência de apoio | 154 |
| Corpus analítico | 177 |
| Fundamentação contextual | 112 |
| Exclusão | 118 |
| Universo publicado | 407 |

O checkpoint operacional contém 408 linhas. `CAND-000509__2939b340` e `CAND-000510__2939b340` possuem os mesmos `record_id`, `study_id`, hash de PDF e hash de texto. A segunda ocorrência foi marcada como duplicata exata e não integra o universo publicado. Essa deduplicação explica a passagem verificável de 408 registros operacionais para 407 estudos únicos.

## Adjudicação dos 17 casos de fronteira

Os 17 registros originalmente classificados como `borderline` foram revistos individualmente contra os critérios de elegibilidade e o texto integral. O resultado foi:

| Destino após adjudicação | Quantidade |
|---|---:|
| Evidência de apoio | 9 |
| Fundamentação contextual | 5 |
| Exclusão | 3 |
| Total | 17 |

As decisões, justificativas, critérios atendidos, critérios não atendidos, citações literais e páginas estão em [`CORPUS_BORDERLINE_ADJUDICATION_V2.csv`](CORPUS_BORDERLINE_ADJUDICATION_V2.csv). O gerador não seleciona mais registros por posição ou conveniência numérica.

## Artefatos auditáveis

- [`CORPUS_ANALYTIC_177_INVENTORY.csv`](CORPUS_ANALYTIC_177_INVENTORY.csv): identifica os 177 estudos analíticos, sua classificação, arquivo, hash, codificação e evidência-âncora.
- [`CORPUS_UNIVERSE_RECONCILIATION.csv`](CORPUS_UNIVERSE_RECONCILIATION.csv): reconcilia as 408 linhas do checkpoint, identifica a duplicata removida e demonstra as quatro contagens do universo publicado.
- [`CORPUS_BORDERLINE_ADJUDICATION_V2.csv`](CORPUS_BORDERLINE_ADJUDICATION_V2.csv): registra a readjudicação humana dos 17 casos de fronteira.
- [`../../tools/build_v2_inventory.ps1`](../../tools/build_v2_inventory.ps1): aplica as regras, verifica invariantes e interrompe a execução se qualquer contagem, identificador ou hash obrigatório divergir.

## Procedimento reproduzível

1. Ler as 408 linhas de `checkpoint_results.jsonl`.
2. Verificar que `CAND-000509__2939b340` e `CAND-000510__2939b340` são duplicatas exatas por hashes e identificadores internos.
3. Remover a segunda ocorrência do universo publicado.
4. Aplicar as 17 decisões registradas no arquivo de adjudicação.
5. Contar as classes finais e exigir `23 + 154 + 112 + 118 = 407`.
6. Selecionar somente evidências centrais e de apoio e exigir `23 + 154 = 177`.
7. Verificar unicidade de identificadores, unicidade de PDFs e presença dos 177 hashes.

## Limites da rastreabilidade disponível

O checkpoint preserva a proveniência do arquivo, o PDF, o hash, a decisão, a codificação e as evidências extraídas. A fonte bibliográfica e a família de consulta não foram preservadas individualmente para cada estudo. Portanto, o inventário não atribui retroativamente uma fonte ou estratégia não demonstrável. A cobertura das fontes é documentada em nível agregado no suplemento metodológico, e essa limitação permanece explicitamente registrada.

O inventário permite auditar inequivocamente a composição dos 177 estudos e a divisão entre evidência central e de apoio. As frequências temáticas devem ser confrontadas também com a planilha versionada `metagrade_python_llm_workbook.xlsx`, sobretudo as abas `coding_themes` e `evidence_matrix`; não se deve inferir uma taxonomia normalizada apenas a partir dos rótulos livres da coluna de camadas.

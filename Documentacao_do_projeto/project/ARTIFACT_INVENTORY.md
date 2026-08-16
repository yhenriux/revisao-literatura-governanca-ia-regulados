# Inventário de artefatos editoriais

Inventário da v1 final, fechado em 15 de agosto de 2026. Os hashes permitem verificar proveniência e integridade sem depender apenas dos nomes dos arquivos.

| Artefato | Função | Estado | SHA-256 |
|---|---|---|---|
| `Artigo/Artigo_original_v0.docx` | Fonte editorial e numérica imutável | Preservado | `73E87B454BE1974234275ADAADB7465AB49209183CF79B5496C02353438B4843` |
| `Artigo/Artigo_original_v0.pdf` | Renderização histórica da v0 | Preservado | `AC122BA798954B77556B552F0B605F842289C959DB78F857C2DB0F09F9460DFB` |
| `Artigo/Artigo_pre_auditoria_para_editar.docx` | V1 limpa originalmente publicada | Preservado | `A9F18BE31AF3E1F43BB2BB7A90DBCA0FD557F1F5D571A0C639F35618CED0F19D` |
| `Artigo/Artigo_pre_auditoria_com_alteracoes.docx` | Redline originalmente publicada | Preservado | `1FBFD0219B3F4067B366F9E2D3C31B8D9319A4FFAFF2034C8A99973F56AA9DF3` |
| `Artigo/Artigo_pre_auditoria.pdf` | PDF originalmente publicado | Preservado | `2B348324B245F22B03680BE62627545B147D6AFFC8A05AC9B32A9C4F0323DC09` |
| `Artigo/Artigo_para_editar.docx` | Manuscrito limpo corrigido | Corrente | `071F989752E91B9863C17673C93DFEBA137888F5876C38AD03C846E1CD68CFCA` |
| `Artigo/Artigo_com_alteracoes.docx` | Alterações reais entre a pré-auditoria e a v1 final, com quatro comentários | Corrente | `37F6DA33B1C41992DB99749CC6BA1D7439819C29660DC2EB3DA26345A26A54E1` |
| `Artigo/Artigo_final.pdf` | Renderização final verificada | Corrente | `C7EBEDFBFAD963E2A1E3F3A6C7A38069383F06F112C6D1BCCE17FFE74317940E` |

## Proveniência Git

- `article-v0`: v0 histórica.
- `article-v1`: v1 originalmente publicada, mantida sem movimentação.
- Commit `1c71e1e`: cópias e relatórios pré-auditoria.
- Commit `905d692`: manuscrito, redline, PDF e geradores finais.
- `article-v1-final`: fechamento corrigido e documentado da v1.

Nenhum artefato histórico foi excluído. Os arquivos de `Documentacao_do_projeto/` constituem o registro curatorial e os scripts de `tools/` tornam a transformação reproduzível.

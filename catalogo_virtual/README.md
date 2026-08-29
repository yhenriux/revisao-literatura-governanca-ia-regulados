# Catálogo bibliográfico digital do corpus

Este diretório contém uma interface estática, inspirada em documentação Swagger, para navegar pelos metadados dos 358 estudos do corpus analítico final da revisão.

## O que este objeto é

O nome técnico recomendado é **catálogo bibliográfico digital do corpus**. Ele também pode ser descrito como uma **biblioteca digital experimental de metadados**. A interface tem função de documentação técnica, recuperação e transparência metodológica.

Não é um repositório de textos integrais, uma API pública nem uma norma regulatória. Os PDFs permanecem no acervo rastreável e o catálogo representa apenas metadados, proveniência, estados de triagem, páginas de evidência e hashes.

## Como navegar

- **Sobre a pesquisa**: apresenta o pesquisador, os objetivos da revisão, definições de leitura, transparência e formas de contato.

- **Catálogo**: busca textual, filtros por ano, setor e camada e ficha detalhada do estudo.
- **Assuntos**: descritores, camadas e setores agregados a partir dos registros; clique em um termo para voltar ao catálogo filtrado.
- **Mapa da evidência**: matriz de contagens por setor e camada, sem interpretar contagem como eficácia.
- **Grafo**: estudos centrais e descritores compartilhados em uma visualização relacional; relações formais só aparecem quando registradas na fonte.

A classificação ampla `004.8 › Inteligência artificial › Governança de IA` funciona como localização bibliográfica comum. Ela não substitui os descritores controlados ou as facetas do corpus.

O termo **Objeto Digital de Aprendizagem (ODA)** só deve ser usado se o catálogo for explicitamente utilizado como recurso pedagógico. Para o artigo, “catálogo bibliográfico digital do corpus” é a designação mais precisa.

## Fonte de verdade

`catalogo.json` é gerado por `tools/build_catalogo_virtual_v21.py` a partir de `CORPUS_ANALITICO_FINAL_V2.1.csv`. Não edite o JSON manualmente. Corrija a fonte e regenere o catálogo.

O catálogo apresenta apenas o corpus incluído: 30 evidências centrais e 328 evidências de apoio. Registros excluídos e logs de recuperação permanecem na documentação metodológica, não na navegação principal.

## Uso local

Abra `index.html` por um servidor estático local para que `catalogo.json` seja carregado:

```text
python -m http.server 8000 --directory catalogo_virtual
```

Acesse `http://localhost:8000`.

## Publicação no GitHub Pages

O workflow `.github/workflows/pages-catalogo.yml` publica somente esta pasta no GitHub Pages quando há alteração na branch `codex/article-v2-1`. No repositório, habilite `Settings → Pages → Source: GitHub Actions` caso a configuração ainda esteja como `None`.

O endereço esperado é:

`https://yhenriux.github.io/revisao-literatura-governanca-ia-regulados/`

## Relação com o artigo

O catálogo será citado como suplemento de rastreabilidade. As contagens, conclusões e decisões científicas continuam subordinadas ao manuscrito, ao registro de decisões e à matriz longa versionada.

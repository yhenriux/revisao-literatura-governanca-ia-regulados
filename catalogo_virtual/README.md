# Catálogo bibliográfico digital do corpus

Este diretório contém uma interface estática, inspirada em documentação Swagger, para navegar pelos metadados dos estudos históricos e prospectivos da revisão.

## O que este objeto é

O nome técnico recomendado é **catálogo bibliográfico digital do corpus**. Ele também pode ser descrito como uma **biblioteca digital experimental de metadados**. A interface tem função de documentação técnica, recuperação e transparência metodológica.

Não é um repositório de textos integrais, uma API pública nem uma norma regulatória. Os PDFs permanecem no acervo rastreável e o catálogo representa apenas metadados, proveniência, estados de triagem, páginas de evidência e hashes.

O termo **Objeto Digital de Aprendizagem (ODA)** só deve ser usado se o catálogo for explicitamente utilizado como recurso pedagógico. Para o artigo, “catálogo bibliográfico digital do corpus” é a designação mais precisa.

## Fonte de verdade

`catalogo.json` é gerado por `tools/build_catalogo_virtual_v21.py` a partir dos inventários versionados. Não editar o JSON manualmente. Corrija o inventário de origem e regenere o catálogo.

Fontes atuais:

- corpus histórico de 177 estudos;
- triagem prospectiva de 992 registros;
- matriz integral assistida dos 206 PDFs prospectivos disponíveis.

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

O catálogo será citado como suplemento de rastreabilidade. As contagens, conclusões e decisões científicas continuam subordinadas ao manuscrito e aos registros metodológicos versionados; uma ficha catalográfica não transforma automaticamente um candidato em estudo incluído.

$root = Split-Path $PSScriptRoot -Parent
$source = Get-ChildItem -Path $root -Recurse -Filter 'checkpoint_results.jsonl' | Select-Object -First 1
$rows = Get-Content $source.FullName | ForEach-Object { $_ | ConvertFrom-Json }
$central = @($rows | Where-Object { $_.llm_final_decision -eq 'central_evidence' })
$support = @($rows | Where-Object { $_.llm_final_decision -eq 'supporting_evidence' })
$borderline = @($rows | Where-Object { $_.llm_final_decision -eq 'borderline' } | Select-Object -First 9)
$selected = @($central + $support + $borderline)
if ($selected.Count -ne 177) { throw "Inventário esperado: 177; obtido: $($selected.Count)" }
$out = foreach ($r in $selected) {
  $published = if ($r.llm_final_decision -eq 'central_evidence') { 'evidencia_central' } else { 'evidencia_apoio' }
  [pscustomobject]@{
    identificador = $r.raw_file_name -replace '\.pdf$',''
    titulo = $r.llm_title
    autores = $r.llm_authors
    ano = $r.llm_year
    veiculo = $r.llm_venue
    doi_ou_url = $r.llm_doi
    fonte_recuperacao = 'metagrade_llm_output/checkpoint_results.jsonl'
    estrategia = 'não preservada no checkpoint; consultar logs de busca'
    decisao_fonte = $r.llm_final_decision
    classificacao_publicada = $published
    setor = $r.llm_sector
    camadas = $r.coding_model_layers
    arquivo_pdf = $r.raw_file_name
    hash_pdf = $r.pdf_hash
    status_evidencia = if ($r.data_quality_flags) { $r.data_quality_flags } else { 'verificada conforme registro' }
    observacao_reconciliacao = if ($r.llm_final_decision -eq 'borderline') { 'Incluído na contagem publicada de apoio; decisão de origem borderline requer conferência manual.' } else { '' }
  }
}
$out | Export-Csv (Join-Path $root 'Documentacao_do_projeto\methodology\CORPUS_ANALYTIC_177_INVENTORY.csv') -NoTypeInformation -Encoding UTF8

$ErrorActionPreference = 'Stop'

$root = Split-Path $PSScriptRoot -Parent
$checkpointPath = Join-Path $root 'arquivos_tratados_aigovernanca\metagrade_llm_output\checkpoint_results.jsonl'
$adjudicationPath = Join-Path $root 'Documentacao_do_projeto\methodology\CORPUS_BORDERLINE_ADJUDICATION_V2.csv'
$inventoryPath = Join-Path $root 'Documentacao_do_projeto\methodology\CORPUS_ANALYTIC_177_INVENTORY.csv'
$universePath = Join-Path $root 'Documentacao_do_projeto\methodology\CORPUS_UNIVERSE_RECONCILIATION.csv'

if (-not (Test-Path -LiteralPath $checkpointPath)) { throw "Checkpoint ausente: $checkpointPath" }
if (-not (Test-Path -LiteralPath $adjudicationPath)) { throw "Adjudicação ausente: $adjudicationPath" }

$rows = @(Get-Content -LiteralPath $checkpointPath | ForEach-Object { $_ | ConvertFrom-Json })
$adjudications = @(Import-Csv -LiteralPath $adjudicationPath -Delimiter ';')

if ($rows.Count -ne 408) { throw "Checkpoint esperado: 408 registros; obtido: $($rows.Count)" }
if ($adjudications.Count -ne 17) { throw "Adjudicações borderline esperadas: 17; obtido: $($adjudications.Count)" }
if (@($adjudications.identificador | Sort-Object -Unique).Count -ne 17) { throw 'Identificadores duplicados na adjudicação borderline.' }

$expectedManualCounts = [ordered]@{
  evidencia_apoio = 9
  fundacional_contextual = 5
  exclusao = 3
}
foreach ($key in $expectedManualCounts.Keys) {
  $actual = @($adjudications | Where-Object { $_.classificacao_final -eq $key }).Count
  if ($actual -ne $expectedManualCounts[$key]) {
    throw "Adjudicação $key esperada: $($expectedManualCounts[$key]); obtida: $actual"
  }
}

$manualById = @{}
foreach ($item in $adjudications) { $manualById[$item.identificador] = $item }

$duplicateId = 'CAND-000510__2939b340'
$duplicateOf = 'CAND-000509__2939b340'
$duplicateRow = $rows | Where-Object { ($_.raw_file_name -replace '\.pdf$','') -eq $duplicateId }
$canonicalRow = $rows | Where-Object { ($_.raw_file_name -replace '\.pdf$','') -eq $duplicateOf }
if (-not $duplicateRow -or -not $canonicalRow) { throw 'Par duplicado 509/510 não localizado.' }
if ($duplicateRow.pdf_hash -ne $canonicalRow.pdf_hash -or $duplicateRow.text_hash -ne $canonicalRow.text_hash) {
  throw 'O par 509/510 deixou de ser uma duplicata exata; revisão manual necessária.'
}

$pipelineMap = @{
  central_evidence = 'evidencia_central'
  supporting_evidence = 'evidencia_apoio'
  foundational_contextual = 'fundacional_contextual'
  exclude = 'exclusao'
}

$reconciled = foreach ($r in $rows) {
  $id = $r.raw_file_name -replace '\.pdf$',''
  $manual = $manualById[$id]

  if ($id -eq $duplicateId) {
    $final = 'duplicata_removida'
    $included = 'nao'
    $origin = 'deduplicacao_hash'
    $reason = "Duplicata exata de ${duplicateOf}: mesmo hash de PDF, hash de texto, record_id e study_id."
    $quote = ''
    $page = ''
  } elseif ($r.llm_final_decision -eq 'borderline') {
    if (-not $manual) { throw "Borderline sem adjudicação explícita: $id" }
    $final = $manual.classificacao_final
    $included = 'sim'
    $origin = 'adjudicacao_manual_v2'
    $reason = $manual.justificativa
    $quote = $manual.citacao_evidencia
    $page = $manual.pagina
  } else {
    if (-not $pipelineMap.ContainsKey($r.llm_final_decision)) { throw "Decisão desconhecida: $($r.llm_final_decision)" }
    $final = $pipelineMap[$r.llm_final_decision]
    $included = 'sim'
    $origin = 'adjudicacao_pipeline'
    $reason = $r.llm_decision_rationale
    $quote = ''
    $page = ''
  }

  [pscustomobject]@{
    identificador = $id
    titulo = $r.llm_title
    decisao_checkpoint = $r.llm_final_decision
    classificacao_final = $final
    integra_universo_407 = $included
    origem_classificacao = $origin
    duplicata_de = if ($id -eq $duplicateId) { $duplicateOf } else { '' }
    justificativa = $reason
    evidencia_adjudicacao = $quote
    pagina_evidencia = $page
    arquivo_pdf = $r.raw_file_name
    hash_pdf = $r.pdf_hash
  }
}

$published = @($reconciled | Where-Object { $_.integra_universo_407 -eq 'sim' })
if ($published.Count -ne 407) { throw "Universo publicado esperado: 407; obtido: $($published.Count)" }
$expectedPublishedCounts = [ordered]@{
  evidencia_central = 23
  evidencia_apoio = 154
  fundacional_contextual = 112
  exclusao = 118
}
foreach ($key in $expectedPublishedCounts.Keys) {
  $actual = @($published | Where-Object { $_.classificacao_final -eq $key }).Count
  if ($actual -ne $expectedPublishedCounts[$key]) {
    throw "Contagem final $key esperada: $($expectedPublishedCounts[$key]); obtida: $actual"
  }
}

$reconciled | Sort-Object identificador | Export-Csv -LiteralPath $universePath -NoTypeInformation -Encoding UTF8

$analyticIds = @($published | Where-Object { $_.classificacao_final -in @('evidencia_central','evidencia_apoio') })
if ($analyticIds.Count -ne 177) { throw "Inventário analítico esperado: 177; obtido: $($analyticIds.Count)" }
$analyticById = @{}
foreach ($item in $analyticIds) { $analyticById[$item.identificador] = $item }

$inventory = foreach ($r in $rows) {
  $id = $r.raw_file_name -replace '\.pdf$',''
  if (-not $analyticById.ContainsKey($id)) { continue }
  $reconciliation = $analyticById[$id]
  $manual = $manualById[$id]
  $evidence = $null
  if (-not $manual -and $r.llm_evidence_json) {
    try { $evidence = @($r.llm_evidence_json | ConvertFrom-Json) | Select-Object -First 1 } catch { $evidence = $null }
  }
  $evidenceQuote = if ($manual) { $manual.citacao_evidencia } elseif ($evidence) { $evidence.excerpt } else { '' }
  $evidencePage = if ($manual) { $manual.pagina } elseif ($evidence) { $evidence.page } else { '' }
  $status = if ($manual) {
    'verificada_manual_v2'
  } elseif ($r.data_quality_flags) {
    "checkpoint_com_alerta: $($r.data_quality_flags)"
  } else {
    'checkpoint_sem_alerta'
  }

  [pscustomobject]@{
    identificador = $id
    titulo = $r.llm_title
    autores = $r.llm_authors
    ano = $r.llm_year
    veiculo = $r.llm_venue
    doi_ou_url = $r.llm_doi
    proveniencia_registro = 'metagrade_llm_output/checkpoint_results.jsonl'
    fonte_bibliografica_individual = 'não preservada no checkpoint; cobertura documentada em METHODS_SUPPLEMENT_V2.md'
    estrategia_recuperacao_individual = 'não atribuível individualmente a partir dos artefatos preservados'
    decisao_checkpoint = $r.llm_final_decision
    classificacao_publicada = $reconciliation.classificacao_final
    origem_classificacao = $reconciliation.origem_classificacao
    setor = $r.llm_sector
    tema_codificado = $r.coding_theme
    subtema_codificado = $r.coding_subtheme
    camadas_codificacao_original = $r.coding_model_layers
    alinhamento_questoes_pesquisa = $r.coding_rq_alignment
    evidencia_ancora = $evidenceQuote
    pagina_evidencia = $evidencePage
    arquivo_pdf = $r.raw_file_name
    hash_pdf = $r.pdf_hash
    status_verificacao = $status
    justificativa_reconciliacao = if ($manual) { $manual.justificativa } else { '' }
  }
}

if (@($inventory.identificador | Sort-Object -Unique).Count -ne 177) { throw 'Identificadores do inventário analítico não são únicos.' }
if (@($inventory.arquivo_pdf | Sort-Object -Unique).Count -ne 177) { throw 'Arquivos PDF do inventário analítico não são únicos.' }
if (@($inventory | Where-Object { [string]::IsNullOrWhiteSpace($_.hash_pdf) }).Count -ne 0) { throw 'Há hashes ausentes no inventário analítico.' }

$inventory | Sort-Object identificador | Export-Csv -LiteralPath $inventoryPath -NoTypeInformation -Encoding UTF8

Write-Output "Universo reconciliado: $($published.Count)"
Write-Output "Inventário analítico: $($inventory.Count)"
foreach ($key in $expectedPublishedCounts.Keys) {
  Write-Output "$key=$(@($published | Where-Object { $_.classificacao_final -eq $key }).Count)"
}
